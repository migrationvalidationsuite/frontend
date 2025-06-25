import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="SAP EC Migration & Monitoring",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="auto"
)

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
    st.markdown("""
    <div style="background-color:#e6f0ff;padding:25px;border-radius:10px;text-align:center">
        <h2 style="color:#003366;">Pioneering the Future of SAP HCM – From Data-Driven Migrations to Enterprise-Ready Variance Management</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🚀 Accelerate Your SAP Employee Central Migration")
    st.markdown("""
    #### Purpose-built migration, validation and variance monitoring to make your SAP HCM transformation effortless.
    """)

    # Feature Table with Icons
    features = [
        ("migration.png", "Streamline Your SAP HCM Migration"),
        ("testing.png", "De-Risk Parallel Testing"),
        ("security.png", "Ensure Data Security & Governance"),
        ("variance.png", "Monitor Field-Level Variance"),
        ("validation.png", "Smart Validation Engine"),
        ("confidence.png", "Enhance Stakeholder Confidence"),
    ]

    st.markdown("<div style='text-align: center'>", unsafe_allow_html=True)
    cols = st.columns(6)
    for col, (icon_path, label) in zip(cols, features):
        col.image(icon_path, width=50)
        col.markdown(f"<p style='font-size:14px; font-weight:500'>{label}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Why Choose Our Tool?")
    st.markdown("""
    - Seamless Data Transformation: Map, cleanse, and migrate with accuracy.
    - Built-in Validation: Eliminate bad data before it hits production.
    - Variance Detection: Compare ECC and EC data at a granular level.
    """)
    col1, col2, col3 = st.columns(3)

with col1:
    st.image("data_icon.png", width=50)
    st.markdown("<h5 style='text-align:center;'>Data Migration</h5>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Template-driven, secure transfers from legacy to EC.</p>", unsafe_allow_html=True)

with col2:
    st.image("check_icon.png", width=50)
    st.markdown("<h5 style='text-align:center;'>Validation</h5>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Field-level checks to catch errors before go-live.</p>", unsafe_allow_html=True)

with col3:
    st.image("chart_icon.png", width=50)
    st.markdown("<h5 style='text-align:center;'>Variance Monitoring</h5>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Automated comparisons between ECC and EC data.</p>", unsafe_allow_html=True)


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
            st.header("📂 Employee Central Data Migration")
            st.markdown("""
            Our tool supports secure, auditable migration of:
            - Foundation Objects (Legal Entity, Business Unit, Location)
            - Hierarchical Position Structures
            - Employee Master Data and Assignments

            Features:
            - Field-level traceability and rollback
            - Template-based uploads
            - Role-based access for audit compliance
            """)
        with col2:
            st.image("Employee_Central_Data_Migration.png", use_container_width=True)
            st.markdown("""
            <iframe width="100%" height="400" src="https://datastudio.google.com/embed/reporting/1examplepage" frameborder="0" style="border:0" allowfullscreen></iframe>
            """, unsafe_allow_html=True)

    elif sol_choice == "Validation":
        col1, col2 = st.columns([1, 1])
        with col1:
            st.header("✅ Validation Services")
            st.markdown("""
            Ensure every single record complies with:
            - Required field presence (null detection)
            - Data types and value formatting
            - Referential logic (e.g., manager mappings, org chart validation)

            Features:
            - Smart rules engine
            - Summary reports with error categorization
            - Revalidation after fixes
            """)
        with col2:
            st.image("validation_lifecycle.png", use_container_width=True)
            st.markdown("""
            <iframe width="100%" height="400" src="https://datastudio.google.com/embed/reporting/2examplepage" frameborder="0" style="border:0" allowfullscreen></iframe>
            """, unsafe_allow_html=True)

    elif sol_choice == "Variance Monitoring":
        col1, col2 = st.columns([1, 1])
        with col1:
            st.header("📊 ECC to EC Variance Monitoring")
            st.markdown("""
            After your migration, compare SAP ECC and EC data:
            - Detect mismatches in values and field formats
            - Identify extra/missing records across modules
            - Focus on critical payroll-impacting fields

            Features:
            - Side-by-side comparisons
            - Field-level variance reports
            - Graphical dashboards to track issues
            """)
        with col2:
            st.image("variance_monitoring.png", use_container_width=True)
            st.markdown("""
            <iframe width="100%" height="400" src="https://datastudio.google.com/embed/reporting/3examplepage" frameborder="0" style="border:0" allowfullscreen></iframe>
            """, unsafe_allow_html=True)

# --- SERVICES PAGE ---
elif selected == "Services":
    st.header("🛠️ End-to-End SAP HCM Migration Services")
    st.markdown("""
    Whether you’re migrating to Employee Central or optimizing your existing setup, our services are tailored to simplify your journey:

    - **Migration Assessment**: System readiness, scope definition, and risk analysis.
    - **Custom Configuration Mapping**: Field-by-field mapping of legacy to EC.
    - **Parallel Testing Support**: Payroll and reporting checks pre-Go Live.
    - **Data Reconciliation & Cleansing**: Ensuring consistency and clean load files.
    - **Cutover Strategy & Execution**: Phased, low-risk deployments.
    - **Variance & Compliance Reports**: Side-by-side views and compliance logs.

    > Our expert-led delivery model ensures you meet tight deadlines without sacrificing quality.
    """)
    st.markdown("---")
    st.subheader("💡 Want a Guided Demo?")
    st.info("Use this tool live or book a session to see how it fits your transformation.")
