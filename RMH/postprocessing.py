# import pandas as pd
#
# # Function to convert date to D/M/YYYY format
# def convert_to_date(value):
#     try:
#         return pd.to_datetime(value).strftime('%d/%m/%Y')
#     except (ValueError, TypeError):
#         return value
#
# # AHPRA
#
# # keep only employee records which have data
# # cust_AHPRARegistrationRequired.externalCode = "TRUE" for all
# # if cust_regNumber is empty then make it "NO DOCUMENT NUMBER"
#
# # Read the Excel file into a DataFrame
# file_path = 'target/AHPRA Registration_output.xlsx'
# output_file_path = 'post_processed_target/AHPRA Registration.xlsx'
# df = pd.read_excel(file_path)
#
# # Create a mask for rows where 'externalCode' is not empty, but all other columns are empty
# mask = (df['externalCode'].notna()) & (df[df.columns.difference(['externalCode'])].apply(lambda row: row.isna().all() or all(pd.isna(val) or val == '' for val in row), axis=1))
#
# # Filter the DataFrame based on the mask
# df = df[~mask]
#
# # Loop through all rows
# for index, row in df.iterrows():
#     # If cust_AHPRARegistrationRequired.externalCode is empty, set it to "TRUE"
#     if pd.isna(row['cust_AHPRARegistrationRequired.externalCode']):
#         df.at[index, 'cust_AHPRARegistrationRequired.externalCode'] = 'TRUE'
#
#     # If cust_regNumber is empty, set it to "NO DOCUMENT NUMBER"
#     if pd.isna(row['cust_regNumber']):
#         df.at[index, 'cust_regNumber'] = 'NO DOCUMENT NUMBER'
#
# # Convert 'effectiveStartDate' values to datetime format with the desired format
# df['effectiveStartDate'] = df['effectiveStartDate'].apply(convert_to_date)
#
# # Save the modified DataFrame back to the Excel file
# df.to_excel(output_file_path, index=False)
# print("AHPRA file updated successfully.")
#
# # JOB
#
# # Read the main DataFrame
# file_path_main = 'target/JobInfoImportTemplate_theroyalmeD_output.xlsx'
# df_main = pd.read_excel(file_path_main)
#
# # Read the Paypoint DataFrame
# file_path_paypoint = 'source/Paypoint.xlsx'
# df_paypoint = pd.read_excel(file_path_paypoint)
#
# # Read the Paypoint Picklist DataFrame
# file_path_picklist = 'source/paypointpicklist.xlsx'
# df_picklist = pd.read_excel(file_path_picklist)
#
# # Read the Picklist ACoral DataFrame
# file_path_acoral = 'source/picklistacoral.xlsx'
# df_acoral = pd.read_excel(file_path_acoral)
#
# # Iterate through rows and update 'custom-string21'
# for index, row in df_main.iterrows():
#     user_id = row['user-id']
#     if user_id in df_paypoint['user-id'].values:
#         location_code = df_paypoint.loc[df_paypoint['user-id'] == user_id, 'Location Code'].iloc[0]
#
#         # Check if location_code is in the picklist
#         if location_code in df_picklist['values.externalCode'].values:
#             # Get the corresponding default value from the picklist
#             default_value = df_picklist.loc[df_picklist['values.externalCode'] == location_code, 'values.label.defaultValue'].iloc[0]
#             df_main.at[index, 'custom-string21'] = default_value
#
# # Iterate through rows and update 'custom-string1'
# for index, row in df_main.iterrows():
#     custom_string1 = str(row['custom-string1']).strip()  # Convert to string and strip whitespace
#     # Convert the externalCode column in df_acoral to string and strip whitespace for comparison
#     external_codes = df_acoral['values.externalCode'].astype(str).str.strip().values
#
#     if custom_string1 in external_codes:
#         # Get the corresponding label from the ACoral picklist
#         label = df_acoral.loc[external_codes == custom_string1, 'values.label.defaultValue'].iloc[0]
#         df_main.at[index, 'custom-string1'] = label
#
# # Update 'custom-string1' based on specific conditions
# df_main.loc[df_main['custom-string1'].isin(['AV']), 'custom-string1'] = 'AV 79-AL4W'
# df_main.loc[df_main['custom-string1'].isin(['AU']), 'custom-string1'] = 'AU 76-AL4W'
#
# # Convert 'position' column to string if it's not already
# df_main['position'] = df_main['position'].astype(str)
#
# # Remove rows where 'position' is '99999999'
# df_main = df_main[df_main['position'] != '99999999']
#
# # Save the updated DataFrame to the same Excel file
# df_main.to_excel('post_processed_target/JobInfoImportTemplate_theroyalmeD.xlsx', index=False)
#
# # Read nonEmployees.xlsx file
# non_employees_df = pd.read_excel('source/nonEmployees.xlsx')
#
# # Read JobInfoImportTemplate_theroyalmeT1.xlsx_output.xlsx file
# job_info_df = pd.read_excel('post_processed_target/JobInfoImportTemplate_theroyalmeD.xlsx')
#
# # Define mapping for honorary and volunteer labels
# label_mapping = {
#     'honorary': {
#         'payScaleArea': 'AUS/HY',
#         'payScaleType': 'AUS/HY',
#         'payScaleGroup': 'AUS/HY/HY/HY',
#         'payScaleLevel': 'AUS/HY/HY/HY/HY'
#     },
#     'volunteer': {
#         'payScaleArea': 'AUS/VR',
#         'payScaleType': 'AUS/VR',
#         'payScaleGroup': 'AUS/VR/VR/VR',
#         'payScaleLevel': 'AUS/VR/VR/VR/VR'
#     }
# }
#
# # Function to update job_info_df based on label
# def update_job_info(row):
#     pers_no = row['Pers.No.']
#     label = row['Label']
#     mapping = label_mapping.get(label, {})
#
#     # Find the corresponding row in job_info_df
#     job_row = job_info_df[job_info_df['user-id'] == pers_no]
#
#     # Update 'payScale' columns if a matching row is found
#     if not job_row.empty:
#         job_info_df.loc[job_row.index, 'payScaleArea'] = mapping.get('payScaleArea', '')
#         job_info_df.loc[job_row.index, 'payScaleType'] = mapping.get('payScaleType', '')
#         job_info_df.loc[job_row.index, 'payScaleGroup'] = mapping.get('payScaleGroup', '')
#         job_info_df.loc[job_row.index, 'payScaleLevel'] = mapping.get('payScaleLevel', '')
#
# # Apply the function to each row in non_employees_df
# non_employees_df.apply(update_job_info, axis=1)
#
# # Loop through the 'job-code' column in job_info_df
# for index, row in job_info_df.iterrows():
#     job_code = row['job-code']
#
#     # Check if job code is 'HONORARY'
#     if job_code == 'HONORARY':
#         # Update 'payScale' columns based on the honorary mapping
#         job_info_df.at[index, 'payScaleArea'] = label_mapping['honorary']['payScaleArea']
#         job_info_df.at[index, 'payScaleType'] = label_mapping['honorary']['payScaleType']
#         job_info_df.at[index, 'payScaleGroup'] = label_mapping['honorary']['payScaleGroup']
#         job_info_df.at[index, 'payScaleLevel'] = label_mapping['honorary']['payScaleLevel']
#
#
# # Specify Pers.No. values to be updated to honorary scale
# pers_no_to_update_honorary = [127582, 84658, 122118]
#
# # Update pay scale for specified Pers.No. values
# for pers_no in pers_no_to_update_honorary:
#     job_info_df.loc[job_info_df['user-id'] == pers_no, 'payScaleArea'] = label_mapping['honorary']['payScaleArea']
#     job_info_df.loc[job_info_df['user-id'] == pers_no, 'payScaleType'] = label_mapping['honorary']['payScaleType']
#     job_info_df.loc[job_info_df['user-id'] == pers_no, 'payScaleGroup'] = label_mapping['honorary']['payScaleGroup']
#     job_info_df.loc[job_info_df['user-id'] == pers_no, 'payScaleLevel'] = label_mapping['honorary']['payScaleLevel']
#
#
# # Specify Pers.No. values to be deleted
# pers_no_to_delete = [89413, 95840, 97407, 98394, 126985, 106223, 106224, 106225, 106226]
#
# # Delete rows with specified Pers.No. values
# job_info_df = job_info_df[~job_info_df['user-id'].isin(pers_no_to_delete)]
#
# # Save the updated job_info_df to a new Excel file
# job_info_df.to_excel('post_processed_target/JobInfoImportTemplate_theroyalmeD.xlsx', index=False)
#
# # Read the Excel file into a DataFrame
# file_path = 'post_processed_target/JobInfoImportTemplate_theroyalmeD.xlsx'
# df = pd.read_excel(file_path)
#
# # Read the Excel file into a DataFrame
# file_path = 'post_processed_target/JobInfoImportTemplate_theroyalmeD.xlsx'
# df = pd.read_excel(file_path)
#
# # Read WorkLocation.xlsx
# work_location_df = pd.read_excel('source/WorkLocation.xlsx')
#
# # Iterate through each row of 'df'
# for index_df, row_df in df.iterrows():
#     business_unit_df = str(row_df['business-unit']).strip()  # Strip leading/trailing whitespaces
#     match_found = False  # Initialize a flag to check if a match is found
#
#     # Check if 'L' is in the business unit
#     if 'L' in business_unit_df:
#         # Split based on '-' and take the first part for comparison
#         business_unit_df = business_unit_df.split('-')[0].strip()
#
#     # Check for a matching location in 'work_location_df'
#     match_location = work_location_df.loc[work_location_df['Org Unit Number'].astype(str).str.strip() == business_unit_df, 'Location']
#
#     if not match_location.empty:
#         # Update 'custom-string14' column in 'df' with the corresponding 'Location' value
#         df.at[index_df, 'custom-string14'] = match_location.iloc[0]
#         match_found = True
#
#     # Print a message if no match is found for the current row in 'df'
#     if not match_found:
#         print(f"No matching location found for business unit {business_unit_df}")
#
# df['positionEntryDate'] = df['positionEntryDate'].apply(convert_to_date)
# df['start-date'] = df['start-date'].apply(convert_to_date)
#
# # Save the modified DataFrame back to the Excel file
# df.to_excel(file_path, index=False)
#
# print("Job file updated successfully.")
#
# # EMERGENCY
#
# # Read the Excel file
# file_path = 'target/EmergencyContactImportTemplate_theroyalmeD_output.xlsx'
# df = pd.read_excel(file_path)
#
# df = df[df['operation'] == 4]
# df['operation'] = None
#
# df.to_excel("post_processed_target/EmergencyContactImportTemplate_theroyalmeD.xlsx", index=False)
#
# print("Emergency contact file updated successfully.")
#
# # PAYMENT/BANKING DETAILS
#
# # Read the Excel file
# file_path = 'target/Payment Info Details_theroyalmeD_output.xlsx'
# df = pd.read_excel(file_path)
#
# # Replace values in the "payid" column
# df['toPaymentInformationDetailV3.payType'] = df['toPaymentInformationDetailV3.payType'].replace({0: 'MAIN', 1: 'PAYROLL'})
#
# # Replace values in the "payidname" column based on the "payid" column
# df.loc[df['toPaymentInformationDetailV3.payType'] == 'MAIN', 'toPaymentInformationDetailV3.customPayType.externalCode'] = 'Main Payment Method'
# df.loc[df['toPaymentInformationDetailV3.payType'] == 'PAYROLL', 'toPaymentInformationDetailV3.customPayType.externalCode'] = 'Other Banks'
#
# # Save the modified DataFrame back to the Excel file
# df.to_excel("post_processed_target/Banking Details-Details.xlsx", index=False)
#
# print("Payment/Banking details file updated successfully.")

# ALTERNATIVE COST DISTRIBUTION

# import pandas as pd

# # Load PA0027.xlsx file
# pa0027_df = pd.read_excel("source/PA0027.xlsx")

# # Load Alternative Cost Distribution_output.xlsx file
# alt_cost_dist_df = pd.read_excel("target/Alternative Cost Distribution-Alternative Cost Distribution_output.xlsx")

# # Iterate through each row in alt_cost_dist_df
# for index, row in alt_cost_dist_df.iterrows():
#     user_sys_id = row['usersSysId']
#     # Check if user_sys_id exists in Pers.No. column of pa0027_df
#     if user_sys_id in pa0027_df['Pers.No.'].values:
#         # Get the corresponding row in pa0027_df
#         matching_row = pa0027_df[pa0027_df['Pers.No.'] == user_sys_id].iloc[0]
#         # Concatenate CoCd and Cost Ctr values with "/" in between if they are not null
#         co_cd = str(matching_row['CoCd']) if not pd.isna(matching_row['CoCd']) else ""
#         cost_ctr = str(matching_row['Cost Ctr']) if not pd.isna(matching_row['Cost Ctr']) else ""
#         if co_cd and cost_ctr:
#             items_cost_center = co_cd + "/" + cost_ctr
#         else:
#             items_cost_center = ""
#         # Assign items_cost_center value to the respective row in alt_cost_dist_df
#         alt_cost_dist_df.at[index, 'items.costCenter.externalCode'] = items_cost_center

# #
# # Save the modified Alternative Cost Distribution_output.xlsx file
# alt_cost_dist_df.to_excel("post_processed_target/Alternative Cost Distribution-Alternative Cost Distribution.xlsx", index=False)

#BSIC USER PPR

import pandas as pd

# Read the Excel file
df = pd.read_excel('target/BasicUserInfoImportTemplate_theroyalmeD_output.xlsx')

# Keep only one row per USERID, prioritizing rows with non-empty EMAIL,
# and if there's no row with non-empty EMAIL, then select any row
df = df.sort_values(by='EMAIL', ascending=False).drop_duplicates(subset='USERID')

# Write the updated DataFrame back to Excel
df.to_excel('post_processed_target/BasicUserInfoImportTemplate_theroyalmeD.xlsx', index=False)

print("BASIC USER COMPLETE")

#COMP INFO PPR
df = pd.read_excel('target/CompInfoImportTemplate_theroyalmeD_output.xlsx')
if 'event-reason' in df.columns:
                    df['event-reason'] = 'HIRNEW'
df.to_excel('post_processed_target/CompInfoImportTemplate_theroyalmeD.xlsx', index=False)

print("COMP INFO COMPLETE")

