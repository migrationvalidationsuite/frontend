# import pandas as pd

# # Read the Excel file
# df = pd.read_excel("post_processed_target/JobInfoImportTemplate_theroyalmeD.xlsx")

# # Remove rows where column 'pay-group' is 'NM'
# df = df[df['pay-group'] != 'NM']

# # Remove duplicate rows
# df = df.drop_duplicates()

# print("file dimenstions ",df.shape[0], df.shape[1])

# # Find duplicates in the 'user-id' column
# duplicates = df[df.duplicated(['user-id'], keep=False)]['user-id'].tolist()
# duplicates = list(set(duplicates))

# # Print the list of user-id column values which have duplicates
# print("number of user id duplicates", len(duplicates))

# import pandas as pd

# # Read the Excel file
# df = pd.read_excel("post_processed_target/JobInfoImportTemplate_theroyalmeD.xlsx")

# # Remove rows where column 'pay-group' is 'NM'
# df = df[df['pay-group'] != 'NM']

# # Remove duplicate rows
# df = df.drop_duplicates()

# # Find duplicates in the 'user-id' column
# duplicate_users = df[df.duplicated(['user-id'], keep=False)]

# # Create a dictionary to store the differences
# differences = {}

# # Iterate over each duplicate user ID
# for user_id in duplicate_users['user-id'].unique():
#     # Select rows with the current user ID
#     user_rows = duplicate_users[duplicate_users['user-id'] == user_id]
    
#     # Drop 'user-id' column for comparison
#     user_rows = user_rows.drop(columns=['user-id'])
    
#     # Find columns with different values
#     different_columns = user_rows.columns[user_rows.nunique() > 1]
    
#     # Store the different columns in the dictionary
#     differences[user_id] = different_columns.tolist()

# # Save the differences to a text file
# with open('differences.txt', 'w') as f:
#     for user_id, columns in differences.items():
#         f.write(f"User ID: {user_id}\n")
#         f.write("Different Columns:\n")
#         for column in columns:
#             f.write(f"- {column}\n")
#         f.write("\n")

import pandas as pd
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")

# Define file paths
file_paths = {
    "PA0001": "source/UserOrganisation.xlsx",
    "PA0007": "source/PA0007.xlsx",
    "PA0008": "source/PA0008.xlsx",
    "pay" : "source/Paypoint.xlsx"
}

# Define columns to read for each file
columns_to_read = {
    "PA0001": ["Personnel No.", "Start Date", "EE group", "EE subgroup", "Payroll area",
               "Position", "Quota group", "Location Code", "poscost", "posloc" , "Payroll admin.", "Pers.admin.", "Time admin.", "Time ContrType", "Org. Unit", 'End Date'],
    "PA0007": ["Personnel No.",  "Start Date", "WS rule", "Workdays", "Weekly work hrs", 'End Date'],
    "PA0008": ["Personnel No.", "Start Date", "P.scale type", "PS Area", "Pay Scale Group", "PS level", 'End Date'],
    "pay" : ["Personnel No.", "Start Date", 'End Date', 'paypoint']
}

import pandas as pd

dfs = {}

for key, path in file_paths.items():
    df = pd.read_excel(path, usecols=columns_to_read[key])
    dfs[key] = df
    dfs[key]["Start Date"] = pd.to_datetime(dfs[key]["Start Date"], format='%d.%m.%Y', errors='coerce')
    dfs[key]["End Date"] = pd.to_datetime(dfs[key]["End Date"], format='%d.%m.%Y', errors='coerce')
    max_possible_date = pd.Timestamp.max
    dfs[key]["End Date"].fillna(max_possible_date, inplace=True)



# Example of accessing dataframes:
# dfs["PA0001"] will contain data from UserOrganisation.xlsx with only specified columns
# dfs["PA0007"] will contain data from PA0007.xlsx with only specified columns
# dfs["PA0008"] will contain data from PA0008.xlsx with only specified columns

# You can access each dataframe using dfs["PA0001"], dfs["PA0007"], and dfs["PA0008"]

file_path = "source/Active.xlsx"

# Read the Excel file and select the 'Pers.No.' column
df = pd.read_excel(file_path, usecols=['Personnel No.'])

# Get unique values from the 'Pers.No.' column
all_employees = df['Personnel No.'].unique().tolist()
print("length of all employees", len(all_employees))

# Define column names
columns = ['Personnel No.', 'Start Date', 'EE group', 'EE subgroup',
           'Position', 'Quota group', 'Location Code', 'poscost', 
           'posloc', 'WS rule', 'Workdays', 'P.scale type', 'PS Area', 'Pay Scale Group', 'PS level', "Payroll admin.", "Pers.admin.", "Time admin.", "Time ContrType", "Weekly work hrs", "Org. Unit", 'paypoint']

# Create empty DataFrame with specified columns
new_df = pd.DataFrame(columns=columns)
# new_df['Pers.No.'] = all_employees
# new_df['Start Date'] = pd.to_datetime("17/6/2024", format='%d/%m/%Y')

count = 0
new_rows_df = pd.DataFrame(columns=["Personnel No.", "Start Date"])
for pers_no in all_employees:
    filtered_df = dfs["PA0001"][dfs["PA0001"]["Personnel No."] == pers_no]

    count += 1

    # print(pers_no, "          ", count, " out of total ", len(all_employees), " for 0001")
    
    # Now 'filtered_df' contains rows where 'Pers.No.' matches the value from 'new_df'
    if len(filtered_df) > 1:
        prev_row = None
        for index, row in filtered_df.iterrows():
            rowcopy = row.copy() 
            if prev_row is not None and not prev_row.drop(["Start Date", "End Date"]).equals(rowcopy.drop(["Start Date", "End Date"])):
                new_row = pd.DataFrame({"Personnel No.": [row["Personnel No."]], "Start Date": [row["Start Date"]]})
                new_rows_df = pd.concat([new_rows_df, new_row])
            prev_row = row

    if len(filtered_df) != 0:
            # Sort filtered_df based on Start Date from past to most recent
            filtered_df.sort_values(by='Start Date', ascending=True, inplace=True)
    
            # Convert the target date to datetime format
            target_date = datetime.strptime("17/6/2024", "%d/%m/%Y")
    
            # Convert the start date of the first row to datetime format
            first_start_date = filtered_df.iloc[0]["Start Date"]
    
            # Check if the start date is less than the target date
            if first_start_date < target_date:
                # If yes, use the target date
                new_start_date = target_date.strftime("%d/%m/%Y")
            else:
                # If not, use the start date of the first row
                new_start_date = filtered_df.iloc[0]["Start Date"]
    
            # Create a DataFrame with personnel number and the new start date
            new_row = pd.DataFrame({"Personnel No.": [filtered_df.iloc[0]["Personnel No."]], "Start Date": [new_start_date]})

            # Append the new row to new_rows_df
            new_rows_df = pd.concat([new_rows_df, new_row])

print("pa0001 ", count)
# Concatenate new_rows_df with new_df to add the new rows
new_df = pd.concat([new_df, new_rows_df])

# Reset index of the new DataFrame
new_df.reset_index(drop=True, inplace=True)

count= 0
new_rows_df = pd.DataFrame(columns=["Personnel No.", "Start Date"])
for pers_no in all_employees:
    filtered_df = dfs["PA0007"][dfs["PA0007"]["Personnel No."] == pers_no]

    count += 1

    # print(pers_no, "          ", count, " out of total ", len(all_employees), " for 0007")
    # Now 'filtered_df' contains rows where 'Pers.No.' matches the value from 'new_df'
        
    if len(filtered_df) > 1:
        prev_row = None
        for index, row in filtered_df.iterrows():
            rowcopy = row.copy() 
            if prev_row is not None and not prev_row.drop(["Start Date", "End Date"]).equals(rowcopy.drop(["Start Date", "End Date"])):
                new_row = pd.DataFrame({"Personnel No.": [row["Personnel No."]], "Start Date": [row["Start Date"]]})
                new_rows_df = pd.concat([new_rows_df, new_row])
            prev_row = row

    if len(filtered_df) != 0:
            # Sort filtered_df based on Start Date from past to most recent
            filtered_df.sort_values(by='Start Date', ascending=True, inplace=True)
    
            # Convert the target date to datetime format
            target_date = datetime.strptime("17/6/2024", "%d/%m/%Y")
    
            # Convert the start date of the first row to datetime format
            first_start_date = filtered_df.iloc[0]["Start Date"]
    
            # Check if the start date is less than the target date
            if first_start_date < target_date:
                # If yes, use the target date
                new_start_date = target_date.strftime("%d/%m/%Y")
            else:
                # If not, use the start date of the first row
                new_start_date = filtered_df.iloc[0]["Start Date"]
    
            # Create a DataFrame with personnel number and the new start date
            new_row = pd.DataFrame({"Personnel No.": [filtered_df.iloc[0]["Personnel No."]], "Start Date": [new_start_date]})

            # Append the new row to new_rows_df
            new_rows_df = pd.concat([new_rows_df, new_row])

print("pa0007 ", count)
# Concatenate new_rows_df with new_df to add the new rows
new_df = pd.concat([new_df, new_rows_df])

# Reset index of the new DataFrame
new_df.reset_index(drop=True, inplace=True)

new_rows_df = pd.DataFrame(columns=["Personnel No.", "Start Date"])

count = 0
for pers_no in all_employees:
    filtered_df = dfs["PA0008"][dfs["PA0008"]["Personnel No."] == pers_no]

    count += 1

    # print(pers_no, "          ", count, " out of total ", len(all_employees), " for file 0008")
    if pers_no == 62923:
        print("hey see this ", filtered_df)
        print("here 1")
        
    if len(filtered_df) > 1:
        prev_row = None
        for index, row in filtered_df.iterrows():
            rowcopy = row.copy() 
            if prev_row is not None and not prev_row.drop(["Start Date", "End Date"]).equals(rowcopy.drop(["Start Date", "End Date"])):
                new_row = pd.DataFrame({"Personnel No.": [row["Personnel No."]], "Start Date": [row["Start Date"]]})
                new_rows_df = pd.concat([new_rows_df, new_row])
            prev_row = row
        # print("here 3")
            
    if len(filtered_df) != 0:
            # Sort filtered_df based on Start Date from past to most recent
            filtered_df.sort_values(by='Start Date', ascending=True, inplace=True)
    
            # Convert the target date to datetime format
            target_date = datetime.strptime("17/6/2024", "%d/%m/%Y")
    
            # Convert the start date of the first row to datetime format
            first_start_date = filtered_df.iloc[0]["Start Date"]
    
            # Check if the start date is less than the target date
            if first_start_date < target_date:
                # If yes, use the target date
                new_start_date = target_date.strftime("%d/%m/%Y")
            else:
                # If not, use the start date of the first row
                new_start_date = filtered_df.iloc[0]["Start Date"]

            # print("here 4")
    
            # Create a DataFrame with personnel number and the new start date
            new_row = pd.DataFrame({"Personnel No.": [filtered_df.iloc[0]["Personnel No."]], "Start Date": [new_start_date]})

            # Append the new row to new_rows_df
            new_rows_df = pd.concat([new_rows_df, new_row])

            # print("here 5")

print("pa0008 ", count)
# Concatenate new_rows_df with new_df to add the new rows
new_df = pd.concat([new_df, new_rows_df])

# Reset index of the new DataFrame
new_df.reset_index(drop=True, inplace=True)

new_rows_df = pd.DataFrame(columns=["Personnel No.", "Start Date"])

count = 0
for pers_no in all_employees:
    filtered_df = dfs["pay"][dfs["pay"]["Personnel No."] == pers_no]

    count += 1

    # print(pers_no, "          ", count, " out of total ", len(all_employees))
    
    # Now 'filtered_df' contains rows where 'Pers.No.' matches the value from 'new_df'

    if len(filtered_df) > 1:
        prev_row = None
        for index, row in filtered_df.iterrows():
            rowcopy = row.copy() 
            if prev_row is not None and not prev_row.drop(["Start Date", "End Date"]).equals(rowcopy.drop(["Start Date", "End Date"])):
                new_row = pd.DataFrame({"Personnel No.": [row["Personnel No."]], "Start Date": [row["Start Date"]]})
                new_rows_df = pd.concat([new_rows_df, new_row])
            prev_row = row

    if len(filtered_df) > 0:
            # Sort filtered_df based on Start Date from past to most recent
            filtered_df.sort_values(by='Start Date', ascending=True, inplace=True)
    
            # Convert the target date to datetime format
            target_date = datetime.strptime("17/6/2024", "%d/%m/%Y")
    
            # Convert the start date of the first row to datetime format
            first_start_date = filtered_df.iloc[0]["Start Date"]
    
            # Check if the start date is less than the target date
            if first_start_date < target_date:
                # If yes, use the target date
                new_start_date = target_date.strftime("%d/%m/%Y")
            else:
                # If not, use the start date of the first row
                new_start_date = filtered_df.iloc[0]["Start Date"]
    
            # Create a DataFrame with personnel number and the new start date
            new_row = pd.DataFrame({"Personnel No.": [filtered_df.iloc[0]["Personnel No."]], "Start Date": [new_start_date]})

            # Append the new row to new_rows_df
            new_rows_df = pd.concat([new_rows_df, new_row])

print("pay ", count)
# Concatenate new_rows_df with new_df to add the new rows
new_df = pd.concat([new_df, new_rows_df])

# Reset index of the new DataFrame
new_df.reset_index(drop=True, inplace=True)


# Assuming new_df is your DataFrame containing the Pers.No and Start Date columns
# And dfs is a dictionary containing DataFrames with keys like "PA0001", "PA0002", etc.

# Convert dates to datetime format
new_df['Start Date'] = pd.to_datetime(new_df['Start Date'])
new_df.loc[new_df['Start Date'] < pd.Timestamp('2024-06-17'), 'Start Date'] = pd.Timestamp('2024-06-17')

# new_df = new_df.drop_duplicates(inplace=True)

import pandas as pd

# Convert dates to datetime format outside the loop
dfs["PA0001"]['Start Date'] = pd.to_datetime(dfs["PA0001"]['Start Date'])
# Assuming dfs is your DataFrame and "PA0001" is the column name
dfs["PA0001"]['End Date'] = pd.to_datetime(dfs["PA0001"]['End Date'], errors='coerce')

# Find rows with NaT (Not a Time) values, indicating conversion errors
error_indices = dfs["PA0001"]['End Date'].isna()

# Replace errors with the specified date '9/9/2259'
dfs["PA0001"]['End Date'][error_indices] = pd.to_datetime('2259-09-09')

# Loop through each row of new_df
for index, row in new_df.iterrows():
    pers_no = row['Personnel No.']
    start_date = row['Start Date']
    
    # Check if the Pers.No exists in dfs["PA0001"] and if the Start Date is within the range
    if "PA0001" in dfs and pers_no in dfs["PA0001"]["Personnel No."].values:
        pa_data = dfs["PA0001"]
        
        filtered_rows = pa_data[(pa_data["Personnel No."] == pers_no) & 
                                (pa_data["Start Date"] <= start_date) & 
                                (pa_data["End Date"] >= start_date)]
        
        # If there are matching rows, fill corresponding columns in new_df
        if not filtered_rows.empty:
            for col in filtered_rows.columns:
                if col != 'Personnel No.' and col != 'Start Date' and col != 'End Date':
                    new_df.at[index, col] = filtered_rows.iloc[0][col]

import pandas as pd

# Convert dates to datetime format outside the loop
dfs["PA0007"]['Start Date'] = pd.to_datetime(dfs["PA0007"]['Start Date'])
# Assuming dfs is your DataFrame and "PA0001" is the column name
dfs["PA0007"]['End Date'] = pd.to_datetime(dfs["PA0007"]['End Date'], errors='coerce')

# Find rows with NaT (Not a Time) values, indicating conversion errors
error_indices = dfs["PA0007"]['End Date'].isna()

# Replace errors with the specified date '9/9/2259'
dfs["PA0007"]['End Date'][error_indices] = pd.to_datetime('2259-09-09')

# Loop through each row of new_df
for index, row in new_df.iterrows():
    pers_no = row['Personnel No.']
    start_date = row['Start Date']
    
    # Check if the Pers.No exists in dfs["PA0001"] and if the Start Date is within the range
    if "PA0007" in dfs and pers_no in dfs["PA0007"]["Personnel No."].values:
        pa_data = dfs["PA0007"]
        
        filtered_rows = pa_data[(pa_data["Personnel No."] == pers_no) & 
                                (pa_data["Start Date"] <= start_date) & 
                                (pa_data["End Date"] >= start_date)]
        
        # If there are matching rows, fill corresponding columns in new_df
        if not filtered_rows.empty:
            for col in filtered_rows.columns:
                if col != 'Personnel No.' and col != 'Start Date' and col != 'End Date':
                    new_df.at[index, col] = filtered_rows.iloc[0][col]

import pandas as pd

# Convert dates to datetime format outside the loop
dfs["PA0008"]['Start Date'] = pd.to_datetime(dfs["PA0008"]['Start Date'])
# Assuming dfs is your DataFrame and "PA0001" is the column name
dfs["PA0008"]['End Date'] = pd.to_datetime(dfs["PA0008"]['End Date'], errors='coerce')

# Find rows with NaT (Not a Time) values, indicating conversion errors
error_indices = dfs["PA0008"]['End Date'].isna()

# Replace errors with the specified date '9/9/2259'
dfs["PA0008"]['End Date'][error_indices] = pd.to_datetime('2259-09-09')

# Loop through each row of new_df
for index, row in new_df.iterrows():
    pers_no = row['Personnel No.']
    start_date = row['Start Date']
    
    # Check if the Pers.No exists in dfs["PA0001"] and if the Start Date is within the range
    if "PA0008" in dfs and pers_no in dfs["PA0008"]["Personnel No."].values:
        pa_data = dfs["PA0008"]
        
        filtered_rows = pa_data[(pa_data["Personnel No."] == pers_no) & 
                                (pa_data["Start Date"] <= start_date) & 
                                (pa_data["End Date"] >= start_date)]
        
        # If there are matching rows, fill corresponding columns in new_df
        if not filtered_rows.empty:
            for col in filtered_rows.columns:
                if col != 'Personnel No.' and col != 'Start Date' and col != 'End Date':
                    new_df.at[index, col] = filtered_rows.iloc[0][col]

# Convert date columns to datetime if they are not already
new_df["Start Date"] = pd.to_datetime(new_df["Start Date"])

import pandas as pd

# Convert dates to datetime format outside the loop
dfs["pay"]['Start Date'] = pd.to_datetime(dfs["pay"]['Start Date'], errors='coerce')
# Assuming dfs is your DataFrame and "PA0001" is the column name
dfs["pay"]['End Date'] = pd.to_datetime(dfs["pay"]['End Date'], errors='coerce')
# Fill missing values with '2259-09-09'
dfs["pay"]['End Date'].fillna(pd.to_datetime('2259-09-09'), inplace=True)

print(dfs["pay"])

# Loop through each row of new_df
for index, row in new_df.iterrows():
    pers_no = row['Personnel No.']
    start_date = row['Start Date']
    
    # Check if the Pers.No exists in dfs["PA0001"] and if the Start Date is within the range
    if "pay" in dfs and pers_no in dfs["pay"]["Personnel No."].values:
        pa_data = dfs["pay"]
        
        filtered_rows = pa_data[(pa_data["Personnel No."] == pers_no) & 
                                (pa_data["Start Date"] <= start_date) & 
                                (pa_data["End Date"] >= start_date)]
        
        # If there are matching rows, fill corresponding columns in new_df
        if not filtered_rows.empty:
            for col in filtered_rows.columns:
                if col != 'Personnel No.' and col != 'Start Date' and col != 'End Date':
                    new_df.at[index, col] = filtered_rows.iloc[0][col]

# Convert date columns to datetime if they are not already
new_df["Start Date"] = pd.to_datetime(new_df["Start Date"])

# # Assuming 'Start Date' and 'End Date' are column names in your DataFrame
# # Replace them with the actual column names if different
# subset_cols = [col for col in new_df.columns if col not in ['Start Date', 'End Date']]

# # Keep the first occurrence of rows with the same values in all columns except 'Start Date' and 'End Date'
# new_df = new_df.drop_duplicates(subset=subset_cols, keep='first')

# # If you want to reset the index after dropping duplicates
# new_df = new_df.reset_index(drop=True)
new_df = new_df.drop_duplicates()
new_df.to_excel("source/jobhelp.xlsx", index=False)