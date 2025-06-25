# SAP EC Migration & Monitoring Tool

A demo dashboard for accelerating Employee Central migrations with built-in validation and variance monitoring — built using Streamlit.

## Features
- Field-level variance detection
- Template-based EC migrations
- Pre-Go Live validations

## Run Locally

1. Clone the repo  
2. Install dependencies:  
   `pip install -r requirements.txt`  
3. Run the app:  
   `streamlit run app.py`

## Run with Docker

```bash
docker build -t sap-tool .
docker run -p 8501:8501 sap-tool
