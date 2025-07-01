#BSIC USER PPR

import pandas as pd

# Read the Excel file
df = pd.read_excel('target/BasicUserInfoImportTemplate_theroyalmeD_output.xlsx')
df = df.drop_duplicates()

# Convert 'start-date' column to datetime format
df['HIREDATE'] = pd.to_datetime(df['HIREDATE'], format='%d/%m/%Y', errors='coerce')

# Create a mask for dates less than 26/2/2024
mask = df['HIREDATE'] < pd.Timestamp('2024-02-26')

# Update dates less than 26/2/2024 to 26/2/2024
df.loc[mask, 'HIREDATE'] = pd.Timestamp('2024-02-26')
df = df.drop_duplicates()

df['EMAIL'] = df['EMAIL'].fillna(df['USERID'].astype(str) + "noemail@mh.org.au")

df.to_excel('post_processed_target/BasicUserInfoImportTemplate_theroyalmeD.xlsx', index=False)

print("BASIC USER COMPLETE")

# PERSON INFO PPR

import pandas as pd
df = pd.read_excel('target/PersonInfoImportTemplate_theroyalmeD_output.xlsx')
df.to_excel('post_processed_target/PersonInfoImportTemplate_theroyalmeD.xlsx', index=False)

print("PERSON INFO COMPLETE")

# EMPLOYMENT INFO PPR

import pandas as pd
df = pd.read_excel('target/EmploymentInfoImportTemplate_theroyalmeT1_output.xlsx')
df = df.drop_duplicates()

# Convert 'start-date' column to datetime format
df['start-date'] = pd.to_datetime(df['start-date'], format='%d/%m/%Y', errors='coerce')

# Create a mask for dates less than 26/2/2024
mask = df['start-date'] < pd.Timestamp('2024-02-26')

# Update dates less than 26/2/2024 to 26/2/2024
df.loc[mask, 'start-date'] = pd.Timestamp('2024-02-26')

# Convert start-date to datetime
df['start-date'] = pd.to_datetime(df['start-date'], format='%d/%m/%Y', errors='coerce')

# Sort DataFrame by start-date
df = df.sort_values(by='start-date')

# Group by user-id and keep row with smallest start-date in each group
df = df.groupby('user-id').first().reset_index()

df.to_excel('post_processed_target/EmploymentInfoImportTemplate_theroyalmeD.xlsx', index=False)

print("EMPLOYMENT INFO COMPLETE")

# ADDRESS INFO PPR

# Read the Excel file
df = pd.read_excel('target/AddressImportTemplate_theroyalmeD_output.xlsx')
df = df.drop_duplicates()

# Convert 'start-date' column to datetime format
df['start-date'] = pd.to_datetime(df['start-date'], format='%d/%m/%Y', errors='coerce')

# Create a mask for dates less than 26/2/2024
mask = df['start-date'] < pd.Timestamp('2024-02-26')

# Update dates less than 26/2/2024 to 26/2/2024
df.loc[mask, 'start-date'] = pd.Timestamp('2024-02-26')

df = df[~df['address-type'].isin([90, 4, 5])]

# Replace the values in the 'address-type' column with 'home'
df['address-type'] = 'home'

shortforms_states = {
    "NSW": "New South Wales",
    "VIC": "Victoria",
    "QLD": "Queensland",
    "SA": "South Australia",
    "WA": "Western Australia",
    "TAS": "Tasmania",
    "NT": "Northern Territory",
    "ACT": "Australian Capital Territory"
}

# Mapping short forms to full names using the dictionary
df['state'] = df['state'].map(lambda x: shortforms_states.get(x, x))

df.loc[df['zip-code'].notnull(), 'zip-code'] = df.loc[df['zip-code'].notnull(), 'zip-code'].astype(str).str.zfill(4)

df.to_excel('post_processed_target/AddressImportTemplate_theroyalmeD.xlsx', index=False)

print("ADDRESS INFO PPR COMPLETE")

# BANKING DETAILS PPR

# Read the Excel file
df = pd.read_excel('target/Banking Details-Details_output.xlsx')
df = df.drop_duplicates()

# Convert 'start-date' column to datetime format
df['effectiveStartDate'] = pd.to_datetime(df['effectiveStartDate'], format='%d/%m/%Y', errors='coerce')


# Create a mask for dates less than 26/2/2024
mask = df['effectiveStartDate'] < pd.Timestamp('2024-02-26')

# Update dates less than 26/2/2024 to 26/2/2024
df.loc[mask, 'effectiveStartDate'] = pd.Timestamp('2024-02-26')

# Replace values in the "payid" column
df['toPaymentInformationDetailV3.payType'] = df['toPaymentInformationDetailV3.payType'].replace({0: 'MAIN', 1: 'PAYROLL'})

# Replace values in the "payidname" column based on the "payid" column
df.loc[df['toPaymentInformationDetailV3.payType'] == 'MAIN', 'toPaymentInformationDetailV3.customPayType.externalCode'] = 'Main Payment Method'
df.loc[df['toPaymentInformationDetailV3.payType'] == 'PAYROLL', 'toPaymentInformationDetailV3.customPayType.externalCode'] = 'Other Banks'

# Assuming df is your DataFrame
df['toPaymentInformationDetailV3.bankCountry.code'] = df['toPaymentInformationDetailV3.bankCountry.code'].replace('AU', 'AUS')

df.to_excel('post_processed_target/Banking Details-Details.xlsx', index=False)

print("BANKING DETAILS PPR COMPLETE")

# COMP INFO PPR

# Read the Excel file
df = pd.read_excel('target/CompInfoImportTemplate_theroyalmeD_output.xlsx')
df = df.drop_duplicates()

# Convert 'start-date' column to datetime format
df['start-date'] = pd.to_datetime(df['start-date'], format='%d/%m/%Y', errors='coerce')

# Create a mask for dates less than 26/2/2024
mask = df['start-date'] < pd.Timestamp('2024-02-26')

# Update dates less than 26/2/2024 to 26/2/2024
df.loc[mask, 'start-date'] = pd.Timestamp('2024-02-26')

df = df[df['pay-group'] == 'NM']

df.to_excel('post_processed_target/CompInfoImportTemplate_theroyalmeD.xlsx', index=False)

print("COMP INFO PPR COMPLETE")

# EMAIL INFO PPR

# Read the Excel file
df = pd.read_excel('target/EmailInfoImportTemplate_theroyalmeD_output.xlsx')
df = df.drop_duplicates()

df['email-type'] = 'Business Email'
df['isPrimary'] = 'Yes'

df['email-address'] = df['email-address'].fillna(df['personInfo.person-id-external'].astype(str) + "noemail@mh.org.au")

df.to_excel('post_processed_target/EmailInfoImportTemplate_theroyalmeD.xlsx', index=False)

print("EMAIL INFO PPR COMPLETE")

# EMERGENCY CONTACT PPR

# Read the Excel file
df = pd.read_excel('target/EmergencyContactImportTemplate_theroyalmeD_output.xlsx')
df = df.drop_duplicates()

# Keep rows where 'operation' column equals 4 after converting to int
df = df[df['operation'].astype(str) == '4']

# Fill empty values in 'homeAddress.country' column with 'AU'
df['homeAddress.country'].fillna('AU', inplace=True)

# Function to convert text to camel case
def to_camel_case(text):
    if text and isinstance(text, str):
        parts = text.split()
        return ' '.join([parts[0].capitalize()] + [part.capitalize() for part in parts[1:]])
    return text

# Apply camel case conversion to 'name' and 'relationship' columns
df['name'] = df['name'].apply(to_camel_case)
df['relationship'] = df['relationship'].apply(to_camel_case)

# Function to extract text within parentheses
def extract_within_parentheses(text):
    if isinstance(text, str) and '(' in text and ')' in text:
        start_index = text.find('(') + 1
        end_index = text.find(')')
        return text[start_index:end_index]
    return text

# Apply function to 'relationship' column
df['relationship'] = df['relationship'].apply(extract_within_parentheses)
df['relationship'] = df['relationship'].apply(to_camel_case)
df.loc[df['homeAddress.zip-code'].notnull(), 'homeAddress.zip-code'] = df.loc[df['homeAddress.zip-code'].notnull(), 'homeAddress.zip-code'].astype(str).str.zfill(4)
df['operation'] = None
df['primary_flag'] = "Yes"

shortforms_states = {
    "NSW": "New South Wales",
    "VIC": "Victoria",
    "QLD": "Queensland",
    "SA": "South Australia",
    "WA": "Western Australia",
    "TAS": "Tasmania",
    "NT": "Northern Territory",
    "ACT": "Australian Capital Territory"
}

# Mapping short forms to full names using the dictionary
df['homeAddress.state'] = df['homeAddress.state'].map(lambda x: shortforms_states.get(x, x))

def extract_within_parentheses(text):
    if isinstance(text, str) and '(' in text:
        start_index = text.find('(')
        return text[:start_index].strip()
    return text

df['name'] = df['name'].apply(extract_within_parentheses)
df['name'] = df['name'].apply(to_camel_case)


# Save the modified DataFrame back to Excel
df.to_excel('post_processed_target/EmergencyContactImportTemplate_theroyalmeD.xlsx', index=False)

print("EMERGENCY CONTACT PPR COMPLETE")

# MEDICARE PPR

# Read the Excel file
df = pd.read_excel('target/Medicare Numbers_output.xlsx')
df = df.drop_duplicates()
df.to_excel('post_processed_target/Medicare Numbers.xlsx', index=False)

print("MEDICARE PPR COMPLETE")

# NDIS PPR

# Read the Excel file
df = pd.read_excel('target/NDIS Worker Screening Check_output.xlsx')
df = df.drop_duplicates()
df.to_excel('post_processed_target/NDIS Worker Screening Check.xlsx', index=False)

print("NDIS PPR COMPLETE")

# PERSONAL PPR

# Read the Excel file
df = pd.read_excel('target/PersonalInfoImportTemplate_theroyalmeD_output.xlsx')
df = df.drop_duplicates()

# Convert 'start-date' column to datetime format
df['start-date'] = pd.to_datetime(df['start-date'], format='%d/%m/%Y', errors='coerce')

# Create a mask for dates less than 26/2/2024
mask = df['start-date'] < pd.Timestamp('2024-02-26')

# Update dates less than 26/2/2024 to 26/2/2024
df.loc[mask, 'start-date'] = pd.Timestamp('2024-02-26')

df['custom-string4'] = df['custom-string4'].fillna('Self Identify')

df.to_excel('post_processed_target/PersonalInfoImportTemplate_theroyalmeD.xlsx', index=False)

print("PERSONAL PPR COMPLETE")

# PHONE PPR

# Read the Excel file
df1 = pd.read_excel('target/PhoneInfoImportTemplate_theroyalmeD1_output.xlsx')
df2 = pd.read_excel('target/PhoneInfoImportTemplate_theroyalmeD2_output.xlsx')
df3 = pd.read_excel('target/PhoneInfoImportTemplate_theroyalmeD3_output.xlsx')
df1 = df1.drop_duplicates()
df2 = df2.drop_duplicates()
df3 = df3.drop_duplicates()
# Concatenate the dataframes
combined_df = pd.concat([df1, df2, df3], ignore_index=True)
# print(df1.columns)
# print(df2.columns)
# print(df3.columns)
# print(combined_df.columns)

# Convert phone-type column to string
combined_df['phone-type'] = combined_df['phone-type'].astype(str)

# Remove rows where phone-type is '90' or '4'
combined_df = combined_df[~combined_df['phone-type'].isin(['90', '4', '5', 'nan', 'OTHR', 'PAGE', 'TEL2', 'Phone Type'])]

# Replace values based on conditions
combined_df['phone-type'].replace({'1': 'Home', 'WORK': 'Business', 'CELL': 'Cell'}, inplace=True)
combined_df['phone-type'] = combined_df['phone-type'].fillna('Other')

combined_df.loc[combined_df['phone-type'] == 'Home', 'isPrimary'] = 'Yes'
combined_df.loc[combined_df['phone-type'] != 'Home', 'isPrimary'] = 'No'

combined_df.dropna(subset=['phone-number'], inplace=True)

# Save the combined dataframe to a new Excel file
combined_df.to_excel('post_processed_target/PhoneInfoImportTemplate_theroyalmeD.xlsx', index=False)

print("PHONE PPR COMPLETE")