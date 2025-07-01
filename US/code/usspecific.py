import pandas as pd
import os

# Define paths for necessary files
code_folder = os.path.dirname(os.path.abspath(__file__))  # Gets the current script's directory
parent_folder = os.path.dirname(code_folder)  # Moves one level up to the parent folder
wage_mapping_file = os.path.join(parent_folder, 'source_extracts', 'wagetypemapping.xlsx')  # Full path to wagetypemapping.xlsx
tax_details_file = os.path.join(parent_folder, 'source_extracts', 'taxdetails.xlsx')  # Full path to taxdetails.xlsx
target_file = os.path.join(parent_folder, 'target', 'T558C_US_output.xlsx')  # Full path to the target output file

# Read the wagetypemapping file and extract necessary columns
wage_mapping_df = pd.read_excel(wage_mapping_file)  # Load the wagetypemapping file into a DataFrame
wage_mapping_df = wage_mapping_df[['legacy', 'tax', 'ecp']].astype(str)  # Keep only needed columns and ensure all are strings

# Read the T5U8C file (assumed to be the target Excel)
target_df = pd.read_excel(target_file)  # Load the target Excel file into a DataFrame

# Ensure relevant columns are of the string type for accurate comparison
target_df['Wage Type'] = target_df['Wage Type'].astype(str)  # Convert Wage Type column to string
target_df['Personnel Number'] = target_df['Personnel Number'].astype(str)  # Convert Personnel Number column to string

# Iterate over rows in target_df and update based on wage type mapping
for index, row in target_df.iterrows():
    wage_type = row['Wage Type']

    # Find matching row in wage mapping
    matched_row = wage_mapping_df[wage_mapping_df['legacy'] == wage_type]
    if not matched_row.empty:
        # Update 'Wage Type' and 'Tax Authority' if a match is found
        target_df.at[index, 'Wage Type'] = matched_row['ecp'].values[0]
        target_df.at[index, 'Tax Authority'] = matched_row['tax'].values[0]

# Read the taxdetails file and ensure columns are strings for comparison
tax_details_df = pd.read_excel(tax_details_file, dtype={'Pers.No.': str, 'Deets': str})  # Load tax details and set column types

# Additional updates based on tax details conditions
for index, row in target_df.iterrows():
    pers_no = row['Personnel Number']
    wage_type = row['Wage Type']

    # Check for matching Pers.No. in tax details
    tax_row = tax_details_df[tax_details_df['Pers.No.'] == pers_no]
    if not tax_row.empty:
        deets = tax_row['Deets'].values[0]

        # Update Tax Authority based on Deets length and Wage Type
        if len(deets) == 2 and wage_type == "402":
            target_df.at[index, 'Tax Authority'] = deets
        elif len(deets) == 4 and wage_type == "403":
            target_df.at[index, 'Tax Authority'] = deets

# Save the modified DataFrame back to the target Excel file
output_file = os.path.join(parent_folder, 'target', 'T558C_US_output.xlsx')  # Define path to save output
target_df.to_excel(output_file, index=False)  # Save the DataFrame to Excel without index

print(f"File processed and saved as {output_file}")  # Inform user of completion
