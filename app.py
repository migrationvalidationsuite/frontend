import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="SAP EC Migration & Monitoring",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="auto"
)

# Optional CSS Styling
# Commenting out unless file provided
# with open("styles.css") as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- NAVIGATION MENU ---
selected = option_menu(
    menu_title=None,
    options=["Home", "Solutions", "Services"],
    icons=["house-door-fill", "layers-fill", "tools"],
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#f0f4f8"},
        "nav-link": {"font-size": "18px", "font-weight": "600", "color": "#003366", "margin": "0 20px"},
        "nav-link-selected": {"background-color": "#cce0ff", "border-radius": "8px"},
    }
)

# --- HOME PAGE ---
if selected == "Home":
    st.markdown("## Accelerate Your SAP Employee Central Migration")
    st.markdown("""
        #### Purpose-built migration, validation and variance monitoring to make your SAP HCM transformation effortless.
    """)
    st.image("landing_hero.png", use_container_width=True)

    st.markdown("---")
    st.subheader("Why Choose Our Tool?")
    st.markdown("""
    - Seamless data transformation with clean templates and rollback support
    - Built-in validation engine to ensure data quality before upload
    - Intelligent variance reports across legacy ECC and SAP EC
    - Designed for payroll-critical data, minimizing business disruptions
    """)
    st.markdown("Explore the 'Solutions' tab above for a detailed walkthrough.")

# --- SOLUTIONS PAGE ---
elif selected == "Solutions":
    sol_choice = option_menu(
        menu_title="Our Solutions",
        options=["Data Migration", "Validation", "Variance Monitoring"],
        icons=["cloud-upload", "check2-square", "bar-chart"],
        orientation="horizontal"
    )

    if sol_choice == "Data Migration":
        col1, col2 = st.columns([1.2, 1])
        with col1:
            st.header("Employee Central Data Migration")
            st.markdown("""
            Migrating from SAP ECC or other systems to EC? Our platform supports:

            - Foundation Object Migration: Legal Entity, Business Unit, Location, Cost Center
            - Position & Job Info Mapping: Custom hierarchies and structures
            - Employee Master Data Uploads: Core data, job info, compensation, time & benefits

            **Capabilities:**
            - Role-based access and traceable logs
            - Error highlighting before transformation
            - Upload-ready SAP-compatible output files
            """)
        with col2:
            st.image("Employee_Central_Data_Migration.png", use_container_width=True)

    elif sol_choice == "Validation":
        col1, col2 = st.columns([1.2, 1])
        with col1:
            st.header("Validation Services")
            st.markdown("""
            Ensure your data adheres to SAP EC standards:

            - Format checks (date/time, strings, enumerations)
            - Field constraints and required value enforcement
            - Referential validations (e.g., manager exists, org units align)

            **Why it matters:**
            - Prevent upload failures
            - Ensure reporting & compliance accuracy
            - Reduce costly rework and post-Go Live delays
            """)
        with col2:
            st.image("validation_lifecycle.png", use_container_width=True)

    elif sol_choice == "Variance Monitoring":
        col1, col2 = st.columns([1.2, 1])
        with col1:
            st.header("ECC to EC Variance Monitoring")
            st.markdown("""
            Post-migration? This tool compares pre/post data for:

            - Field-level mismatches in values and formats
            - Missing or extra records across modules
            - Logic and configuration mismatches (infotype vs MDF)

            **Key Benefits:**
            - Granular insights into payroll-critical variances
            - Audit-ready documentation
            - Visual summary dashboards
            """)
        with col2:
            st.image("variance_monitoring.png", use_container_width=True)

# --- SERVICES PAGE ---
elif selected == "Services":
    st.header("SAP EC Transformation Services")
    st.markdown("""
    Our team supports full lifecycle SAP EC implementations:

    - Project scoping, feasibility and fit-gap assessments
    - Data audit, cleansing, enrichment and mapping strategy
    - EC configuration and upload file generation
    - Multi-round validations and data harmonization
    - Pre-Go Live reconciliations and post-load fixes

    **We specialize in:**
    - Fast-track migrations for payroll or compliance-driven timelines
    - Parallel test phase support
    - Change tracking and variance auditing

    We deliver not just a migration tool — but an end-to-end framework tailored to SAP HCM and EC best practices.
    """)
