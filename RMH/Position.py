import pandas as pd
import os

# Function to read template file and extract column names and corresponding table names
def read_template(template_path):
    template_data = pd.read_excel(template_path)
    template_column_name = template_data.columns
    table_names = template_data.iloc[1].values.tolist()
    column_names = template_data.iloc[3].values.tolist() # change it to 2 for technical name
    return template_column_name, table_names, column_names

def merge_tables(table_names, column_names, column_name_mapping, source_folder='source'):
    # Create a dictionary to store table names and their corresponding columns
    table_columns = {}

    for table, column in zip(table_names, column_names):
        if table is not None and column is not None:
            if table in table_columns:
                table_columns[table].append(column)
            else:
                table_columns[table] = [column]

    for table, columns in table_columns.items():
        new_columns = []  # Store updated list of columns
        for column in columns:
            if isinstance(column, float):
                new_columns.append(str(column))  # Convert float to string
            elif '/' in column:
                new_columns.extend(column.split('/'))  # Split on '/' and extend the list
            else:
                new_columns.append(column)  # Add the column as is if no '/'
        table_columns[table] = new_columns

    print("table columns", table_columns)
    combined_data = None

    for table_name, cols in table_columns.items():
        file_path = os.path.join(source_folder, f"{table_name}.xlsx")
        if os.path.exists(file_path):
            table_data = pd.read_excel(file_path)
            print("reading table ", file_path)
            # Select only required columns and the common column
            required_cols = [col for col in cols if col is not None]
            if column_name_mapping != 'NAN':
                required_cols.append(column_name_mapping)
            else:
                print("column mapping common NAN")
            required_cols = list(set(required_cols))
            print("required_cols", required_cols)
            table_data = table_data[required_cols]
            if combined_data is None:
                combined_data = table_data
            else:
                combined_data = pd.merge(combined_data, table_data, on=column_name_mapping)

    return combined_data

# Read templates from the template folder
def read_templates(folder):
    templates = {}
    for file in os.listdir(folder):
        if file.endswith('.xlsx'):
            filepath = os.path.join(folder, file)
            templates[file.split('.')[0]] = filepath
    return templates

# Main function to process each template
def process_templates(template_folder):
    template_path = os.path.join(template_folder, "Position.xlsx")
    if os.path.exists(template_path):
        print("Processing template:", template_path)
        # Read the template and extract column names and table names
        template_column_name, table_names, column_names = read_template(template_path)
        print("template_column_name ", template_column_name)
        print("Table names ", table_names)
        print("Column names ", column_names)

        mapping = {
            'Cost Center': 'Cost Ctr',
            'Job Classification': 'NAN'
        }

        # Assuming you have a function merge_tables(table_names, column_names, third_param)
        # that merges tables with given parameters

        # Function to fill the third parameter based on template_path
        def fill_third_param(template_name):
            return mapping.get(template_name, 'NAN')

        third_param = fill_third_param('Company')
        print(third_param)

        # Merge tables based on the specified mapping
        combined_data = merge_tables(table_names, column_names, third_param) # !!!!!!!!

        # Fill the template with selected column values
        df = pd.read_excel(template_path)
        print("reading template ", template_path)
        print("combined data columns ", combined_data.columns)

        mapping = {}

        for template, column in zip(template_column_name, column_names):
            if template is not None and column is not None:
                mapping[template] = column

        print(mapping)

        print("Number of rows in combined data:", combined_data.shape[0])
        print("Number of columns in combined data:", combined_data.shape[1])

        new_df = pd.DataFrame(columns=df.columns)

        for template_col, mapped_col in mapping.items():
            if isinstance(mapped_col, float):
                # Convert mapped_col to string if it's a float
                mapped_col = str(mapped_col)
            if '/' in mapped_col:
                    # If mapped_col contains '/', split it and consider all resulting columns
                    columns_to_concat = mapped_col.split('/')
                    concatenated_values = []
                    for _, row in combined_data.iterrows():
                        concat_value = '/'.join([str(row[col]) for col in columns_to_concat if pd.notnull(row[col])])
                        concatenated_values.append(concat_value)
                    new_df[template_col] = concatenated_values
            elif mapped_col in combined_data.columns:
                # If mapped_col is a single column
                new_df[template_col] = combined_data[mapped_col]

        output_file_path = "target/" + os.path.basename(template_path).split(".")[0] + '_output.xlsx'
        new_df.to_excel(output_file_path, index=False)
    else:
        print("Template file 'Position.xlsx' not found in the specified folder.")

# Process the templates
process_templates('template')

import pandas as pd

# Read the Excel file
df = pd.read_excel("source/PA0001.xlsx")

# Create positionFrequency dictionary
positionFrequency = {}
for index, row in df.iterrows():
    position = row['Position']
    if position not in positionFrequency:
        positionFrequency[position] = 1
    else:
        positionFrequency[position] += 1

# Create positionPerson dictionary
positionPerson = {}
for index, row in df.iterrows():
    position = row['Position']
    if position not in positionPerson:
        positionPerson[position] = row['Pers.No.']

# Write dictionaries to files
with open("positionFrequency.txt", "w") as f:
    for key, value in positionFrequency.items():
        f.write(f"{key}: {value}\n")

with open("positionPerson.txt", "w") as f:
    for key, value in positionPerson.items():
        f.write(f"{key}: {value}\n")

print("Dictionaries created and saved as positionFrequency.txt and positionPerson.txt")

import pandas as pd

# Read positionPerson.txt to create a dictionary mapping position codes to Pers.No.
positionPerson = {}
with open("positionPerson.txt", "r") as f:
    for line in f:
        position, pers_no = map(int, line.strip().split(": "))
        positionPerson[position] = pers_no

# Read source/PA0001.xlsx to create a dictionary mapping Pers.No. to cost center
source_df = pd.read_excel("source/PA0001.xlsx")
source_dict = dict(zip(source_df['Pers.No.'].astype(int), source_df['poscost']))
source_dictloc = dict(zip(source_df['Pers.No.'].astype(int), source_df['posloc']))

# Read target/Position_output.xlsx
output_df = pd.read_excel("target/Position_output.xlsx")

# Batch processing
for index, batch_df in output_df.groupby(output_df.index // 1000):
    batch_df_codes = batch_df['code'].tolist()
    for code in batch_df_codes:
        if code in positionPerson:
            pers_no = positionPerson[code]
            if pers_no in source_dict:
                cost_center = source_dict[pers_no]
                output_df.loc[output_df['code'] == code, 'costCenter.externalCode'] = cost_center
            if pers_no in source_dictloc:
               cost_center = source_dictloc[pers_no]
               output_df.loc[output_df['code'] == code, 'location.externalCode'] = cost_center
#         else:
#             print(f"No code, person number combination in file {code}")

# Write the updated dataframe back to target/Position_output.xlsx
output_df.to_excel("target/Position_output.xlsx", index=False)

print("File target/Position_output.xlsx updated successfully.")


import pandas as pd

# Read positionPerson.txt to create a dictionary mapping position codes to Pers.No.
positionPerson = {}
with open("positionPerson.txt", "r") as f:
    for line in f:
        position, pers_no = map(int, line.strip().split(": "))
        positionPerson[position] = pers_no

# Read source/PA0001.xlsx to create a dictionary mapping Pers.No. to cost center
source_df = pd.read_excel("source/PA0008.xlsx")
source_dict1 = dict(zip(source_df['Pers.No.'].astype(int), source_df['Ar.']))
source_dict2 = dict(zip(source_df['Pers.No.'].astype(int), source_df['PS group']))
source_dict3 = dict(zip(source_df['Pers.No.'].astype(int), source_df['Lv']))
source_dict4 = dict(zip(source_df['Pers.No.'].astype(int), source_df['Ty.']))

# Read target/Position_output.xlsx
output_df = pd.read_excel("target/Position_output.xlsx")

# Batch processing
for index, batch_df in output_df.groupby(output_df.index // 1000):
    batch_df_codes = batch_df['code'].tolist()
    for code in batch_df_codes:
        if code in positionPerson:
            pers_no = positionPerson[code]
            if pers_no in source_dict1:
                cost_center = "AUS/" + str(source_dict1[pers_no])
                output_df.loc[output_df['code'] == code, 'cust_payScaleArea.code'] = cost_center
            if pers_no in source_dict2 and pers_no in source_dict1 and pers_no in source_dict4:
                 cost_center = "AUS/" + str(source_dict1[pers_no]) + "/" + str(source_dict4[pers_no]) + "/" + str(source_dict2[pers_no])
                 output_df.loc[output_df['code'] == code, 'cust_payScaleGroup.code'] = cost_center
            if pers_no in source_dict2 and pers_no in source_dict1 and pers_no in source_dict4:
                if pers_no in source_dict3 and str(source_dict3[pers_no]) != "nan":
                    cost_center = "AUS/" + str(source_dict1[pers_no]) + "/" + str(source_dict4[pers_no]) + "/" + str(source_dict2[pers_no])  + "/" + str(source_dict3[pers_no])
                else:
                     cost_center = "AUS/" + str(source_dict1[pers_no]) + "/" + str(source_dict4[pers_no]) + "/" + str(source_dict2[pers_no])  + "/" + str(source_dict2[pers_no])
                output_df.loc[output_df['code'] == code, 'cust_payScaleLevel.code'] = cost_center
            if pers_no in source_dict2 and pers_no in source_dict1 and pers_no in source_dict4:
                  if pers_no in source_dict3 and str(source_dict3[pers_no]) != "nan":
                          cost_center = str(source_dict4[pers_no]) + "/" + str(source_dict2[pers_no])  + "/" + str(source_dict3[pers_no])
                  else:
                           cost_center = str(source_dict4[pers_no]) + "/" + str(source_dict2[pers_no])  + "/" + str(source_dict2[pers_no])
                  output_df.loc[output_df['code'] == code, 'jobCode.externalCode'] = cost_center
            if pers_no in source_dict4:
                 cost_center = "AUS/" + str(source_dict4[pers_no])
                 output_df.loc[output_df['code'] == code, 'cust_payScaleType.code'] = cost_center


#         else:
#             print(f"No code, person number combination in file {code}")

# Write the updated dataframe back to target/Position_output.xlsx
output_df.to_excel("target/Position_output.xlsx", index=False)

print("File target/Position_output.xlsx updated successfully.")

import pandas as pd

# Read the first Excel file and create the dictionary
file_path_1 = "source/PPR_HRP1001_OrgRelationships_O-S.xlsx"
df_dict = pd.read_excel(file_path_1)
pos_to_org = dict(zip(df_dict["ID rel.object"], df_dict["Object ID"]))

# Read the second Excel file
file_path_2 = "merged_hierarchy.xlsx"
df_hierarchy = pd.read_excel(file_path_2)
org_to_lev = dict(zip(df_hierarchy["Object ID"], df_hierarchy["Level"]))

import pandas as pd

# Read the Excel file
file_path = "target/Position_output.xlsx"
output_df = pd.read_excel(file_path)

# Loop through each row and extract/display specific columns
for index, row in output_df.iterrows():
    # Extract columns and print their values
    position = row['code']
    if position in pos_to_org.keys():  # Corrected line
        org = pos_to_org[position]
        if org in org_to_lev.keys():
            lev = org_to_lev[org]
#             print("found level ", lev)
            if lev == 2:
                output_df.loc[output_df['code'] == position, 'businessUnit.externalCode'] = org
            elif lev == 3:
                output_df.loc[output_df['code'] == position, 'division.externalCode'] = org
            elif lev == 4:
                output_df.loc[output_df['code'] == position, 'department.externalCode'] = org
            elif lev == 5:
                output_df.loc[output_df['code'] == position, 'cust_subteam.externalCode'] = org
            elif lev == 6:
                output_df.loc[output_df['code'] == position, 'cust_specialty.externalCode'] = org
            elif lev == 7:
                output_df.loc[output_df['code'] == position, 'cust_subspecialty.externalCode'] = org

output_df.to_excel("target/Position_output.xlsx", index=False)

file_path_1 = "target/PPR. Department-Division.xlsx"
df_dict = pd.read_excel(file_path_1)
chDep_parDiv = dict(zip(df_dict["externalCode"], df_dict["cust_toDivision.externalCode"]))

file_path_1 = "target/PPR. Division-Business Unit.xlsx"
df_dict = pd.read_excel(file_path_1)
chDiv_parBu = dict(zip(df_dict["externalCode"], df_dict["cust_toBusinessUnit.externalCode"]))

file_path_1 = "target/PPR. Sub Department-Department.xlsx"
df_dict = pd.read_excel(file_path_1)
chSubDep_parDep = dict(zip(df_dict["externalCode"], df_dict["cust_toDepartment.externalCode"]))

file_path_1 = "target/PPR. Specialty Sub-Department.xlsx"
df_dict = pd.read_excel(file_path_1)
chSpc_parSubDep = dict(zip(df_dict["externalCode"], df_dict["cust_SubDepartment.externalCode"]))

file_path_1 = "target/PPR. Sub Specialty-Specialty.xlsx"
df_dict = pd.read_excel(file_path_1)
chSubSpc_parSpc = dict(zip(df_dict["externalCode"], df_dict["cust_Specialty.externalCode"]))

import pandas as pd

# Read the Excel file
file_path = "target/Position_output.xlsx"
df = pd.read_excel(file_path)

# List of columns to check and fill
columns_to_fill = [
    'businessUnit.externalCode',
    'division.externalCode',
    'department.externalCode',
    'cust_subteam.externalCode',
    'cust_specialty.externalCode',
    'cust_subspecialty.externalCode'
]

# Iterate over each row and fill missing values with 'X'
for index, row in df.iterrows():
    for column in columns_to_fill:
        if pd.isnull(row[column]):
            df.at[index, column] = 'X'

# List of columns to check
columns_to_check = [
    'businessUnit.externalCode',
    'division.externalCode',
    'department.externalCode',
    'cust_subteam.externalCode',
    'cust_specialty.externalCode',
    'cust_subspecialty.externalCode'
]

# Iterate over each row
for index, row in df.iterrows():
    # Flag to keep track of whether a non-'X' value is found
    found_non_x = False

    # Iterate over columns until the first non-'X' value is found
    for column in columns_to_check:
        if row[column] != 'X':
            # print(f"First non-'X' value found at column: {column}, value: {row[column]}")
            if column == 'division.externalCode':
                df.at[index, 'businessUnit.externalCode'] = chDiv_parBu[row[column]]
            if column == 'department.externalCode':
                df.at[index, 'division.externalCode'] = chDep_parDiv[row[column]]
                df.at[index, 'businessUnit.externalCode'] = chDiv_parBu[chDep_parDiv[row[column]]]
            if column == 'cust_subteam.externalCode':
                df.at[index, 'department.externalCode'] = chSubDep_parDep[row[column]]
                df.at[index, 'division.externalCode'] = chDep_parDiv[chSubDep_parDep[row[column]]]
                df.at[index, 'businessUnit.externalCode'] = chDiv_parBu[chDep_parDiv[chSubDep_parDep[row[column]]]]
            if column == 'cust_specialty.externalCode':
                 df.at[index, 'cust_subteam.externalCode'] = chSpc_parSubDep[row[column]]
                 df.at[index, 'department.externalCode'] = chSubDep_parDep[chSpc_parSubDep[row[column]]]
                 df.at[index, 'division.externalCode'] = chDep_parDiv[chSubDep_parDep[chSpc_parSubDep[row[column]]]]
                 df.at[index, 'businessUnit.externalCode'] = chDiv_parBu[chDep_parDiv[chSubDep_parDep[chSpc_parSubDep[row[column]]]]]
            if column == 'cust_subspecialty.externalCode':
                 df.at[index, 'cust_specialty.externalCode'] = chSubSpc_parSpc[row[column]]
                 df.at[index, 'cust_subteam.externalCode'] = chSpc_parSubDep[chSubSpc_parSpc[row[column]]]
                 df.at[index, 'department.externalCode'] = chSubDep_parDep[chSpc_parSubDep[chSubSpc_parSpc[row[column]]]]
                 df.at[index, 'division.externalCode'] = chDep_parDiv[chSubDep_parDep[chSpc_parSubDep[chSubSpc_parSpc[row[column]]]]]
                 df.at[index, 'businessUnit.externalCode'] = chDiv_parBu[chDep_parDiv[chSubDep_parDep[chSpc_parSubDep[chSubSpc_parSpc[row[column]]]]]]
            found_non_x = True
            break

for column in columns_to_check:
    # Replace 'X' with None in the specified column
    df[column] = df[column].replace('X', None)


# Save the modified DataFrame back to the Excel file
df.to_excel("target/Position_output.xlsx", index=False)


# Read the Excel file
file_path = "target/Position_output.xlsx"
df = pd.read_excel(file_path)

# Iterate over each row and fill missing values with 'X'
for index, row in df.iterrows():
    for column in columns_to_fill:
        if pd.isnull(row[column]):
            df.at[index, column] = 'X'

# Read the Excel file
managerdf = pd.read_excel("source/PPR_HRP1001_OrgRelationships_O-SManager.xlsx")

# Convert columns to string
managerdf['ID rel.object'] = managerdf['ID rel.object'].astype(str)
managerdf['Object ID'] = managerdf['Object ID'].astype(str)

# Create dictionary from 'ID rel.object' to 'Object ID'
relation_dict = dict(zip(managerdf['Object ID'], managerdf['ID rel.object']))
# print(relation_dict)

# Iterate over each row
for index, row in df.iterrows():
    # Flag to keep track of whether a non-'X' value is found
    found_non_x = False

    # Iterate over columns until the first non-'X' value is found
    for column in columns_to_check:
        if str(row[column]) != 'X':
#             print(str(int(row[column])))
            # print(f"First non-'X' value found at column: {column}, value: {row[column]}")
            if str(int(row[column])) in relation_dict.keys():
                df.at[index, 'parentPosition.code'] = relation_dict[str(int(row[column]))]

for column in columns_to_check:
    # Replace 'X' with None in the specified column
    df[column] = df[column].replace('X', None)

df.to_excel("target/Position_output.xlsx", index=False)
