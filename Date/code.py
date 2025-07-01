import pandas as pd
from datetime import datetime

def convert_columns_to_date(file_name, columns):
    # Detect file extension
    if file_name.lower().endswith(('.xlsx', '.xls')):
        df = pd.read_excel(file_name)
    elif file_name.lower().endswith('.csv'):
        df = pd.read_csv(file_name)
    else:
        raise ValueError("Unsupported file format. Only Excel and CSV files are supported.")

    for col in columns:
        if col in df.columns:
            new_values = []
            for value in df[col]:
                try:
                    # Try parsing with dayfirst=True to handle "2017-02-01 00:00:00" as 1st Feb 2017
                    parsed = pd.to_datetime(str(value), dayfirst=True)
                    new_values.append(parsed.strftime('%d/%m/%Y'))
                except Exception:
                    new_values.append(value)  # Leave as-is if parsing fails
            df[col] = new_values
        else:
            print(f"Column '{col}' not found in the file.")

    # Save to a new file
    output_file = 'updated_' + file_name
    if output_file.endswith('.csv'):
        df.to_csv(output_file, index=False)
    else:
        df.to_excel(output_file, index=False)

    print(f"File saved as: {output_file}")

# Example usage
columns_to_convert = ['Date Text (dd.mm.yyyy)', 'Date Text (dd/mm/yyyy)', 'Date Format (dd/mm/yyyy)', 'Date (yyyy/mm/dd)']
file_name = 'random_dates.xlsx'
convert_columns_to_date(file_name, columns_to_convert)

columns_to_convert = ['HIREDATE']
file_name = 'BasicUser.xlsx'
convert_columns_to_date(file_name, columns_to_convert)
