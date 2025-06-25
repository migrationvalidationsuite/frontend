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
    st.markdown("#### Purpose-built migration, validation and variance monitoring to make your SAP HCM transformation effortless.")
    st.image("landing_hero.png", use_container_width=True)

    # New SAP-aligned banner section
    with st.container():
        st.markdown("""
            <div style='background-color:#0f1b4c;padding:50px;border-radius:8px;color:white'>
                <h2 style='text-align:center;'>Built for SAP & SuccessFactors</h2>
                <p style='text-align:center; font-size:16px;'>
                    Our solutions are purpose-built for SAP SuccessFactors and SAP S/4HANA environments.<br>
                    Whether you're migrating from ECC or optimizing existing EC setups, we deliver tools that support compliance, performance, and confidence at scale.
                </p>
                <br>
                <div style='display:flex;justify-content:space-around;gap:30px;flex-wrap:wrap;'>
                    <div style='flex:1;min-width:250px;'>
                        <h4>EC Data Migration & Implementation Services</h4>
                        <p>Streamline Employee Central migrations using best-practice templates, transformation rules, and rollback-safe utilities.</p>
                    </div>
                    <div style='flex:1;min-width:250px;'>
                        <h4>Payroll Validation & Compliance Automation</h4>
                        <p>Run pre-Go Live validations across all HR/payroll master data to catch and correct errors before they disrupt cutover.</p>
                    </div>
                    <div style='flex:1;min-width:250px;'>
                        <h4>Variance Monitoring & Audit Reporting</h4>
                        <p>Track EC vs ECC mismatches and field-level differences with dashboards that enable rapid triage and correction.</p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Why Choose Our Tool?")
    st.markdown("""
    - Seamless Data Transformation: Map, cleanse, and migrate with accuracy  
    - Built-in Validation: Eliminate bad data before it hits production  
    - Variance Detection: Compare ECC and EC data at a granular level  
    """)



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
