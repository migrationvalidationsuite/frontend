import os
import pandas as pd

# Function to convert input Excel data into a wage type format
def convert_to_wagetype(input_file, output_file):
    # Load the input Excel file
    df = pd.read_excel(input_file, dtype=str)  # Load everything as strings to avoid type issues

    # Extract the headers from the first row and set them as column names
    df.columns = df.iloc[0].fillna("missing")  # Ensure column names are strings
    df = df[1:].reset_index(drop=True)  # Remove the header row from data

    # Rename the first column to Pers.No.
    df.rename(columns={df.columns[0]: "Pers.No."}, inplace=True)

    # Handle missing or unnamed columns by renaming them uniquely
    missing_count = 1
    new_columns = []
    for col in df.columns:
        if not isinstance(col, str) or col.strip() == "" or col.lower() == "missing":
            new_columns.append(f"missing{missing_count}")
            missing_count += 1
        else:
            new_columns.append(col.strip())
    df.columns = new_columns  # Set the new column names

    # Create a list to hold transformed data
    transformed_data = []

    # Loop through each row to pivot wide format into long format
    for index, row in df.iterrows():
        pers_no = str(row["Pers.No."].strip()) if pd.notna(row["Pers.No."]) else None  # Extract personal number
        for col in df.columns[1:]:  # Exclude the "Pers.No." column
            wage_type = str(col).strip()  # Ensure wage type is a string
            amount = row[col]
            try:
                amount = float(amount) if amount not in [None, "", "NaN"] else None  # Convert to float if valid
            except ValueError:
                amount = None  # If conversion fails, set to None

            # Only append rows with valid personal number, wage type, and amount
            if pers_no and wage_type and amount is not None:
                transformed_data.append([pers_no, wage_type, amount, 1])  # Add period as 1

    # Create the transformed DataFrame
    df_transformed = pd.DataFrame(transformed_data, columns=["Pers.No.", "Wage Type", "Amount", "period"])

    # Save the transformed data to an Excel file
    df_transformed.to_excel(output_file, index=False)

    # Inform the user that the file was saved successfully
    print(f"File successfully converted and saved as {output_file}")


# Example usage

# Get the path to the current script's folder (e.g., a/b/c/d)
code_folder = os.path.dirname(os.path.abspath(__file__))

# Go one level up to get the parent folder (e.g., a/b/c)
parent_folder = os.path.dirname(code_folder)

# Construct paths to various required folders relative to the parent
workbooks_folder = os.path.join(parent_folder, 'workbooks')  # a/b/c/workbooks
template_folder = os.path.join(parent_folder, 'template')  # a/b/c/template
source_folder = os.path.join(parent_folder, 'source_extracts')  # a/b/c/source_extracts
target_folder = os.path.join(parent_folder, 'target')  # a/b/c/target

# Define input and output Excel file paths
input_file = os.path.join(source_folder, "YTDdata.xlsx")  # Replace with actual input file
output_file = os.path.join(source_folder,"wagetype.xlsx")  # Output file location

# Call the function to perform conversion
convert_to_wagetype(input_file, output_file)
