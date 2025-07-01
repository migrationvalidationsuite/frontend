import pandas as pd

# Read the Excel file
file_path = 'EmailSource.xlsx'
df = pd.read_excel(file_path)

# Duplicate rows with multiple numbers in the 'Pers.No.' column
df['Pers.No.'] = df['Pers.No.'].astype(str).str.split(';')
df = df.explode('Pers.No.', ignore_index=True)

# Display the modified DataFrame
print(df)

# Save the modified DataFrame to a new Excel file
df.to_excel('Modified_EmailSource.xlsx', index=False)
