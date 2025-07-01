import pandas as pd
import os
import re

def extract_info(column_name_mapping):
    """
    Extracts table names and mapping keys from a column_name_mapping string.
    """
    brackets_content = re.findall(r'\((.*?)\)', column_name_mapping)
    text_outside_brackets = re.sub(r'\(.*?\)', '', column_name_mapping)
    words_outside_brackets = [word.strip() for word in re.split(r'\bAND\b|\bCOMB\b', text_outside_brackets) if word.strip()]
    return words_outside_brackets, brackets_content

def process_picklist_replacements(data, template_path):
    """
    Process picklist replacements by mapping values from source columns to target columns
    using specified picklist files. The configuration is read from the template file.

    Args:
        data: DataFrame containing data to process
        template_path: Path to Excel template containing picklist configuration

    Returns:
        DataFrame with picklist replacements applied
    """
    try:
        # Read template configuration with first row as header
        template_data = pd.read_excel(template_path, dtype=str, header=0)

        # Verify template has minimum required rows for configuration
        if template_data.shape[0] < 9:
            print("Template missing picklist configuration rows. Skipping picklist processing.")
            return data

        # Extract configuration from specific template rows:
        # - Header row contains target column names
        # - Row 8 contains source columns in picklists
        # - Row 7 contains picklist filenames
        # - Row 6 contains result columns from picklists
        target_columns = template_data.columns.tolist()
        start_cols = template_data.iloc[8].values.tolist()
        picklist_files = template_data.iloc[7].values.tolist()
        result_cols = template_data.iloc[6].values.tolist()

        # Process each configured column mapping
        for target_col, start_col, file_name, result_col in zip(
                target_columns, start_cols, picklist_files, result_cols):

            # Skip if any configuration element is missing
            if (pd.isna(target_col)) or (pd.isna(start_col)) or (pd.isna(file_name)) or (pd.isna(result_col)):
                continue

            # Skip if target column doesn't exist in input data
            if target_col not in data.columns:
                print(f"Target column '{target_col}' not found in data. Skipping.")
                continue

            # Standardize picklist filename with .xlsx extension
            file_name = file_name.strip()
            if not file_name.lower().endswith('.xlsx'):
                file_name += '.xlsx'

            # Construct full path to picklist file
            picklist_path = os.path.join('../source_extracts/', file_name)

            # Verify picklist file exists
            if not os.path.exists(picklist_path):
                print(f"Picklist file not found: {picklist_path}")
                continue

            try:
                # Load picklist data
                picklist_df = pd.read_excel(picklist_path, dtype=str)

                # Validate required columns exist in picklist
                if start_col not in picklist_df.columns or result_col not in picklist_df.columns:
                    print(f"Picklist file missing required columns: '{start_col}' or '{result_col}'")
                    continue

                # Create mapping dictionary from picklist data
                picklist_map = {
                    str(k).strip(): str(v).strip()
                    for k, v in zip(picklist_df[start_col], picklist_df[result_col])
                }

                # Capture original values for comparison
                original_values = data[target_col].astype(str).str.strip().unique()

                # Apply replacements while preserving unmatched values
                data[target_col] = data[target_col].astype(str).str.strip().map(
                    lambda x: picklist_map.get(x, x)
                )

                # Identify changed values for logging
                new_values = data[target_col].astype(str).str.strip().unique()
                changed_pairs = [
                    (orig, new)
                    for orig in original_values
                    for new in new_values
                    if orig != new and orig in picklist_map
                ]

                # Log processing details
                print(f"\nProcessed picklist for column: {target_col}")
                print(f"Picklist file: {file_name}")
                print(f"Mapping: {start_col} -> {result_col}")
                print(f"Sample picklist entries (first 3):")
                for k, v in list(picklist_map.items())[:3]:
                    print(f"  '{k}' -> '{v}'")

                # Log changes or reasons for no changes
                if changed_pairs:
                    print(f"Sample changes (showing first 5):")
                    for orig, new in changed_pairs[:5]:
                        print(f"  '{orig}' -> '{new}'")
                    if len(changed_pairs) > 5:
                        print(f"  (plus {len(changed_pairs)-5} more changes)")
                else:
                    print("No values were changed - possible reasons:")
                    print(f"- Values in '{target_col}' don't match '{start_col}' in picklist")
                    print(f"- Example picklist keys: {list(picklist_map.keys())[:5]}")
                    print(f"- Example data values: {original_values[:5]}")
                    print(f"- Check for whitespace or case differences")

            except Exception as e:
                print(f"Error processing picklist for column {target_col}: {str(e)}")

        return data

    except Exception as e:
        print(f"Error in picklist processing: {str(e)}")
        return data


def read_template(template_path):
    """
    Read template configuration including column names, table names, and column mappings.

    Args:
        template_path: Path to Excel template file

    Returns:
        tuple: (template_column_names, table_names, column_names)
    """
    try:
        template_data = pd.read_excel(template_path, dtype=str)
        template_column_name = template_data.columns
        table_names = template_data.iloc[1].values.tolist()  # Row 2 contains table names
        column_names = template_data.iloc[3].values.tolist()  # Row 4 contains column mappings
        return template_column_name, table_names, column_names
    except Exception as e:
        print(f"Error reading template file: {e}")
        return None, None, None


def get_default_values(template_path):
    """
    Extract default values from row 6 of the template.

    Args:
        template_path: Path to Excel template file

    Returns:
        dict: Dictionary mapping column names to default values
    """
    try:
        df = pd.read_excel(template_path, dtype=str)
        if df.shape[0] < 4:
            print("Template file does not contain a row 6 for default values. Skipping default value assignment.")
            return {}

        # Row 6 (index 4) contains default values
        defaults = df.iloc[4].to_dict()
        print("Default values from row 6:")
        for col, default in defaults.items():
            print(f"  Column '{col}': Default value '{default}'")
        return defaults
    except Exception as e:
        print(f"Error reading default values from template: {e}")
        return {}



def apply_filter_on_target_file(target_file_path, template_path):
    """
    Apply filter and deduplication to target output file based on template configuration.

    Args:
        target_file_path: Path to generated output file
        template_path: Path to template file containing filter configuration
    """
    try:
        print(f"\nApplying filter on target file: {target_file_path} using template: {template_path}")

        # Read template configuration
        df_template = pd.read_excel(template_path, dtype=str)

        # Extract filter specification from row 6 if available
        if df_template.shape[0] <= 5:
            print("Template file does not have row 6 for filter specification. Skipping filtering step.")
            filter_cell = None
        else:
            filter_cell = df_template.iloc[5, 0]
            print(f"Filter cell raw value (target filter): '{filter_cell}'")

        # Load target output data
        target_df = pd.read_excel(target_file_path, dtype=str)

        # Process filter if specified
        if filter_cell and pd.notna(filter_cell) and filter_cell.strip():
            parts = filter_cell.split(":", 1)
            if len(parts) == 2:
                col_name = parts[0].strip()
                filter_value = parts[1].strip()
                print(f"Filter for target file - Column: '{col_name}', Value to keep: '{filter_value}'")

                if col_name in target_df.columns:
                    target_df[col_name] = target_df[col_name].astype(str).str.strip()
                    original_count = len(target_df)

                    # Apply appropriate filter comparison
                    try:
                        filter_value_float = float(filter_value)
                        numeric_values = pd.to_numeric(target_df[col_name], errors='coerce')
                        mask = numeric_values == filter_value_float
                        target_df = target_df[mask]
                        target_df[col_name] = "";
                        print("Numeric comparison applied on target file.")
                    except ValueError:
                        target_df = target_df[target_df[col_name] == filter_value]
                        target_df[col_name] = "";
                        print("String comparison applied on target file.")

                    # Log filtering results
                    filtered_count = len(target_df)
                    print(f"After filtering target file, kept {filtered_count} rows (from {original_count}).")
                else:
                    print(f"Column '{col_name}' not found in target file columns. Skipping filtering.")
            else:
                print(f"Filter specification invalid: '{filter_cell}'. Expected format 'columnname:value'")
        else:
            print("No valid filter specified in template. Proceeding with duplicate removal and row addition.")

        # Remove duplicate rows
        rows_before_dup = len(target_df)
        target_df = target_df.drop_duplicates()
        rows_after_dup = len(target_df)
        print(f"Removed {rows_before_dup - rows_after_dup} duplicate rows. Final data shape: {target_df.shape}")

        # Save processed data
        target_df.to_excel(target_file_path, index=False)
        print(f"Processed target file saved: {target_file_path}")

        # Add second row from template to output
        # add_second_row_from_template_to_output(target_file_path, template_path)

    except Exception as e:
        print(f"Error applying filter on target file: {e}")


def get_table_columns(table_names, column_names):
    """
    Create mapping of table names to their associated columns.

    Args:
        table_names: List of table names
        column_names: List of corresponding column names

    Returns:
        dict: Dictionary mapping tables to their columns
    """
    table_columns = {}
    for table, column in zip(table_names, column_names):
        if table and column and column != 'NAN':
            table_columns.setdefault(table, []).append(column)
    return table_columns


def clean_columns(table_columns):
    """
    Clean column specifications by handling special cases:
    - Float values converted to strings
    - Split columns marked with '/'
    - Remove 'NAN' values

    Args:
        table_columns: Dictionary of tables and their columns

    Returns:
        dict: Cleaned column mapping
    """
    for table, columns in table_columns.items():
        new_columns = []
        for column in columns:
            if isinstance(column, float):
                new_columns.append(str(column))
            elif '/' in column:
                new_columns.extend(col for col in column.split('/') if col != 'AUS')
            elif column != 'nan':
                new_columns.append(column)
        table_columns[table] = new_columns
    return table_columns


def merge_tables(table_columns, column_name_mapping, source_folder='../source_extracts/'):
    """
    Merge data from multiple tables based on specified columns.

    Args:
        table_columns: Dictionary mapping tables to their required columns
        column_name_mapping: merge rule for complex files
        source_folder: Path to folder containing source Excel files

    Returns:
        DataFrame: Merged data from all specified tables
    """
    combined_data = None
    print("Starting merge_tables function")
    print(f"Source folder: {source_folder}")
    print(f"Column name mapping: {column_name_mapping}")

    if column_name_mapping == 'nan':
        print("Simple merge case (column_name_mapping is 'nan')")
        for table_name, cols in table_columns.items():
            file_path = os.path.join(source_folder, f"{table_name}.xlsx")
            print(f"Looking for file: {file_path}")
            if os.path.exists(file_path):
                try:
                    print(f"Reading table: {file_path}")
                    table_data = pd.read_excel(file_path, dtype=str)

                    required_cols = [col for col in cols if col != 'nan']
                    print(f"Initial required columns: {required_cols}")

                    if column_name_mapping != 'nan':
                        required_cols.append(column_name_mapping)
                    required_cols = list(set(required_cols))
                    print(f"Final required columns for table {table_name}: {required_cols}")

                    table_data = table_data[required_cols]
                    print(f"Data shape for {table_name}: {table_data.shape}")

                    if combined_data is None:
                        print(f"Setting initial combined data from {table_name}")
                        combined_data = table_data
                    else:
                        print(f"Merging {table_name} with existing combined data on '{column_name_mapping}'")
                        combined_data = pd.merge(combined_data, table_data, on=column_name_mapping)
                        print(f"Combined data shape after merging {table_name}: {combined_data.shape}")

                except Exception as e:
                    print(f"Error processing table {file_path}: {e}")
            else:
                print(f"Table file {file_path} not found.")
    else:
        print("Complex merge case with column mapping")
        words_list, brackets_list = extract_info(column_name_mapping)
        print(f"Tables in order: {words_list}")
        print(f"Mapping keys (brackets): {brackets_list}")

        table_columns = {key: [val for val in values if val.lower() != 'nan'] for key, values in table_columns.items()}
        count = 0
        combined = 0
        mapping = 0
        maplist = ['', '']

        for table_name in words_list:
            file_path = os.path.join(source_folder, f"{table_name}.xlsx")
            print(f"Looking for file: {file_path}")
            if os.path.exists(file_path):
                try:
                    print(f"Reading table: {file_path}")
                    table_data = pd.read_excel(file_path, dtype=str)

                    cols = table_columns.get(table_name, [])
                    print(f"Initial columns for {table_name}: {cols}")

                    required_cols = [col for col in cols if col != 'nan']

                    for key in brackets_list:
                        if key in table_data.columns:
                            required_cols.append(key)

                    required_cols = list(set(required_cols))
                    print(f"Final required columns for {table_name}: {required_cols}")

                    table_data = table_data[required_cols]
                    print(f"Data shape for {table_name}: {table_data.shape}")

                    if combined_data is None:
                        print(f"Setting initial combined data from {table_name}")
                        combined_data = table_data
                    else:
                        combined = 1
                        print(f"Merging {table_name} using keys: {brackets_list[count]} (left) and {brackets_list[count+1]} (right)")
                        combined_data = pd.merge(combined_data, table_data, left_on=brackets_list[count], right_on=brackets_list[count+1])
                        count += 2
                        print(f"Combined data shape after merging {table_name}: {combined_data.shape}")

                except Exception as e:
                    print(f"Error processing table {file_path}: {e}")
            else:
                print(f"Table file {file_path} not found.")

    print("Merge process completed.")
    print(combined_data)
    return combined_data



def read_templates(folder):
    """
    Discover all Excel template files in specified folder.

    Args:
        folder: Path to folder containing template files

    Returns:
        dict: Dictionary mapping template filenames to their full paths
    """
    templates = {}
    for file in os.listdir(folder):
        if file.endswith('.xlsx'):
            filepath = os.path.join(folder, file)
            templates[file] = filepath
    return templates


def fill_template(template_path, combined_data, mapping):
    """
    Populate template structure with merged data according to column mappings.

    Args:
        template_path: Path to template file
        combined_data: Merged DataFrame containing source data
        mapping: Dictionary mapping template columns to source columns
    """
    try:
        # Load template structure
        df = pd.read_excel(template_path, dtype=str)
        print(f"\nReading template: {template_path}")
        print(f"Mapping: {mapping}")

        # Create output DataFrame with template columns
        new_df = pd.DataFrame(columns=df.columns)

        # Populate each template column according to mapping
        for template_col, mapped_col in mapping.items():
            if isinstance(mapped_col, float):
                mapped_col = str(mapped_col)

            # Handle concatenated columns (marked with '/')
            if '/' in mapped_col:
                columns_to_concat = mapped_col.split('/')
                concatenated_values = []
                for _, row in combined_data.iterrows():
                    concat_value = '/'.join(['AUS' if col == 'AUS'
                                             else str(row[col]) if col in row.index else ''
                                             for col in columns_to_concat])
                    concatenated_values.append(concat_value)
                new_df[template_col] = concatenated_values

            # Direct column mapping
            elif mapped_col in combined_data.columns:
                new_df[template_col] = combined_data[mapped_col]
            else:
                new_df[template_col] = None

        # Apply default values from template
        defaults = get_default_values(template_path)
        for col in new_df.columns:
            if col in defaults and pd.notna(defaults[col]):
                missing_before = new_df[col].isna().sum()
                new_df[col] = new_df[col].fillna(defaults[col])
                missing_after = new_df[col].isna().sum()
                if missing_before > missing_after:
                    print(f"Default value '{defaults[col]}' added to column '{col}' for {missing_before - missing_after} missing entries.")
                else:
                    print(f"No missing values in column '{col}'; default value not applied.")
            else:
                print(f"No default value specified for column '{col}'.")

        # Process picklist replacements
        new_df = process_picklist_replacements(new_df, template_path)

        # Save output file
        output_file_path = os.path.join("../target", f"{os.path.basename(template_path).split('.')[0]}_output.xlsx")
        new_df.to_excel(output_file_path, index=False)
        print(f"Template filled and saved to {output_file_path}")

        # Apply post-processing filters and transformations
        apply_filter_on_target_file(output_file_path, template_path)

    except Exception as e:
        print(f"Error filling template {template_path}: {e}")


def create_mapping(template_column_name, table_names, column_names):
    """
    Create column mapping dictionary from template configuration.

    Args:
        template_column_name: List of template column names
        table_names: List of source table names
        column_names: List of source column names

    Returns:
        dict: Mapping of template columns to source columns
    """
    mapping = {}
    for template_col, table_name, column_name in zip(template_column_name, table_names, column_names):
        if pd.notna(template_col) and pd.notna(column_name):
            mapping[template_col] = column_name
    return mapping


def add_second_row_from_template_to_output(output_file_path, template_path):
    """
    Insert second row from template into output file at position 1.

    Args:
        output_file_path: Path to generated output file
        template_path: Path to template file
    """
    try:
        # Load template and output data
        template_data = pd.read_excel(template_path, dtype=str)
        output_data = pd.read_excel(output_file_path, dtype=str)

        # Extract row to insert (first row from template)
        row_to_insert = template_data.iloc[0]

        # Prepare new row with matching columns
        new_row = pd.DataFrame([row_to_insert])[output_data.columns]

        # Insert new row at position 1
        output_data = pd.concat([output_data.iloc[:0], new_row, output_data.iloc[0:]], ignore_index=True)

        # Save modified output
        output_data.to_excel(output_file_path, index=False)
        print(f"New row inserted at position 1 in {output_file_path}")
    except Exception as e:
        print(f"Error adding second row from template: {e}")


def process_all_templates(template_folder):
    """
    Main processing function that handles all templates in specified folder.

    Args:
        template_folder: Path to folder containing template files
    """
    # Discover all template files
    templates = read_templates(template_folder)

    # Process each template
    for template_name, template_path in templates.items():
        print(f"\nProcessing template: {template_path}")

        # Read template configuration
        template_column_name, table_names, column_names = read_template(template_path)

        if template_column_name is not None and not template_column_name.empty and table_names and column_names:
            print(f"Template column names: {template_column_name}")
            print(f"Table names: {table_names}")
            print(f"Column names: {column_names}")

            # Prepare table-column mappings
            table_columns = get_table_columns(table_names, column_names)
            table_columns = clean_columns(table_columns)

            # Merge data from all source tables
            sheet_data = pd.read_excel(template_path, dtype=str)
            # print(sheet_data)
            column_name_mapping = sheet_data.iloc[9, 0] if sheet_data.shape[0] > 8 and pd.notna(sheet_data.iloc[9, 0]) else "nan"
            print("column name mapping: ", column_name_mapping)
            combined_data = merge_tables(table_columns, column_name_mapping)

            if combined_data is not None:
                print(f"Combined data columns: {combined_data.columns}")

                # Create column mappings and fill template
                mapping = create_mapping(template_column_name, table_names, column_names)
                fill_template(template_path, combined_data, mapping)
            else:
                print("No combined data to fill the template.")
        else:
            print("Failed to read template details.")


if __name__ == "__main__":
    # Entry point - process all templates in ../template/ folder
    process_all_templates('../template/')