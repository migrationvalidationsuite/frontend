import pandas as pd
import os

# Get the absolute path of the current script file
code_folder = os.path.dirname(os.path.abspath(__file__))  # e.g., a/b/c/d

# Get the parent directory of the current script folder
parent_folder = os.path.dirname(code_folder)  # e.g., a/b/c

# Construct path to wagetypemapping file located in 'source_extracts' folder
wage_mapping_file = os.path.join(parent_folder, 'source_extracts', 'wagetypemapping.xlsx')  # e.g., a/b/c/source_extracts/wagetypemapping.xlsx

# Construct path to the target output Excel file
target_file = os.path.join(parent_folder, 'target', 'T558C_output.xlsx')  # e.g., a/b/c/target/T558C_output.xlsx

# Read the wagetypemapping Excel file and keep only 'legacy' and 'ecp' columns as strings
wage_mapping_df = pd.read_excel(wage_mapping_file)
wage_mapping_df = wage_mapping_df[['legacy', 'ecp']].astype(str)

# Read the target output Excel file into a DataFrame
target_df = pd.read_excel(target_file)

# Ensure 'Wage Type in ECP' is treated as a string for consistent mapping
target_df['Wage Type in ECP'] = target_df['Wage Type in ECP'].astype(str)

# --- The following code is commented out but was originally used to map legacy wage types to ECP wage types ---
# Iterate through each row in the target DataFrame and update wage type using the mapping
# for index, row in target_df.iterrows():
#     wage_type = row['Wage Type in ECP']
#
#     # Find matching row in the wage mapping DataFrame based on 'legacy' value
#     matched_row = wage_mapping_df[wage_mapping_df['legacy'] == wage_type]
#
#     if not matched_row.empty:
#         # Replace the 'Wage Type in ECP' with the mapped 'ecp' value
#         target_df.at[index, 'Wage Type in ECP'] = matched_row['ecp'].values[0]

# Group by relevant columns and aggregate the 'Amount' by summing values for duplicates
target_df = target_df.groupby(['Pers.No.', 'Seq.Nr', 'Wage Type in ECP', 'Date', 'Paygroup'], as_index=False)['Amount'].sum()

# Define the output file path to save the modified data
output_file = os.path.join(parent_folder, 'target', 'T558C_output.xlsx')

# Specify the desired column order for the final output
desired_columns = ['Pers.No.', 'Seq.Nr', 'Tabel Type', 'Cummulation Type', 'Tx.Key', 'Wage Type in ECP', 'Date', 'Rate', 'Number', 'Amount', 'Paygroup']

# Add any missing columns to the DataFrame with blank values
for col in desired_columns:
    if col not in target_df.columns:
        target_df[col] = ''

# Reorder the DataFrame columns to match the desired structure
target_df = target_df[desired_columns]

# Write the updated DataFrame to an Excel file
target_df.to_excel(output_file, index=False)

# Print a confirmation message with the output file path
print(f"File processed and saved as {output_file}")
