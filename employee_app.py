import streamlit as st
import pandas as pd
import chardet
import numpy as np
from io import StringIO, BytesIO
from typing import Dict, List, Optional, Tuple

# Initialize session state
if 'current_step' not in st.session_state:
    st.session_state.current_step = 'validation'
if 'file_reviews' not in st.session_state:
    st.session_state.file_reviews = {}
if 'cleansed_files' not in st.session_state:
    st.session_state.cleansed_files = {}
if 'target_data' not in st.session_state:
    st.session_state.target_data = None
if 'default_values' not in st.session_state:
    st.session_state.default_values = {
        'STATUS': 'Active', 'HR': 'NO_HR', 
        'TIMEZONE': 'Australia/Melbourne', 'STATE': 'VIC',
        'COUNTRY': 'Australia', 'REVIEW_FREQ': 'Annual'
    }
if 'gender_mapping' not in st.session_state:
    st.session_state.gender_mapping = {'1': 'Male', '2': 'Female', 'Other': 'Others'}
if 'manager_blank_action' not in st.session_state:
    st.session_state.manager_blank_action = "Set to 'NO_MANAGER'"
if 'manager_copy_field' not in st.session_state:
    st.session_state.manager_copy_field = None
if 'custom_transforms' not in st.session_state:
    st.session_state.custom_transforms = {}

def main():
    if st.session_state.current_step == 'validation':
        show_validation_page()
    elif st.session_state.current_step == 'mapping':
        show_mapping_page()

def validate_file(file) -> Dict:
    """Comprehensive file validation with detailed findings"""
    result = {
        'status': 'ok',
        'message': '',
        'issues': [],
        'encoding': None,
        'stats': {},
        'recommendations': []
    }
    
    # Basic validations
    if not file.name.lower().endswith(('.csv', '.xlsx')):
        result.update({
            'status': 'error',
            'message': 'Invalid file type. Only CSV or Excel files accepted.',
            'recommendations': [{
                'action': 'reupload',
                'description': 'Please upload a CSV or Excel file'
            }]
        })
        return result
    
    if len(file.getvalue()) == 0:
        result.update({
            'status': 'error',
            'message': 'File is empty',
            'recommendations': [{
                'action': 'reupload',
                'description': 'Upload a non-empty file'
            }]
        })
        return result
    
    # Excel specific validation
    if file.name.endswith('.xlsx'):
        try:
            df = pd.read_excel(file, nrows=5)  # Sample first 5 rows
            result['stats'] = {
                'sample_data': df.head(),
                'num_rows': len(df),
                'num_columns': len(df.columns),
                'empty_cells': df.isna().sum().sum(),
                'duplicate_rows': df.duplicated().sum()
            }
            return result
        except Exception as e:
            result.update({
                'status': 'error',
                'message': f'Invalid Excel file: {str(e)}',
                'recommendations': [{
                    'action': 'reupload',
                    'description': 'Upload a valid Excel file or convert to CSV'
                }]
            })
            return result
    
    # CSV specific validation
    try:
        # Encoding detection
        rawdata = file.getvalue()[:10000]
        encoding = chardet.detect(rawdata)['encoding']
        result['encoding'] = encoding
        
        # Test read
        content = file.getvalue().decode(encoding)
        df = pd.read_csv(StringIO(content), nrows=100)
        result['stats'] = {
            'sample_data': df.head(),
            'num_rows': len(df),
            'num_columns': len(df.columns),
            'empty_cells': df.isna().sum().sum(),
            'duplicate_rows': df.duplicated().sum()
        }
        
        # Check for common issues
        if content.count('\x00') > 0:
            result['issues'].append({
                'type': 'null_bytes',
                'count': content.count('\x00'),
                'severity': 'high'
            })
            result['recommendations'].append({
                'action': 'remove_null_bytes',
                'description': 'Remove null byte characters',
                'impact': 'Will replace null bytes with empty values'
            })
        
        empty_cols = [col for col in df.columns if df[col].isna().all()]
        if empty_cols:
            result['issues'].append({
                'type': 'empty_columns',
                'columns': empty_cols,
                'severity': 'medium'
            })
            result['recommendations'].append({
                'action': 'drop_empty_columns',
                'description': f'Remove empty columns: {", ".join(empty_cols)}',
                'impact': f'Will drop {len(empty_cols)} column(s)'
            })
        
        # Update status based on findings
        if any(issue['severity'] == 'high' for issue in result['issues']):
            result['status'] = 'error'
        elif result['issues']:
            result['status'] = 'warning'
        
        result['message'] = "Found issues that need review" if result['issues'] else "File is valid"
        return result
        
    except UnicodeDecodeError:
        result.update({
            'status': 'error',
            'message': 'Encoding issue detected - file contains non-UTF-8 characters',
            'recommendations': [{
                'action': 'fix_encoding',
                'description': 'Attempt automatic encoding correction',
                'impact': 'Will try multiple encodings to read the file correctly'
            }]
        })
        return result
        
    except Exception as e:
        result.update({
            'status': 'error',
            'message': f'Unexpected error: {str(e)}',
            'recommendations': [{
                'action': 'reupload',
                'description': 'Try uploading the file again'
            }]
        })
        return result

def show_detailed_findings(filename: str, validation: Dict):
    """Displays comprehensive validation results"""
    st.subheader("Validation Summary")
    
    col1, col2 = st.columns(2)
    col1.metric("File Status", validation['status'].upper())
    if validation['encoding']:
        col2.metric("Detected Encoding", validation['encoding'])
    
    if validation['stats']:
        st.subheader("Data Preview")
        st.dataframe(validation['stats']['sample_data'])
        
        st.subheader("Basic Statistics")
        cols = st.columns(4)
        cols[0].metric("Columns", validation['stats']['num_columns'])
        cols[1].metric("Sample Rows", validation['stats']['num_rows'])
        cols[2].metric("Empty Cells", validation['stats']['empty_cells'])
        cols[3].metric("Duplicate Rows", validation['stats']['duplicate_rows'])
    
    if validation['issues']:
        st.subheader("Detected Issues")
        for issue in validation['issues']:
            with st.container():
                st.markdown(f"**{issue['type'].replace('_', ' ').title()}**")
                cols = st.columns(3)
                cols[0].write(f"Severity: {issue['severity']}")
                if 'count' in issue:
                    cols[1].write(f"Count: {issue['count']}")
                if 'columns' in issue:
                    cols[2].write(f"Columns: {', '.join(issue['columns'])}")

def render_recommendations(filename: str, validation: Dict):
    """Displays interactive recommendations with user choices"""
    for i, recommendation in enumerate(validation['recommendations']):
        with st.container():
            st.markdown(f"#### Recommendation {i+1}")
            cols = st.columns([3, 1])
            cols[0].write(recommendation['description'])
            
            # Track user decisions in session state
            key = f"{filename}_{recommendation['action']}"
            if key not in st.session_state.file_reviews[filename]['user_actions']:
                st.session_state.file_reviews[filename]['user_actions'][key] = True
            
            # Show toggle for each recommendation
            st.session_state.file_reviews[filename]['user_actions'][key] = cols[1].checkbox(
                "Apply this fix", 
                value=True,
                key=key,
                help=recommendation.get('impact', '')
            )
            
            if 'impact' in recommendation:
                st.caption(f"Impact: {recommendation['impact']}")

def apply_user_actions(file, review) -> Tuple[pd.DataFrame, Dict]:
    """Applies user-selected cleansing actions"""
    validation = review['validation']
    actions = review['user_actions']
    report = {
        'original_stats': validation['stats'],
        'applied_actions': [],
        'new_stats': None
    }
    
    try:
        # Handle encoding issues first
        if any('fix_encoding' in key for key in actions if actions[key]):
            file.seek(0)
            for encoding in ['utf-8', 'latin-1', 'windows-1252', 'iso-8859-1']:
                try:
                    content = file.getvalue().decode(encoding)
                    df = pd.read_csv(StringIO(content))
                    report['applied_actions'].append(f"Applied encoding: {encoding}")
                    break
                except UnicodeDecodeError:
                    continue
            else:
                raise ValueError("Failed to decode with any supported encoding")
        else:
            # Read with original encoding
            content = file.getvalue().decode(validation['encoding'])
            df = pd.read_csv(StringIO(content))
    
        # Apply other user-selected actions
        for action_key, should_apply in actions.items():
            if not should_apply:
                continue
                
            if 'remove_null_bytes' in action_key:
                df = df.replace('\x00', np.nan)
                report['applied_actions'].append("Removed null bytes")
            
            if 'drop_empty_columns' in action_key:
                empty_cols = [col for col in df.columns if df[col].isna().all()]
                if empty_cols:
                    df = df.drop(columns=empty_cols)
                    report['applied_actions'].append(f"Dropped empty columns: {', '.join(empty_cols)}")
        
        # Generate post-cleansing stats
        report['new_stats'] = {
            'sample_data': df.head(),
            'num_rows': len(df),
            'num_columns': len(df.columns),
            'empty_cells': df.isna().sum().sum(),
            'duplicate_rows': df.duplicated().sum()
        }
        return df, report
        
    except Exception as e:
        st.error(f"Error during cleansing: {str(e)}")
        raise

def show_cleansing_report(filename: str, report: Dict):
    """Displays comprehensive cleansing results"""
    with st.expander(f"🧹 Cleansing Report for {filename}", expanded=True):
        st.subheader("Applied Actions")
        for action in report['applied_actions']:
            st.markdown(f"- {action}")
        
        st.subheader("Before vs After")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Original File**")
            st.write(f"Rows: {report['original_stats']['num_rows']}")
            st.write(f"Columns: {report['original_stats']['num_columns']}")
            st.write(f"Empty cells: {report['original_stats']['empty_cells']}")
        
        with col2:
            st.markdown("**Cleaned File**")
            st.write(f"Rows: {report['new_stats']['num_rows']}")
            st.write(f"Columns: {report['new_stats']['num_columns']}")
            st.write(f"Empty cells: {report['new_stats']['empty_cells']}")
        
        # Show comparison metrics
        st.subheader("Data Quality Improvement")
        if report['original_stats']['empty_cells'] > report['new_stats']['empty_cells']:
            st.success(f"Reduced empty cells by {report['original_stats']['empty_cells'] - report['new_stats']['empty_cells']}")
        else:
            st.info("Empty cell count unchanged")
        
        if report['original_stats']['num_columns'] > report['new_stats']['num_columns']:
            st.success(f"Removed {report['original_stats']['num_columns'] - report['new_stats']['num_columns']} empty columns")

def load_clean_file(file, validation) -> pd.DataFrame:
    """Loads validated file without cleansing"""
    if file.name.endswith('.xlsx'):
        return pd.read_excel(file)
    
    content = file.getvalue().decode(validation['encoding'])
    return pd.read_csv(StringIO(content))

def merge_data() -> pd.DataFrame:
    """Merges all source files into a single dataframe"""
    pa0002 = st.session_state.cleansed_files.get('PA0002')
    pa0001 = st.session_state.cleansed_files.get('PA0001')
    pa0006 = st.session_state.cleansed_files.get('PA0006')
    pa0105 = st.session_state.cleansed_files.get('PA0105')
    
    if not all([pa0002, pa0001, pa0006, pa0105]):
        raise ValueError("Missing required source files")
    
    return pa0002.merge(
        pa0001, 
        on='Pers.No.', 
        how='left'
    ).merge(
        pa0006,
        on='Pers.No.', 
        how='left'
    ).merge(
        pa0105,
        on='Pers.No.', 
        how='left'
    )

def apply_transformations(df: pd.DataFrame) -> pd.DataFrame:
    """Applies all transformations to create target data"""
    target_data = pd.DataFrame()
    
    # Apply default values
    for col, val in st.session_state.default_values.items():
        target_data[col] = val
    
    # Apply predefined transformations
    def transform_gender(gender_key):
        gender_key = str(gender_key)
        if gender_key in st.session_state.gender_mapping:
            return st.session_state.gender_mapping[gender_key]
        return st.session_state.gender_mapping['Other']
    
    target_data['GENDER'] = df['Gender Key'].apply(transform_gender)
    
    # Manager handling
    if st.session_state.manager_blank_action == "Set to 'NO_MANAGER'":
        target_data['MANAGER'] = df['Name of superior (OM)'].fillna('NO_MANAGER')
    elif st.session_state.manager_blank_action == "Set to empty string":
        target_data['MANAGER'] = df['Name of superior (OM)'].fillna('')
    else:
        target_data['MANAGER'] = df[st.session_state.manager_copy_field]
    
    # Apply custom transformations
    for col, code in st.session_state.custom_transforms.items():
        try:
            local_vars = {'df': df}
            global_vars = {}
            exec(f"result = {code}", global_vars, local_vars)
            target_data[col] = local_vars['result']
        except Exception as e:
            st.error(f"Error in custom transform for {col}: {str(e)}")
            target_data[col] = None
    
    # Target columns list
    target_columns = [
        'STATUS', 'USERID', 'USERNAME', 'FIRSTNAME', 'NICKNAME', 'MI', 'LASTNAME', 
        'SUFFIX', 'TITLE', 'GENDER', 'EMAIL', 'MANAGER', 'HR', 'DEPARTMENT', 
        'JOBCODE', 'DIVISION', 'LOCATION', 'TIMEZONE', 'HIREDATE', 'EMP', 'BZ', 
        'PHONE', 'FAX', 'ADDR1', 'ADDR2', 'CITY', 'STATE', 'ZIP', 'COUNTRY', 
        'REVIEW_FREQ', 'LAST_REVIEW', 'MATRIX_MANAGER', 'DEFAULT_LOC', 'PROXY', 
        '_seatingChart', 'ASSIGNMENT', 'DISPLAYNAME', 'PERSON.ID_', 'ASSIGNMENT_ID', 
        'EXTERNAL'
    ]
    
    # Fill in remaining columns with direct mappings or empty values
    if 'USERID' not in st.session_state.custom_transforms:
        target_data['USERID'] = df['Pers.No.']
    if 'USERNAME' not in st.session_state.custom_transforms:
        target_data['USERNAME'] = df['First name'] + ' ' + df['Last name']
    # ... (all other direct mappings as previously defined)
    
    # Ensure all target columns exist
    for col in target_columns:
        if col not in target_data:
            target_data[col] = ''
    
    return target_data[target_columns]

def show_validation_page():
    st.title("Data Validation")
    uploaded_files = st.file_uploader("Upload files (PA0001, PA0002, PA0006, PA0105)", 
                                    type=['csv', 'xlsx'], 
                                    accept_multiple_files=True)
    if uploaded_files:
        for file in uploaded_files:
            if file.name not in st.session_state.file_reviews:
                st.session_state.file_reviews[file.name] = {
                    'validation': None, 'user_actions': {}, 'processed': False
                }
            with st.expander(f"File: {file.name}"):
                file_review_workflow(file)
        
        if all(review['processed'] for review in st.session_state.file_reviews.values()):
            st.success("All files validated!")
            if st.button("Proceed to Mapping"):
                st.session_state.current_step = 'mapping'
                st.rerun()

def file_review_workflow(file):
    review = st.session_state.file_reviews[file.name]
    if review['validation'] is None:
        with st.spinner(f"Validating {file.name}..."):
            review['validation'] = validate_file(file)
    
    validation = review['validation']
    if validation['status'] == 'error':
        st.error(validation['message'])
    elif validation['status'] == 'warning':
        st.warning(validation['message'])
    else:
        st.success("File valid")
        st.session_state.cleansed_files[file.name] = load_clean_file(file, validation)
        review['processed'] = True
        return
    
    with st.expander("Details"):
        show_detailed_findings(file.name, validation)
    
    if validation['issues']:
        st.subheader("Recommended Fixes")
        render_recommendations(file.name, validation)
    
    if review['user_actions'] and st.button(f"Apply to {file.name}"):
        with st.spinner("Processing..."):
            cleansed_df, report = apply_user_actions(file, review)
            st.session_state.cleansed_files[file.name] = cleansed_df
            review['processed'] = True
            show_cleansing_report(file.name, report)

def show_mapping_page():
    st.title("Data Mapping")
    required_files = ['PA0001', 'PA0002', 'PA0006', 'PA0105']
    available_files = [f for f in st.session_state.cleansed_files.keys() 
                      if any(req in f for req in required_files)]
    
    if len(available_files) < 4:
        st.error("Missing required files")
        if st.button("Back to Validation"):
            st.session_state.current_step = 'validation'
            st.rerun()
        return
    
    st.subheader("Validated Source Files")
    for filename, df in st.session_state.cleansed_files.items():
        with st.expander(f"📄 {filename} (shape: {df.shape})"):
            st.dataframe(df.head())
    
    st.subheader("Default Values")
    cols = st.columns(3)
    with cols[0]:
        st.session_state.default_values['STATUS'] = st.text_input('STATUS', st.session_state.default_values['STATUS'])
        st.session_state.default_values['HR'] = st.text_input('HR', st.session_state.default_values['HR'])
    with cols[1]:
        st.session_state.default_values['TIMEZONE'] = st.text_input('TIMEZONE', st.session_state.default_values['TIMEZONE'])
        st.session_state.default_values['STATE'] = st.text_input('STATE', st.session_state.default_values['STATE'])
    with cols[2]:
        st.session_state.default_values['COUNTRY'] = st.text_input('COUNTRY', st.session_state.default_values['COUNTRY'])
        st.session_state.default_values['REVIEW_FREQ'] = st.text_input('REVIEW_FREQ', st.session_state.default_values['REVIEW_FREQ'])

    st.subheader("Transformations")
    selected_gender_map = st.selectbox("Gender Mapping", ["1 → Male, 2 → Female, else → Others", "Custom"])
    if selected_gender_map == "Custom":
        col1, col2, col3 = st.columns(3)
        with col1:
            male_val = st.text_input("Value for Male", "1")
        with col2:
            female_val = st.text_input("Value for Female", "2")
        with col3:
            other_val = st.text_input("Default Value", "Others")
        st.session_state.gender_mapping = {
            male_val: 'Male',
            female_val: 'Female',
            'Other': other_val
        }
    
    st.session_state.manager_blank_action = st.selectbox(
        "When Manager is blank",
        options=["Set to 'NO_MANAGER'", "Set to empty string", "Copy from another field"],
        index=0
    )

    if st.session_state.manager_blank_action == "Copy from another field":
        st.session_state.manager_copy_field = st.selectbox(
            "Field to copy from",
            options=st.session_state.cleansed_files['PA0001'].columns.tolist(),
            index=0
        )

    st.subheader("Custom Python Transformations")
    st.markdown("Write custom Python code to transform your data. Use `df` to reference the merged dataframe.")
    
    target_columns = [
        'USERNAME', 'EMAIL', 'PHONE', 'ADDR1', 'ADDR2', 'CITY', 'ZIP',
        'DEPARTMENT', 'JOBCODE', 'DIVISION', 'LOCATION', 'HIREDATE'
    ]
    
    for col in target_columns:
        with st.expander(col):
            current_code = st.session_state.custom_transforms.get(col, '')
            new_code = st.text_area(
                f"Code for {col}",
                value=current_code,
                height=100,
                key=f"code_{col}"
            )
            if new_code:
                st.session_state.custom_transforms[col] = new_code

    if st.button("Process Data"):
        with st.spinner("Mapping data..."):
            try:
                merged_data = merge_data()
                target_data = apply_transformations(merged_data)
                st.session_state.target_data = target_data
                st.success("Done!")
                st.dataframe(target_data.head())
                
                csv = target_data.to_csv(index=False)
                st.download_button(
                    "Download CSV",
                    data=csv,
                    file_name="mapped_data.csv",
                    mime="text/csv"
                )
            except Exception as e:
                st.error(f"Error: {str(e)}")

    if st.button("Back to Validation"):
        st.session_state.current_step = 'validation'
        st.rerun()

if __name__ == "__main__":
    main()