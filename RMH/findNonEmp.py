import pandas as pd

# Read the Excel file
df = pd.read_excel('source/PA0001.xlsx')

# Convert 'PositionName' column to strings
df['PositionName'] = df['PositionName'].astype(str)

# Function to check if 'volunteer' or 'honorary' is present in the position
def get_label(position):
    position_lower = position.lower()
    if 'volunteer' in position_lower:
        return 'volunteer'
    elif 'honorary' in position_lower or 'honarary' in position_lower or 'hon' in position_lower:
        return 'honorary'
    else:
        return 'unknown'

# Add 'Label' column based on the presence of 'volunteer' or 'honorary'
df['Label'] = df['PositionName'].apply(get_label)

# Filter rows where 'Label' is 'volunteer' or 'honorary'
non_employees = df[df['Label'].isin(['volunteer', 'honorary'])]

# Select relevant columns
result_df = non_employees[['Pers.No.', 'Label', 'PositionName']]

# Write the result to a new Excel file
result_df.to_excel('source/nonEmployees.xlsx', index=False)

print("Non-employees' Pers.No., Labels, and PositionNames written to nonEmployees.xlsx")
