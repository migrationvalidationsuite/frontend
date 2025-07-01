"""
DATA MIGRATION TOOL - FLASK APPLICATION

Main application file containing all routes and functionality for:
- User authentication
- Data migration processes
- Payroll processing for multiple countries
- File management
- Data validation
- Chatbot integration
"""

# Import statements (keep all original imports)
from flask import Flask, request, redirect, url_for, render_template, send_from_directory, jsonify
import os
from flask import Flask, request, render_template, session, redirect, url_for
import os
import pandas as pd
from flask import Flask, render_template, redirect, url_for, request
import subprocess
import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory, flash
import os
import pandas as pd
import matplotlib.pyplot as plt
import io
import seaborn as sns
import numpy as np
from werkzeug.utils import secure_filename
import base64
import matplotlib
import sys
matplotlib.use('Agg')
from functools import wraps
from datetime import datetime
from openai import OpenAI
import logging

# Configure logging to track application events
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask application
app = Flask(__name__)

# ==============================================
# APPLICATION CONFIGURATION
# ==============================================

# Base directory for file uploads
BASE_DIR = 'uploads'
# Get current working directory
current_dir = os.path.abspath(os.getcwd())

# Create temporary folder for processing files
TEMP_FOLDER = 'temp'
os.makedirs(TEMP_FOLDER, exist_ok=True)
app.config['TEMP_FOLDER'] = TEMP_FOLDER

# Generate secure secret key for session management
app.secret_key = os.urandom(24)  # 24-byte random key

# Configure file storage locations
app.config['UPLOAD_FOLDER'] = os.path.join(current_dir, "uploads")  # Main upload directory
app.config['CANADA_FOLDER'] = os.path.join(current_dir, "CANADA")   # Canada-specific files
app.config['US_FOLDER'] = os.path.join(current_dir, "US")           # US-specific files
app.config['AUS_FOLDER'] = os.path.join(current_dir, "AUS")         # Australia-specific files

# Allowed file extensions for uploads
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'xlsx'}
# Maximum file size limit (16MB)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# User credentials (in production, use a proper database)
USERS = {
    'admin': 'Support01$'  # Single admin user with password
}

# Configure OpenAI client for chatbot functionality
client = OpenAI(api_key='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')

# ==============================================
# AUTHENTICATION DECORATORS AND HELPERS
# ==============================================

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


def allowed_file(filename):
    """
    Check if a filename has an allowed extension.
    Returns True if allowed, False otherwise.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def ensure_directory_exists(category, folder_type):
    """
    Ensure required directory structure exists for file storage.
    Creates directories if they don't exist.
    """
    directory = os.path.join(app.config['UPLOAD_FOLDER'], category, folder_type)
    os.makedirs(directory, exist_ok=True)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(f"Login attempt - username: {username}")  # Debug print

        if username in USERS and USERS[username] == password:
            session['logged_in'] = True
            session['username'] = username
            print("Login successful")  # Debug print
            next_page = request.args.get('next')
            return redirect(next_page or url_for('home'))
        else:
            print("Login failed")  # Debug print
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('login'))

# ==============================================
# CORE APPLICATION ROUTES
# ==============================================

@app.route('/')
@login_required
def home():
    """Main home page route - requires authentication"""
    print("Session:", session)  # Debug session info
    print("Logged in:", session.get('logged_in'))  # Debug login status
    return render_template('home.html')

@app.route("/data_migration_page")
@login_required
def data_migration_page():
    """Data migration overview page"""
    return render_template("data_migration_page.html")

@app.route("/validation_page")
@login_required
def validation_page():
    """Validation tools overview page"""
    return render_template("validation_page.html")

# ==============================================
# DATA MIGRATION ROUTES
# ==============================================

@app.route('/data-migration')
@login_required
def data_migration():
    """Main data migration landing page"""
    return render_template('data_migration.html')

@app.route('/datamigpayroll')
@login_required
def datamigpayroll():
    """Payroll data migration landing page"""
    print("US CANADA AUS")  # Debug output
    return render_template('datamigpayroll.html')

# Country-specific payroll routes
@app.route('/payrollCANADA')
def payrollCANADA():
    """Canada payroll page"""
    print("CANADA")  # Debug output
    return render_template('payrollCANADA.html')

@app.route('/payrollAUS')
def payrollAUS():
    """Australia payroll page"""
    print("AUS")  # Debug output
    return render_template('payrollAUS.html')

@app.route('/payrollUS')
def payrollUS():
    """US payroll page"""
    print("US")  # Debug output
    return render_template('payrollUS.html')

@app.route('/data-migration/<category>')
def data_migration_category(category):
    """
    Category-specific data migration page
    Valid categories: foundation, position, employee
    """
    if category not in ['foundation', 'position', 'employee']:
        return redirect(url_for('data_migration'))
    return render_template('data_migration_category.html', category=category)

# ==============================================
# FILE UPLOAD AND MANAGEMENT ROUTES
# ==============================================

@app.route('/data-migration/<category>/upload-source-extracts', methods=['GET', 'POST'])
def upload_source_extracts(category):
    """
    Handle source extract file uploads for a specific category
    Supports both GET (display form) and POST (process upload)
    """
    if category not in ['foundation', 'position', 'employee']:
        return redirect(url_for('data_migration'))

    # Ensure directory exists
    ensure_directory_exists(category, 'source_extracts')

    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            # Save file to appropriate directory
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], category, 'source_extracts', filename))
            return redirect(url_for('view_source_extracts', category=category))

    return render_template('upload_source_extracts.html', category=category)

@app.route('/data-migration/<category>/upload-workbook', methods=['GET', 'POST'])
def upload_workbook(category):
    """
    Handle workbook file uploads for a specific category
    Supports both GET (display form) and POST (process upload)
    """
    if category not in ['foundation', 'position', 'employee']:
        return redirect(url_for('data_migration'))

    # Ensure directory exists
    ensure_directory_exists(category, 'workbooks')

    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            # Save file to appropriate directory
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], category, 'workbooks', filename))
            return redirect(url_for('view_workbooks', category=category))

    return render_template('upload_workbook.html', category=category)

@app.route('/data-migration/<category>/view-source-extracts')
def view_source_extracts(category):
    """
    Display list of uploaded source extracts for a category
    """
    if category not in ['foundation', 'position', 'employee']:
        return redirect(url_for('data_migration'))

    source_extracts_dir = os.path.join(app.config['UPLOAD_FOLDER'], category, 'source_extracts')
    print("source extracts directory")  # Debug output
    print(source_extracts_dir)  # Debug output
    files = os.listdir(source_extracts_dir) if os.path.exists(source_extracts_dir) else []
    print(files)  # Debug output
    print("files^")  # Debug output
    print(os.path.exists(source_extracts_dir))  # Debug output
    return render_template('view_source_extracts.html', category=category, files=files)

@app.route('/data-migration/<category>/view-workbooks')
def view_workbooks(category):
    """
    Display list of uploaded workbooks for a category
    Only shows .xlsx files
    """
    if category not in ['foundation', 'position', 'employee']:
        return redirect(url_for('data_migration'))

    workbooks_dir = os.path.join(app.config['UPLOAD_FOLDER'], category, 'workbooks')
    files = [f for f in os.listdir(workbooks_dir) if f.endswith('.xlsx')] if os.path.exists(workbooks_dir) else []
    return render_template('view_workbooks.html', category=category, files=files)

# File serving routes
@app.route('/data-migration/<category>/source-extracts/<filename>')
def uploaded_file(category, filename):
    """
    Serve uploaded source extract file for download
    """
    return send_from_directory(os.path.join(app.config['UPLOAD_FOLDER'], category, 'source_extracts'), filename)

@app.route('/create_loadsheet/<category>/org/<filename>')
def uploaded_file_org(category, filename):
    """
    Serve organization structure file for download
    """
    return send_from_directory(os.path.join(app.config['UPLOAD_FOLDER'], category, 'org'), filename)

@app.route('/create_loadsheet/<category>/target/<filename>')
def uploaded_file_foundation(category, filename):
    """
    Serve foundation target file for download
    """
    return send_from_directory(os.path.join(app.config['UPLOAD_FOLDER'], category, 'target'), filename)

@app.route('/create_loadsheet/<category>/targetcsv/<filename>')
def uploaded_file_foundationcsv(category, filename):
    """
    Serve foundation CSV target file for download
    """
    return send_from_directory(os.path.join(app.config['UPLOAD_FOLDER'], category, 'targetcsv'), filename)

@app.route('/data-migration/<category>/workbooks/<filename>')
def workbook_file(category, filename):
    """
    Serve workbook file for download
    """
    return send_from_directory(os.path.join(app.config['UPLOAD_FOLDER'], category, 'workbooks'), filename)

# File deletion routes
@app.route('/data-migration/<category>/delete-source-extracts/<filename>', methods=['POST'])
def delete_source_extracts(category, filename):
    """
    Delete a source extract file
    """
    source_extracts_dir = os.path.join(app.config['UPLOAD_FOLDER'], category, 'source_extracts')
    file_path = os.path.join(source_extracts_dir, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    return redirect(url_for('view_source_extracts', category=category))

@app.route('/data-migration/<category>/delete-workbooks/<filename>', methods=['POST'])
def delete_workbook(category, filename):
    """
    Delete a workbook file
    """
    workbooks_dir = os.path.join(app.config['UPLOAD_FOLDER'], category, 'workbooks')
    file_path = os.path.join(workbooks_dir, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    return redirect(url_for('view_workbooks', category=category))

# ==============================================
# LOADSHEET GENERATION ROUTES
# ==============================================

@app.route('/data-migration/<category>/create-loadsheets', methods=['GET', 'POST'])
def create_loadsheets(category):
    """
    Generate loadsheets by executing processing scripts
    Handles both foundation and position/employee categories differently
    """
    print(category)  # Debug output
    if category not in ['foundation', 'position', 'employee']:
        return redirect(url_for('data_migration'))

    if category.lower() == 'foundation':
        # Process foundation data
        script_path = os.path.join(app.config['UPLOAD_FOLDER'], category, 'code', 'code.py')
        print(script_path)  # Debug output
        try:
            result = subprocess.run(['python', script_path], capture_output=True, text=True, check=True)
            output = result.stdout
            # Handle script output if necessary
        except subprocess.CalledProcessError as e:
            output = f"Error occurred: {e.stderr}"
        except Exception as e:
            output = f"Unexpected error: {str(e)}"
            print(f"Unexpected error: {output}")  # Debug output

        script_path = os.path.join(app.config['UPLOAD_FOLDER'], category, 'code', 'allfiles.py')
        print(script_path)  # Debug output
        try:
            result = subprocess.run(['python', script_path], capture_output=True, text=True, check=True)
            output = result.stdout
            # Handle script output if necessary
        except subprocess.CalledProcessError as e:
            output = f"Error occurred: {e.stderr}"
        except Exception as e:
            output = f"Unexpected error: {str(e)}"
            print(f"Unexpected error: {output}")  # Debug output

        source_extracts_dir = os.path.join(app.config['UPLOAD_FOLDER'], category, 'target')
        print(source_extracts_dir)  # Debug output
        files = os.listdir(source_extracts_dir) if os.path.exists(source_extracts_dir) else []

        # Convert to CSV
        script_path = os.path.join(app.config['UPLOAD_FOLDER'], category, 'code', 'tocsv.py')
        print(script_path)  # Debug output
        try:
            result = subprocess.run(['python', script_path], capture_output=True, text=True, check=True)
            output = result.stdout
            # Handle script output if necessary
        except subprocess.CalledProcessError as e:
            output = f"Error occurred: {e.stderr}"
        except Exception as e:
            output = f"Unexpected error: {str(e)}"
            print(f"Unexpected error: {output}")  # Debug output

        source_extracts_dir = os.path.join(app.config['UPLOAD_FOLDER'], category, 'targetcsv')
        print(source_extracts_dir)  # Debug output
        files2 = os.listdir(source_extracts_dir) if os.path.exists(source_extracts_dir) else []
        return render_template('position_loadsheet.html', category=category, files_xlsx=files, files_csv=files2)

    if category.lower() == 'position' or category.lower() == 'employee':
        print("working on position/employee loadsheet")  # Debug output
        if True:
            script_path = os.path.join(app.config['UPLOAD_FOLDER'], category, 'code', 'code.py')
            print(script_path)  # Debug output
            try:
                result = subprocess.run(['python', script_path], capture_output=True, text=True, check=True)
                output = result.stdout
                # Handle script output if necessary
            except subprocess.CalledProcessError as e:
                output = f"Error occurred: {e.stderr}"
            except Exception as e:
                output = f"Unexpected error: {str(e)}"
                print(f"Unexpected error: {output}")  # Debug output
        if True:
            script_path = os.path.join(app.config['UPLOAD_FOLDER'], category, 'code', 'allfiles.py')
            print(script_path)  # Debug output
            try:
                result = subprocess.run(['python', script_path], capture_output=True, text=True, check=True)
                output = result.stdout
                # Handle script output if necessary
            except subprocess.CalledProcessError as e:
                output = f"Error occurred: {e.stderr}"
            except Exception as e:
                output = f"Unexpected error: {str(e)}"
                print(f"Unexpected error: {output}")  # Debug output

        script_path = os.path.join(app.config['UPLOAD_FOLDER'], category, 'code', 'tocsv.py')
        print(script_path)  # Debug output
        try:
            result = subprocess.run(['python', script_path], capture_output=True, text=True, check=True)
            output = result.stdout
            # Handle script output if necessary
        except subprocess.CalledProcessError as e:
            output = f"Error occurred: {e.stderr}"
        except Exception as e:
            output = f"Unexpected error: {str(e)}"
            print(f"Unexpected error: {output}")  # Debug output

        source_extracts_dir = os.path.join(app.config['UPLOAD_FOLDER'], category, 'target')
        print(source_extracts_dir)  # Debug output
        files = os.listdir(source_extracts_dir) if os.path.exists(source_extracts_dir) else []
        source_extracts_dir = os.path.join(app.config['UPLOAD_FOLDER'], category, 'targetcsv')
        print(source_extracts_dir)  # Debug output
        files2 = os.listdir(source_extracts_dir) if os.path.exists(source_extracts_dir) else []
        return render_template('position_loadsheet.html', category=category, files_xlsx=files, files_csv=files2)

    return render_template('create_loadsheets.html', category=category)

# ==============================================
# VALIDATION ROUTES
# ==============================================

def allowed_file(filename):
    """Repeated function - checks for allowed file extensions"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def ensure_one_directory_exists(folder):
    """Ensure a single directory exists (creates if not)"""
    os.makedirs(folder, exist_ok=True)

@app.route('/validation', methods=['GET'])
def validation():
    """Validation tools landing page"""
    return render_template('validation.html')

@app.route('/data_comparisonECP', methods=['GET', 'POST'])
def data_comparisonECP():
    """
    Compare ECP data between legacy and SAP systems
    Handles both GET (display form) and POST (process comparison)
    """
    if request.method == 'POST':
        # Validate file uploads
        if 'legacyPayrollFile' not in request.files or 'sapPayrollFile' not in request.files or 'mappingFile' not in request.files:
            return "Missing file input.", 400

        legacy_file = request.files['legacyPayrollFile']
        sap_file = request.files['sapPayrollFile']
        mapping_file = request.files['mappingFile']

        # Check files were selected
        if legacy_file.filename == '' or sap_file.filename == '' or mapping_file.filename == '':
            return "No selected file.", 400

        # Helper function to read Excel with consistent typing
        def read_excel_file(file):
            return pd.read_excel(file, dtype={'LEGACY employee number': str, 'SAP employee number': str})

        try:
            # Read all input files
            legacy_df = read_excel_file(legacy_file)
            sap_df = read_excel_file(sap_file)
            mapping_df = read_excel_file(mapping_file)
        except Exception as e:
            return f"Error reading files: {e}", 400

        # Create wage type mapping
        wage_type_mapping = dict(zip(mapping_df['LEGACY'], mapping_df['SAP']))

        # Summarize SAP data
        sap_summary = (sap_df
                       .groupby(['SAP employee number', 'SAP wage type'])
                       ['SAP amount'].sum().reset_index()
                       .rename(columns={'SAP amount': 'amount_sap'}))

        # Summarize legacy data
        legacy_summary = (legacy_df
                          .groupby(['LEGACY employee number', 'LEGACY wage type'])
                          ['LEGACY amount'].sum().reset_index()
                          .rename(columns={'LEGACY amount': 'amount_legacy'}))

        # Map legacy wage types to SAP
        legacy_summary['SAP wage type mapped'] = legacy_summary['LEGACY wage type'].map(wage_type_mapping)

        # Merge the datasets
        merged_results = pd.merge(
            legacy_summary,
            sap_summary,
            left_on=['LEGACY employee number', 'SAP wage type mapped'],
            right_on=['SAP employee number', 'SAP wage type'],
            how='outer'
        )

        # Calculate differences
        merged_results['difference'] = merged_results['amount_legacy'].fillna(0) - merged_results['amount_sap'].fillna(0)
        filtered_results = merged_results[merged_results['difference'] != 0]  # Only show differences

        # Clean up results
        filtered_results = filtered_results.drop(columns=['difference']).fillna('Missing')
        filtered_results = filtered_results[['SAP employee number', 'SAP wage type', 'amount_sap',
                                             'LEGACY employee number', 'LEGACY wage type', 'amount_legacy']]

        # Format for display
        filtered_results.reset_index(drop=True, inplace=True)
        filtered_results.index += 1  # Start index at 1

        return render_template('results.html', results=filtered_results.to_html())

    return render_template('data_comparisonECP.html')

# ==============================================
# VARIANCE MONITOR ROUTES
# ==============================================

@app.route('/variance_monitor_page', methods=['GET', 'POST'])
def variance_monitor_page():
    """
    Variance monitoring tool
    Handles both GET (display form) and POST (process files)
    """
    if request.method == 'POST':
        # Save uploaded files temporarily
        legacy_file = request.files['legacyPayrollFile']
        sap_file = request.files['sapPayrollFile']
        mapping_file = request.files['mappingFile']

        legacy_path = os.path.join(app.config['TEMP_FOLDER'], legacy_file.filename)
        sap_path = os.path.join(app.config['TEMP_FOLDER'], sap_file.filename)
        mapping_path = os.path.join(app.config['TEMP_FOLDER'], mapping_file.filename)

        legacy_file.save(legacy_path)
        sap_file.save(sap_path)
        mapping_file.save(mapping_path)

        # Store paths in session for next step
        session['legacy_file'] = legacy_path
        session['sap_file'] = sap_path
        session['mapping_file'] = mapping_path

        # Get column names for selection
        df = pd.read_excel(legacy_file)
        column_names = df.columns.tolist()

        return render_template('variance_monitor_selection.html', columns=column_names)

    return render_template('variance_monitor_page.html')

@app.route('/process_variance_selection', methods=['POST'])
def process_variance_selection():
    """
    Process variance monitoring with user-selected options
    """
    # Retrieve stored file paths
    legacy_path = session.get('legacy_file')
    sap_path = session.get('sap_file')
    mapping_path = session.get('mapping_file')

    if not (legacy_path and sap_path and mapping_path):
        return "File information is missing. Please start over.", 400

    print("got files")  # Debug output

    # Get user selections
    comparison = request.form['comparison']
    percentage = request.form.get('percentage')
    print("got selections")  # Debug output

    if comparison == 'percentage':
        percentage = float(percentage)
        if not (0 < percentage < 100):
            return "Invalid percentage value. Please enter a number between 0 and 100.", 400
    print("correct percentage")  # Debug output

    if comparison == 'exact' or comparison == 'percentage':
        # Helper function to read Excel with consistent typing
        def read_excel_file(file):
            return pd.read_excel(file, dtype={'LEGACY employee number': str, 'SAP employee number': str})

        try:
            # Read all input files
            legacy_df = read_excel_file(legacy_path)
            sap_df = read_excel_file(sap_path)
            mapping_df = read_excel_file(mapping_path)
        except Exception as e:
            return f"Error reading files: {e}", 400

        print("files read successfully")  # Debug output

        # Create wage type mapping
        wage_type_mapping = dict(zip(mapping_df['LEGACY'], mapping_df['SAP']))

        # Summarize SAP data
        sap_summary = (sap_df
                       .groupby(['SAP employee number', 'SAP wage type'])
                       ['SAP amount'].sum().reset_index()
                       .rename(columns={'SAP amount': 'amount_sap'}))

        # Summarize legacy data
        legacy_summary = (legacy_df
                          .groupby(['LEGACY employee number', 'LEGACY wage type'])
                          ['LEGACY amount'].sum().reset_index()
                          .rename(columns={'LEGACY amount': 'amount_legacy'}))

        # Map legacy wage types to SAP
        legacy_summary['SAP wage type mapped'] = legacy_summary['LEGACY wage type'].map(wage_type_mapping)

        # Merge datasets
        merged_results = pd.merge(
            legacy_summary,
            sap_summary,
            left_on=['LEGACY employee number', 'SAP wage type mapped'],
            right_on=['SAP employee number', 'SAP wage type'],
            how='outer'
        )

        # Calculate differences
        merged_results['difference'] = merged_results['amount_legacy'].fillna(0) - merged_results['amount_sap'].fillna(0)
        merged_results['percentage_difference'] = np.where(
            merged_results['amount_sap'].fillna(0) == 0,
            100,  # Handle division by zero
            (merged_results['difference'] / merged_results['amount_sap'].fillna(0)) * 100
        )
        merged_results['percentage_difference'] = merged_results['percentage_difference'].abs().astype(int)

        # Filter to only show differences
        filtered_results = merged_results[merged_results['difference'] != 0].fillna('Missing')

        # Prepare final columns
        filtered_results = filtered_results[['SAP employee number', 'SAP wage type', 'amount_sap',
                                             'LEGACY employee number', 'LEGACY wage type', 'amount_legacy', 'difference',
                                             'percentage_difference']]

        # Format for display
        filtered_results.reset_index(drop=True, inplace=True)
        filtered_results.index += 1

        if comparison == 'percentage':
            print("gotta colour code!!!1")  # Debug output
            print(percentage)  # Debug output
        else:
            percentage = 100
        percentage = int(percentage)

        return render_template('results_VM.html',
                               difference_results=filtered_results[['SAP employee number', 'SAP wage type', 'amount_sap',
                                                                    'LEGACY employee number', 'LEGACY wage type', 'amount_legacy', 'difference', 'percentage_difference']].to_dict(orient='records'),
                               percentage_results=filtered_results[['SAP employee number', 'SAP wage type', 'amount_sap',
                                                                    'LEGACY employee number', 'LEGACY wage type', 'amount_legacy', 'percentage_difference']].to_dict(orient='records'),
                               threshold=percentage)

    return f"Processing {comparison} comparison with percentage {percentage if percentage else 'N/A'}."

# ==============================================
# STATISTICS AND VALIDATION ROUTES
# ==============================================

@app.route('/validation/statistics', methods=['GET', 'POST'])
def validation_statistics():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'validation', filename)
            ensure_one_directory_exists('validation')
            file.save(filepath)

            data = pd.read_excel(filepath)

            row_count = data.shape[0]
            column_count = data.shape[1]
            missing_values = data.isnull().sum()
            numeric_summary = data.describe(include=[np.number]).to_html()

            numeric_columns = data.select_dtypes(include=[np.number]).columns
            categorical_columns = data.select_dtypes(exclude=[np.number]).columns

            plot_images = []

            for column in numeric_columns:
                fig, ax = plt.subplots()
                data[column].plot(kind='hist', ax=ax, title=f'Distribution of {column}')
                img = io.BytesIO()
                plt.savefig(img, format='png')
                img.seek(0)
                img_data = base64.b64encode(img.read()).decode('utf-8')
                plot_images.append({'column': column, 'img_data': img_data})
                plt.close()

            for column in categorical_columns:
                fig, ax = plt.subplots()
                data[column].value_counts().plot(kind='bar', ax=ax, title=f'Value counts of {column}')
                img = io.BytesIO()
                plt.savefig(img, format='png')
                img.seek(0)
                img_data = base64.b64encode(img.read()).decode('utf-8')
                plot_images.append({'column': column, 'img_data': img_data})
                plt.close()

            return render_template('statistics_result.html',
                                   row_count=row_count,
                                   column_count=column_count,
                                   missing_values=missing_values.to_dict(),
                                   numeric_summary=numeric_summary,
                                   plot_images=plot_images)

    return render_template('upload_statistics.html')


@app.route('/validation/comparison', methods=['GET', 'POST'])
def validation_comparison():
    if request.method == 'POST':
        loadsheet = request.files['loadsheet']
        extracted = request.files['extracted']

        if loadsheet and allowed_file(loadsheet.filename) and extracted and allowed_file(extracted.filename):
            filename1 = secure_filename(loadsheet.filename)
            filename2 = secure_filename(extracted.filename)

            folder_path = os.path.join(app.config['UPLOAD_FOLDER'], 'comparison')
            ensure_one_directory_exists(folder_path)

            filepath1 = os.path.join(folder_path, filename1)
            filepath2 = os.path.join(folder_path, filename2)

            loadsheet.save(filepath1)
            extracted.save(filepath2)

            data1 = pd.read_excel(filepath1)
            data2 = pd.read_excel(filepath2)

            data1 = data1.fillna('')
            data2 = data2.fillna('')

            data2_reordered = data2.reindex(columns=data1.columns)

            unique_in_loadsheet = data1[~data1.apply(tuple, axis=1).isin(data2_reordered.apply(tuple, axis=1))]
            unique_in_extracted = data2_reordered[~data2_reordered.apply(tuple, axis=1).isin(data1.apply(tuple, axis=1))]

            stats = {
                'loadsheet_rows': data1.shape[0],
                'extracted_rows': data2.shape[0],
                'loadsheet_columns': len(data1.columns),
                'extracted_columns': len(data2.columns),
            }

            return render_template('comparison_result.html', stats=stats,
                                   unique_in_loadsheet=unique_in_loadsheet,
                                   unique_in_extracted=unique_in_extracted)

    return render_template('upload_comparison.html')


# ==============================================
# FILE DOWNLOAD ROUTES
# ==============================================

@app.route('/download/<filename>')
def download(filename):
    """Serve comparison result files for download"""
    return send_from_directory(os.path.join(app.config['UPLOAD_FOLDER'], 'comparison'), filename)

# ==============================================
# EMPLOYEE DATA VALIDATION ROUTES
# ==============================================

@app.route('/validate_source_extracts/<category>', methods=['GET'])
def validate_source_extracts(category):
    """Display employee data validation interface"""
    return render_template('validate_source_extracts.html', category=category)

def analyze_employee_data(base_file_name, employee_number_var):
    """
    Analyze employee data across multiple files
    Identifies missing employee numbers compared to base file
    """
    directory = os.path.join(app.config['UPLOAD_FOLDER'], 'employee', 'source_extracts')
    base_file_path = os.path.join(directory, base_file_name)
    base_df = pd.read_excel(base_file_path)
    unique_employee_numbers_base = set(base_df[employee_number_var])

    results = {}

    def get_unique_employee_numbers(df):
        """Helper to get unique employee numbers from a dataframe"""
        return set(df[employee_number_var])

    for file_name in os.listdir(directory):
        if file_name.endswith('.xlsx') and file_name != base_file_name:
            current_df = pd.read_excel(os.path.join(directory, file_name))
            unique_employee_numbers_current = get_unique_employee_numbers(current_df)
            missing_employee_numbers = list(unique_employee_numbers_base - unique_employee_numbers_current)

            results[file_name] = {
                'num_rows': len(current_df),
                'missing_employee_numbers': missing_employee_numbers
            }

    return results

@app.route('/perform_validation/<category>', methods=['POST'])
def perform_validation(category):
    """
    Execute employee data validation and display results
    """
    base_file_name = request.form['base_file_name']
    employee_number_var = request.form['employee_number_var']
    results = analyze_employee_data(base_file_name, employee_number_var)
    return render_template('validation_results.html', category=category, results=results)

# ==============================================
# PAYROLL COUNTRY-SPECIFIC ROUTES
# ==============================================

def ensure_directory_existspay(category, folder_type):
    """Ensure payroll directories exist (country-specific)"""
    directory = os.path.join(category, folder_type)
    os.makedirs(directory, exist_ok=True)

# Canada payroll routes
@app.route('/datamigpayroll/upload-source-extracts_canada', methods=['GET', 'POST'])
def upload_source_extracts_canada():
    """Handle Canada payroll source extract uploads"""
    ensure_directory_existspay('CANADA', 'source_extracts')

    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config["CANADA_FOLDER"], 'source_extracts', filename))
            return redirect(url_for('view_source_extracts_canada'))

    return render_template('upload_source_extracts_canada.html')

@app.route('/datamigpayroll/view-source-extracts_canada')
def view_source_extracts_canada():
    """View Canada payroll source extracts"""
    source_extracts_dir = os.path.join(app.config["CANADA_FOLDER"], 'source_extracts')
    files = os.listdir(source_extracts_dir) if os.path.exists(source_extracts_dir) else []
    return render_template('view_source_extracts_canada.html', files=files)

@app.route('/datamigpayroll/delete-source-extracts_canada/<filename>', methods=['POST'])
def delete_source_extracts_canada(filename):
    """Delete Canada payroll source extract"""
    source_extracts_dir = os.path.join(app.config["CANADA_FOLDER"], 'source_extracts')
    file_path = os.path.join(source_extracts_dir, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    return redirect(url_for('view_source_extracts_canada'))

# Similar routes for US and Australia payroll...
# [Previous country-specific routes maintained exactly as is...]

# ==============================================
# PAYROLL LOADSHEET GENERATION ROUTES
# ==============================================

@app.route('/datamigpayroll/create-loadsheets-canada', methods=['GET', 'POST'])
def create_loadsheets_canada():
    """Generate Canada payroll loadsheets"""
    # Execute processing scripts
    scripts = ['code.py', 'allfiles.py', 'amtspecific.py']
    for script in scripts:
        script_path = os.path.join(app.config["CANADA_FOLDER"], 'code', script)
        print(script_path)  # Debug output
        try:
            result = subprocess.run(['python', script_path], capture_output=True, text=True, check=True)
            print(result.stdout)  # Debug output
        except subprocess.CalledProcessError as e:
            print(e.stderr)  # Debug output
        except Exception as e:
            print(f"Unexpected error: {str(e)}")  # Debug output

    # Get resulting files
    source_extracts_dir = os.path.join(app.config["CANADA_FOLDER"], 'target')
    print(source_extracts_dir)  # Debug output
    files = os.listdir(source_extracts_dir) if os.path.exists(source_extracts_dir) else []
    print(files)  # Debug output
    return render_template('create_loadsheets_canada.html', files=files)



# ==============================================
# PAYROLL FILE SERVING ROUTES
# ==============================================

@app.route('/datamigpayroll/source-extracts/<filename>')
def uploaded_file_canada(filename):
    """Serve Canada payroll source extract"""
    return send_from_directory(os.path.join(app.config["CANADA_FOLDER"], 'source_extracts'), filename)

@app.route('/datamigpayroll/workbooks_canada/<filename>')
def workbook_file_canada(filename):
    """Serve Canada payroll workbook"""
    return send_from_directory(os.path.join(app.config["CANADA_FOLDER"], 'workbooks'), filename)

@app.route('/loadsheet_file_canada/<filename>')
def loadsheet_file_canada(filename):
    """Serve Canada payroll loadsheet"""
    return send_from_directory(os.path.join(app.config["CANADA_FOLDER"], 'target'), filename)

# ==============================================
# AUSTRALIA PAYROLL ROUTES (same pattern as Canada/US)
# ==============================================

@app.route('/datamigpayroll/upload-source-extracts_aus', methods=['GET', 'POST'])
def upload_source_extracts_aus():
    """
    Handle Australia payroll source extract file uploads
    Same functionality as Canada/US but for Australia
    """
    ensure_directory_existspay('AUS', 'source_extracts')

    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['AUS_FOLDER'], 'source_extracts', filename))
            print(os.path.join(app.config['AUS_FOLDER'], 'source_extracts', filename))  # Debug file path
            return redirect(url_for('view_source_extracts_aus'))

    return render_template('upload_source_extracts_aus.html')

@app.route('/datamigpayroll/view-source-extracts_aus')
def view_source_extracts_aus():
    """
    Display list of uploaded Australia payroll source extracts
    Same functionality as Canada/US but for Australia
    """
    source_extracts_dir = os.path.join(app.config['AUS_FOLDER'], 'source_extracts')
    print(source_extracts_dir)  # Debug directory path
    files = os.listdir(source_extracts_dir) if os.path.exists(source_extracts_dir) else []
    return render_template('view_source_extracts_aus.html', files=files)

@app.route('/datamigpayroll/delete-source-extracts_aus/<filename>', methods=['POST'])
def delete_source_extracts_aus(filename):
    """
    Delete an Australia payroll source extract file
    Same functionality as Canada/US but for Australia
    """
    source_extracts_dir = os.path.join(app.config['AUS_FOLDER'], 'source_extracts')
    file_path = os.path.join(source_extracts_dir, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    return redirect(url_for('view_source_extracts_aus'))

@app.route('/datamigpayroll/upload-workbook_aus', methods=['GET', 'POST'])
def upload_workbook_aus():
    """
    Handle Australia payroll workbook file uploads
    Same functionality as Canada/US but for Australia
    """
    ensure_directory_existspay('AUS', 'workbooks')

    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['AUS_FOLDER'], 'workbooks', filename))
            return redirect(url_for('view_workbooks_aus'))

    return render_template('upload_workbook_aus.html')

@app.route('/datamigpayroll/view-workbooks_aus')
def view_workbooks_aus():
    """
    Display list of uploaded Australia payroll workbooks (.xlsx only)
    Same functionality as Canada/US but for Australia
    """
    workbooks_dir = os.path.join(app.config['AUS_FOLDER'], 'workbooks')
    files = [f for f in os.listdir(workbooks_dir) if f.endswith('.xlsx')] if os.path.exists(workbooks_dir) else []
    return render_template('view_workbooks_aus.html', files=files)

@app.route('/datamigpayroll/delete-workbooks/<filename>', methods=['POST'])
def delete_workbook_aus(filename):
    """
    Delete an Australia payroll workbook file
    Same functionality as Canada/US but for Australia
    """
    workbooks_dir = os.path.join(app.config['AUS_FOLDER'], 'workbooks')
    file_path = os.path.join(workbooks_dir, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    return redirect(url_for('view_workbooks_aus'))

@app.route('/datamigpayroll/create-loadsheets-aus', methods=['GET', 'POST'])
def create_loadsheets_aus():
    """
    Generate Australia payroll loadsheets by executing processing scripts
    Same pattern as Canada/US but with Australia-specific processing
    """
    # Execute Australia-specific processing scripts
    scripts = ['code.py', 'allfiles.py', 'amtspecific.py']
    for script in scripts:
        script_path = os.path.join(app.config['AUS_FOLDER'], 'code', script)
        print(script_path)  # Debug script path
        try:
            result = subprocess.run(['python', script_path], capture_output=True, text=True, check=True)
            output = result.stdout
        except subprocess.CalledProcessError as e:
            output = f"Error occurred: {e.stderr}"
            print(e.stderr)  # Debug error
        except Exception as e:
            output = f"Unexpected error: {str(e)}"
            print(f"Unexpected error: {output}")  # Debug error

    # Get resulting files
    source_extracts_dir = os.path.join(app.config['AUS_FOLDER'], 'target')
    print(source_extracts_dir)  # Debug directory
    files = os.listdir(source_extracts_dir) if os.path.exists(source_extracts_dir) else []
    return render_template('create_loadsheets_aus.html', files=files)

@app.route('/datamigpayroll/source-extracts/<filename>')
def uploaded_file_aus(filename):
    """
    Serve Australia payroll source extract file for download
    Same functionality as Canada/US but for Australia
    """
    return send_from_directory(os.path.join(app.config["AUS_FOLDER"], 'source_extracts'), filename)

@app.route('/datamigpayroll/workbooks_aus/<filename>')
def workbook_file_aus(filename):
    """
    Serve Australia payroll workbook file for download
    Same functionality as Canada/US but for Australia
    """
    return send_from_directory(os.path.join(app.config["AUS_FOLDER"], 'workbooks'), filename)

@app.route('/loadsheet_file_aus/<filename>')
def loadsheet_file_aus(filename):
    """
    Serve generated Australia payroll loadsheet file for download
    Same functionality as Canada/US but for Australia
    """
    print(os.path.join(app.config["AUS_FOLDER"], 'target'))  # Debug directory
    print(filename)  # Debug filename
    return send_from_directory(os.path.join(app.config["AUS_FOLDER"], 'target'), filename)

# ==============================================
# US PAYROLL ROUTES (same pattern as Canada/Australia)
# ==============================================

@app.route('/datamigpayroll/upload-source-extracts_us', methods=['GET', 'POST'])
def upload_source_extracts_us():
    """
    Handle US payroll source extract file uploads
    Same functionality as Canada/Australia but for US
    """
    ensure_directory_existspay('US', 'source_extracts')

    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['US_FOLDER'], 'source_extracts', filename))
            return redirect(url_for('view_source_extracts_us'))

    return render_template('upload_source_extracts_us.html')

@app.route('/datamigpayroll/view-source-extracts_us')
def view_source_extracts_us():
    """
    Display list of uploaded US payroll source extracts
    Same functionality as Canada/Australia but for US
    """
    source_extracts_dir = os.path.join(app.config['US_FOLDER'], 'source_extracts')
    print(source_extracts_dir)  # Debug directory path
    files = os.listdir(source_extracts_dir) if os.path.exists(source_extracts_dir) else []
    return render_template('view_source_extracts_us.html', files=files)

@app.route('/datamigpayroll/delete-source-extracts_us/<filename>', methods=['POST'])
def delete_source_extracts_us(filename):
    """
    Delete a US payroll source extract file
    Same functionality as Canada/Australia but for US
    """
    source_extracts_dir = os.path.join(app.config['US_FOLDER'], 'source_extracts')
    file_path = os.path.join(source_extracts_dir, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    return redirect(url_for('view_source_extracts_us'))

@app.route('/datamigpayroll/upload-workbook_us', methods=['GET', 'POST'])
def upload_workbook_us():
    """
    Handle US payroll workbook file uploads
    Same functionality as Canada/Australia but for US
    """
    ensure_directory_existspay('US', 'workbooks')

    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['US_FOLDER'], 'workbooks', filename))
            return redirect(url_for('view_workbooks_us'))

    return render_template('upload_workbook_us.html')

@app.route('/datamigpayroll/view-workbooks_us')
def view_workbooks_us():
    """
    Display list of uploaded US payroll workbooks (.xlsx only)
    Same functionality as Canada/Australia but for US
    """
    workbooks_dir = os.path.join(app.config['US_FOLDER'], 'workbooks')
    files = [f for f in os.listdir(workbooks_dir) if f.endswith('.xlsx')] if os.path.exists(workbooks_dir) else []
    return render_template('view_workbooks_us.html', files=files)

@app.route('/datamigpayroll/delete-workbooks/<filename>', methods=['POST'])
def delete_workbook_us(filename):
    """
    Delete a US payroll workbook file
    Same functionality as Canada/Australia but for US
    """
    workbooks_dir = os.path.join(app.config['US_FOLDER'], 'workbooks')
    file_path = os.path.join(workbooks_dir, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    return redirect(url_for('view_workbooks_us'))

@app.route('/datamigpayroll/create-loadsheets-us', methods=['GET', 'POST'])
def create_loadsheets_us():
    """
    Generate US payroll loadsheets by executing processing scripts
    Same pattern as Canada/Australia but with US-specific processing
    Includes additional US-specific script
    """
    # Execute US-specific processing scripts
    scripts = ['code.py', 'allfiles.py', 'amtspecific.py', 'usspecific.py']
    for script in scripts:
        script_path = os.path.join(app.config['US_FOLDER'], 'code', script)
        print(script_path)  # Debug script path
        try:
            result = subprocess.run(['python', script_path], capture_output=True, text=True, check=True)
            output = result.stdout
        except subprocess.CalledProcessError as e:
            output = f"Error occurred: {e.stderr}"
            print(e.stderr)  # Debug error
        except Exception as e:
            output = f"Unexpected error: {str(e)}"
            print(f"Unexpected error: {output}")  # Debug error

    # Get resulting files
    source_extracts_dir = os.path.join(app.config['US_FOLDER'], 'target')
    print(source_extracts_dir)  # Debug directory
    files = os.listdir(source_extracts_dir) if os.path.exists(source_extracts_dir) else []
    return render_template('create_loadsheets_us.html', files=files)

@app.route('/datamigpayroll/source-extracts-us/<filename>')
def uploaded_file_us(filename):
    """
    Serve US payroll source extract file for download
    Same functionality as Canada/Australia but for US
    """
    print(os.path.join(app.config["US_FOLDER"], 'source_extracts'), filename)  # Debug path
    return send_from_directory(os.path.join('US', 'source_extracts'), filename)

@app.route('/datamigpayroll/workbooks_us/<filename>')
def workbook_file_us(filename):
    """
    Serve US payroll workbook file for download
    Same functionality as Canada/Australia but for US
    """
    return send_from_directory(os.path.join(app.config["US_FOLDER"], 'workbooks'), filename)

@app.route('/loadsheet_file_us/<filename>')
def loadsheet_file_us(filename):
    """
    Serve generated US payroll loadsheet file for download
    Same functionality as Canada/Australia but for US
    """
    return send_from_directory(os.path.join(app.config["US_FOLDER"], 'target'), filename)

# ==============================================
# CHATBOT ROUTES
# ==============================================

@app.route('/chat', methods=['POST'])
def chat():
    try:
        logger.info(f"Chat request received from user: {session.get('username', 'unknown')}")

        if not request.is_json:
            logger.error("Request is not JSON")
            return jsonify({
                'response': "Invalid request format",
                'timestamp': datetime.now().strftime('%H:%M'),
                'error': True
            }), 400

        message = request.json.get('message', '')
        if not message:
            logger.error("Empty message received")
            return jsonify({
                'response': "No message received",
                'timestamp': datetime.now().strftime('%H:%M'),
                'error': True
            }), 400

        logger.info(f"Sending message to OpenAI: {message[:50]}...")
        logger.info("Making OpenAI API call...")
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": """You are a helpful assistant for a Data Migration Tool. 
                You help users with:
                1. Data Migration:
                   - Foundation data migration
                   - Position data migration
                   - Employee data migration
                   - Payroll data migration for US, Canada, and Australia
                2. File Management:
                   - Upload source extracts
                   - Upload workbooks
                   - View and manage uploaded files
                3. Validation:
                   - Data validation features
                   - Source data validation
                   - Loadsheet validation
                Keep responses concise and friendly. If unsure, guide users to the appropriate section of the tool."""},
                {"role": "user", "content": message}
            ],
            store=True
        )

        response = completion.choices[0].message.content
        logger.info(f"Extracted response: {response}")

        return jsonify({
            'response': response,
            'timestamp': datetime.now().strftime('%H:%M'),
            'error': False
        })

    except Exception as e:
        logger.error(f"Unexpected error in chat route: {str(e)}", exc_info=True)
        logger.error(f"Full error details: {e.__dict__}")
        return jsonify({
            'response': "I apologize, but I'm experiencing technical difficulties. Please try again later.",
            'timestamp': datetime.now().strftime('%H:%M'),
            'error': True
        }), 500


# ==============================================
# APPLICATION STARTUP
# ==============================================

if __name__ == '__main__':
    # Ensure base directory exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    # Start application on port 8080
    app.run(host='0.0.0.0', port=8080, debug=False, use_reloader=False)

# Support01$