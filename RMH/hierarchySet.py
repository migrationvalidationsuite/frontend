#Import the required Libraries
import pandas as pd

try:
    # Load data from Excel file
    print("Loading data from Excel file...")
    df = pd.read_excel('source/PPR_HRP1001_OrgRelationships_O-O.xlsx')
    print("Data loaded successfully.")

    # Extract values in "Parent" column but not in "Entity ID" column (topmost level)
    parent_only_values = df.loc[~df['ID rel.object'].isin(df['Object ID']), 'ID rel.object'].unique()

    # Create DataFrame to store the hierarchy information
    hierarchy_df = pd.DataFrame(columns=['Object ID', 'ID rel.object', 'Level'])

    # Function to recursively find children and add them to the DataFrame
    def add_children_to_hierarchy(parent, level):
        children = df.loc[df['ID rel.object'] == parent, 'Object ID'].unique()
        for child in children:
            hierarchy_df.loc[len(hierarchy_df)] = [child, parent, level]
            add_children_to_hierarchy(child, level + 1)

    # Add topmost level to the hierarchy DataFrame
    for entity_id in parent_only_values:
        hierarchy_df.loc[len(hierarchy_df)] = [entity_id, entity_id, 0]
        add_children_to_hierarchy(entity_id, 1)

    # Save the hierarchy DataFrame to a CSV file
    hierarchy_df.to_csv('hierarchy.csv', index=False)
    print("Hierarchy information saved to 'hierarchy.csv'.")

except FileNotFoundError:
    print("Error: Excel file not found.")
except Exception as e:
    print(f"An error occurred 1: {e}")

print("first section done")

import pandas as pd

try:
    # Load hierarchy information from CSV file
    print("Loading hierarchy information...")
    hierarchy_df = pd.read_csv('hierarchy.csv')
    print("Hierarchy information loaded successfully.")

    # Load data from another sheet containing entity ID and description columns
    print("Loading data from another sheet...")
    description0_df = pd.read_excel('source/PPR_HRP1000_OrgUnits.xlsx')
    print("Data loaded successfully.")


    # Extract desired columns from the first file
    description_df = description0_df[['Object ID', 'Name']]  # Adjust columns as needed

    # Merge hierarchy information with description DataFrame
    merged_df = pd.merge(hierarchy_df, description_df, on='Object ID', how='left')

    # Save the merged DataFrame to a CSV file
    merged_df.to_csv('merged_hierarchy.csv', index=False)
    print("Merged hierarchy information saved to 'merged_hierarchy.csv'.")

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An error occurred 2: {e}")

print("second section done")

import pandas as pd

try:
    # Load hierarchy information from CSV file
    print("Loading hierarchy information...")
    hierarchy_df = pd.read_csv('merged_hierarchy.csv')
    print("Hierarchy information loaded successfully.")

    # Determine the maximum level in the hierarchy
    max_level = hierarchy_df['Level'].max()

    # Split the hierarchy information into separate DataFrames based on level
    for level in range(max_level + 1):
        level_df = hierarchy_df[hierarchy_df['Level'] == level]
        level_df.to_csv(f'level{level}.csv', index=False)
        print(f"Level {level} information saved to 'level{level}.csv'.")

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An error occurred 3: {e}")

print("third section done")

import pandas as pd

# Function to recursively get all children of a given SOBJID
def get_children(df, parent_col, parent):
    children = df[df[parent_col] == parent]['Object ID'].tolist()
    result = children[:]
    for child in children:
        result.extend(get_children(df, parent_col, child))
    return result

# Function to filter and display hierarchy elements under a given SOBJID
def display_hierarchy(df, objid_col, sobid_col, level_col, sobjid):
    children = get_children(df, sobid_col, sobjid)
    result = df[df[objid_col].isin(children)]
    return result

# Load the CSV file into a DataFrame
try:
    file_path = 'merged_hierarchy.csv'
    df = pd.read_csv(file_path)
    print("\nCSV file loaded successfully.")
except FileNotFoundError:
    print("Error: File not found. Please upload the CSV file.")
    exit()
except Exception as e:
    print("An error occurred while reading the CSV file:", e)
    exit()

# Convert columns to string data type and clean leading/trailing whitespaces
for col in df.columns:
    df[col] = df[col].astype(str).str.strip()

# Prompt user to enter a value for SOBJID
sobjid_input = input("\nEnter a value for SOBJID: ").strip()

# Check if the entered SOBJID exists in the dataframe
print("Checking SOBJID", sobjid_input, "in the data...")
if sobjid_input not in df['Object ID'].values:
    print("Error: SOBJID", sobjid_input, "not found in the data.")
    print("Available SOBJIDs:", df['Object ID'].values)
else:
    print("SOBJID", sobjid_input, "found in the data.")

    # Display hierarchy elements under the entered SOBJID
    hierarchy_elements = display_hierarchy(df, 'Object ID', 'ID rel.object', 'Level', sobjid_input)

    # Output hierarchy elements to a CSV file
    output_file_path = 'hierarchy_elements.csv'
    hierarchy_elements.to_csv(output_file_path, index=False)
    print(f"\nHierarchy elements under SOBJID {sobjid_input} have been written to {output_file_path}.")

print("fourth section done")
#
# import pandas as pd
#
# try:
#     # Load hierarchy information from CSV file
#     print("Loading hierarchy information...")
#     hierarchy_df = pd.read_csv('hierarchy_elements.csv')
#     print("Hierarchy information loaded successfully.")
#
#     # Determine the maximum level in the hierarchy
#     max_level = hierarchy_df['Level'].max()
#
#     # Split the hierarchy information into separate DataFrames based on level
#     for level in range(max_level + 1):
#         level_df = hierarchy_df[hierarchy_df['Level'] == level]
#         level_df.to_csv(f'level{level}.csv', index=False)
#         print(f"Level {level} information saved to 'level{level}.csv'.")
#
# except FileNotFoundError:
#     print("Error: File not found.")
# except Exception as e:
#     print(f"An error occurred 4: {e}")

print("fifth section done")

import pandas as pd

# Read the hierarchy_elements.csv file
hierarchy_df = pd.read_csv('hierarchy_elements.csv')

# Read the Org Relationships file
org_relationships_df = pd.read_excel('source/PPR_HRP1001_OrgRelationships_O-O.xlsx')

# Merge hierarchy_df with org_relationships_df to get the start date and end date
merged_df = pd.merge(hierarchy_df, org_relationships_df, left_on=['Object ID', 'ID rel.object'],
                     right_on=['Object ID', 'ID rel.object'], how='left')

# Select only the required columns
final_df = merged_df[['Object ID', 'ID rel.object', 'Level', 'Name', 'Start date', 'End Date']]

# Save the final DataFrame to hierarchy_elements.xlsx
final_df.to_excel('hierarchy_elements.xlsx', index=False)


# 2, 1 - business unit
# 3 - division, parent is corresponding business unit
# 4 - department
# 5 - sub department
# 6 - speciality
# 7 - sub speciality

# 51017851
