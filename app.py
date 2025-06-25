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
    st.markdown("## Accelerate Your SAP Employee Central Migration")
    st.markdown("""
        #### Purpose-built migration, validation and variance monitoring to make your SAP HCM transformation effortless.
    """)
    st.image("landing_hero.png", use_container_width=True)

    # 🔽 INSERT ICON GRID SECTION HERE
    st.markdown("### Key Benefits of Our Migration Platform")

    cols = st.columns(3)

    icons = [
        ("migration.png", "Accelerated Migration", "Migrate complex org structures in record time."),
        ("testing.png", "Automated Testing", "Validate configuration and data pre-Go Live."),
        ("security.png", "Enterprise-Grade Security", "Role-based access and audit logging."),
        ("variance.png", "Variance Reporting", "Spot mismatches instantly post-migration."),
        ("validation.png", "Field Validation", "Catch nulls, mismaps and format errors."),
        ("confidence.png", "Implementation Confidence", "Drive success with predictable delivery.")
    ]

    for i in range(0, len(icons), 3):
        row = st.columns(3)
        for col, (icon_file, title, desc) in zip(row, icons[i:i+3]):
            with col:
                try:
                    st.image(icon_file, width=60)
                except:
                    st.warning(f"Missing image: {icon_file}")
                st.markdown(f"**{title}**")
                st.caption(desc)

    # ✅ CONTINUE with the rest of Home section
    st.markdown("---")
    st.subheader("Why Choose Our Tool?")
    st.markdown("""
    - 🔄 Seamless Data Transformation: Map, cleanse, and migrate with accuracy.
    - ✅ Built-in Validation: Eliminate bad data before it hits production.
    - 📊 Variance Detection: Compare ECC and EC data at a granular level.
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
