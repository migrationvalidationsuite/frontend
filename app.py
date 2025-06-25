import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="SAP EC Migration & Monitoring",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="auto"
)

# Optional CSS Styling
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

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
    - Seamless data transformation with structured templates and logic mapping
    - Built-in validation to prevent corrupt or non-compliant entries
    - Variance detection to ensure migration accuracy across systems
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
        col1, col2 = st.columns([1, 1])
        with col1:
            st.header("Employee Central Data Migration")
            st.markdown("""
            Our migration module handles object-by-object transformations, including:

            - Foundation Objects: Legal entities, business units, geographies, cost centers
            - Position Management: Parent-child hierarchy setup with reporting lines
            - Employee Master Data: Demographics, roles, compensation, time profiles

            Highlights:
            - Transformation logic for legacy fields into EC-compatible formats
            - Pre-load and post-load reconciliation templates
            - Change audit logs and rollback utilities
            - Supports phased or big-bang go-live models
            """)
        with col2:
            st.image("Employee_Central_Data_Migration.png", use_container_width=True)
            st.markdown("""
            <iframe width="100%" height="400" src="https://datastudio.google.com/embed/reporting/1examplepage" frameborder="0" style="border:0" allowfullscreen></iframe>
            """, unsafe_allow_html=True)

    elif sol_choice == "Validation":
        col1, col2 = st.columns([1, 1])
        with col1:
            st.header("Data Validation Services")
            st.markdown("""
            Our validation module ensures migration files comply with SAP EC load expectations:

            - Schema alignment with SuccessFactors templates
            - Null checks, data type enforcement, and regex-based pattern rules
            - Lookup validation across dependent objects (e.g., cost center match)

            Features:
            - Smart rules engine for reusable data quality checks
            - Issue severity scoring (Critical / Warning / Info)
            - Error summary exports (CSV/PDF)
            - Revalidation support after fixes
            """)
        with col2:
            st.image("validation_lifecycle.png", use_container_width=True)
            st.markdown("""
            <iframe width="100%" height="400" src="https://datastudio.google.com/embed/reporting/2examplepage" frameborder="0" style="border:0" allowfullscreen></iframe>
            """, unsafe_allow_html=True)

    elif sol_choice == "Variance Monitoring":
        col1, col2 = st.columns([1, 1])
        with col1:
            st.header("ECC to EC Variance Monitoring")
            st.markdown("""
            Post-migration, our comparison utility detects:

            - Value-level discrepancies between ECC exports and EC staging loads
            - Field formatting mismatches (date formats, number precision)
            - Records missing or duplicated between source/target

            Capabilities:
            - Side-by-side field comparison viewer
            - Filter by object type, date range, or issue type
            - Downloadable variance report with tags (Resolved / Unresolved)
            - Supports integrations into Power BI / Excel dashboards
            """)
        with col2:
            st.image("variance_monitoring.png", use_container_width=True)
            st.markdown("""
            <iframe width="100%" height="400" src="https://datastudio.google.com/embed/reporting/3examplepage" frameborder="0" style="border:0" allowfullscreen></iframe>
            """, unsafe_allow_html=True)

# --- SERVICES PAGE ---
elif selected == "Services":
    st.header("End-to-End SAP HCM Migration Services")
    st.markdown("""
    We offer hands-on assistance and strategic consulting through each phase:

    **1. Migration Planning**
    - Readiness checks and stakeholder interviews
    - Object prioritization and scoping roadmap

    **2. Data Design & Cleansing**
    - Legacy data profiling and normalization
    - Gap analysis and enrichment recommendations

    **3. Configuration & Conversion**
    - Field mapping documents
    - EC template population and bulk loaders

    **4. Validation & Testing**
    - Smart rules, sample audits, UAT test packs
    - Parallel payroll runs and historical loads

    **5. Go-Live Support & Variance Tracking**
    - Final load dry runs
    - Issue dashboards and cutover QA

    → We tailor our delivery approach based on your internal capability and migration stage.
    """)
    st.markdown("---")
    st.subheader("Request a Live Demo")
    st.info("Want to walk through a real example? Use our tool live or schedule a tailored session.")
