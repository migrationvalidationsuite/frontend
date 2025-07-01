import os
import shutil
import stat
import pandas as pd
import glob

def on_rm_error(func,path,exc_info):
    os.chmod(path,stat.S_IWRITE)
    func(path)

# Get the absolute path of the current script's directory
code_folder = os.path.dirname(os.path.abspath(__file__))
# Get the parent directory of the script's location
parent_folder = os.path.dirname(code_folder)
# Define paths for workbooks and template folders relative to parent directory
workbooks_folder = os.path.join(parent_folder, 'workbooks')
template_folder = os.path.join(parent_folder, 'template')

# Clean up existing template folder and create a fresh one
if os.path.exists(template_folder):
    shutil.rmtree(template_folder, onerror = on_rm_error)
os.makedirs(template_folder)

# Find the most recently created Excel file in the workbooks folder
list_of_files = glob.glob(os.path.join(workbooks_folder, '*.xlsx'))
newest_file = max(list_of_files, key=os.path.getctime)

# Read the Excel file and extract all sheet names
excel_data = pd.ExcelFile(newest_file)
sheet_names = excel_data.sheet_names

# List of required columns to process each sheet
target_columns = [
    'Target column 1',
    'Target column 2',
    'Source Table',
    'Technical Name',
    'Extract Field Name',
    'Default Value',
    'Filter',
    'PicklistSource target',
    'PicklistSource file',
    'PicklistSource column',
    'Merge Rule'
]

# Process each sheet in the Excel file
for sheet_name in sheet_names:
    # Read current sheet into a DataFrame
    df = pd.read_excel(newest_file, sheet_name=sheet_name)

    # Only process sheets that contain all target columns
    if all(col in df.columns for col in target_columns):
        # Create a new DataFrame with values from target columns
        df_target = pd.DataFrame({
            col: df[col].values for col in target_columns
        })

        # Transpose the DataFrame (convert columns to rows)
        df_target = df_target.T.reset_index(drop=True)

        # Save the transformed data to a new Excel file
        output_path = os.path.join(template_folder, f'{sheet_name}.xlsx')
        df_target.to_excel(output_path, index=False, header=False)
        print(f'Sheet "{sheet_name}" processed: Target columns saved to {output_path}')
    else:
        print(f'Sheet "{sheet_name}" skipped: Not all target columns found')

print("Processing complete. Files saved in the template folder.")