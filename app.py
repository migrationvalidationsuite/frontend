import streamlit as st
from PIL import Image
import os

# Set page config
st.set_page_config(page_title="Quantumela: SAP EC Migration Tool", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Home", "Solutions", "Data Migration", "Validation", "Variance Monitoring"])

# Image path utility
def load_image(name):
    return os.path.join("assets", "images", name)

# --- HOME ---
if page == "Home":
    st.image(load_image("homepage_banner.png"), use_container_width=True)
    st.title("Quantumela: SAP Employee Central Migration & Monitoring Suite")
    st.subheader("Accelerate SAP EC transitions with data integrity, speed, and confidence.")
    st.markdown("""
    Welcome to Quantumela's streamlined migration and variance platform built for seamless SAP EC deployment.  
    Explore our tools to ensure **accurate data migration**, **validated payrolls**, and **minimal disruption** to operations.
    """)

# --- SOLUTIONS OVERVIEW ---
elif page == "Solutions":
    st.header("Solutions Overview")
    st.markdown("""
    Quantumela provides an integrated toolkit for SAP EC data workflows:
    - 🔁 **Data Migration**: Clean, map, and migrate EC-relevant data objects.
    - ✅ **Validation**: Automate checks and parallel testing to ensure accuracy.
    - 📊 **Variance Monitoring**: Visualize and track key changes between pre/post migration states.
    """)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(load_image("employee_central_migration.png"), caption="Employee Central Migration", use_container_width=True)
    with col2:
        st.image(load_image("validation_lifecycle.png"), caption="Validation Lifecycle", use_container_width=True)
    with col3:
        st.image(load_image("variance_monitoring_workflow.png"), caption="Variance Monitoring Flow", use_container_width=True)

# --- DATA MIGRATION ---
elif page == "Data Migration":
    st.header("Data Migration Services")
    st.markdown("""
    Our migration module allows you to:
    - Transform employee master data and structure.
    - Extract from legacy systems and prepare for EC upload.
    - Create formatted files based on SAP data object mapping.

    Ensure readiness before cutover through stepwise staging and extraction reviews.
    """)
    st.image(load_image("employee_central_migration.png"), caption="Data Migration Diagram", use_container_width=True)

# --- VALIDATION ---
elif page == "Validation":
    st.header("Validation Framework")
    st.markdown("""
    Validation tools compare legacy vs EC migrated records using:
    - Parallel run payroll comparisons
    - Object-by-object discrepancy detection
    - Visual lifecycle tracking for approvals

    This ensures **zero-data-loss** and audit-aligned accuracy.
    """)
    st.image(load_image("validation_lifecycle.png"), caption="Validation Lifecycle", use_container_width=True)

# --- VARIANCE MONITORING ---
elif page == "Variance Monitoring":
    st.header("Variance Monitoring")
    st.markdown("""
    Monitor key attributes such as pay group, cost center, compensation, or position assignments pre and post-migration:
    - Real-time reports of mismatches
    - Alerting thresholds
    - Exportable logs

    Visualize what changed, when, and why—so there are no surprises post-GoLive.
    """)
    st.image(load_image("variance_monitoring_workflow.png"), caption="Variance Monitoring Flow", use_container_width=True)
