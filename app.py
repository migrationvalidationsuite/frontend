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
    st.markdown("## 🚀 Accelerate Your SAP Employee Central Migration")
    st.markdown("""
        #### Purpose-built migration, validation and variance monitoring to make your SAP HCM transformation effortless.
    """)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        - ⚙️ **Automate** and optimize key HR and payroll processes
        - 🔐 **Secure** and standardize your payroll workflows
        - ⏱️ **Accelerate** and de-risk testing and migration activities
        - 🧠 **Improve compliance** and reduce audit risks
        - 📈 **Increase satisfaction** through better data accuracy
        """)
    with col2:
        st.image("landing_hero.png", use_container_width=True)

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
            - 🏢 Foundation Objects (Legal Entity, Business Unit, Location)
            - 🧩 Hierarchical Position Structures
            - 👤 Employee Master Data and Assignments

            Key Features:
            - 🔍 Field-level traceability and rollback
            - 📁 Template-based uploads
            - 🔒 Role-based access for audit compliance
            - ⚙️ Automated mapping and transformation rules
            - 🧾 Detailed migration logs and status trackers
            """)
        with col2:
            st.image("Employee_Central_Data_Migration.png", use_container_width=True)

    elif sol_choice == "Validation":
        col1, col2 = st.columns([1, 1])
        with col1:
            st.header("✅ Validation Services")
            st.markdown("""
            Ensure every single record complies with:
            - 🧪 Field validations (required, format, types)
            - 🔗 Referential integrity (e.g., position-to-manager links)
            - 📊 Multi-layer rule enforcement (custom + system)

            Features:
            - 🤖 Smart rules engine
            - 📋 Summary and drill-down error reports
            - 🔄 Revalidation workflows for corrections
            - 🚦 Validation dashboards for Go-Live readiness
            """)
        with col2:
            st.image("validation_lifecycle.png", use_container_width=True)

    elif sol_choice == "Variance Monitoring":
        col1, col2 = st.columns([1, 1])
        with col1:
            st.header("📊 ECC to EC Variance Monitoring")
            st.markdown("""
            After your migration, compare SAP ECC and EC data:
            - 🔍 Detect mismatches in values and field formats
            - ❌ Identify extra/missing records across modules
            - 📈 Focus on critical payroll-impacting fields

            Features:
            - 👓 Side-by-side comparisons
            - 🧾 Field-level variance reporting
            - 📊 Graphical dashboards to track issues
            - ✅ Confidence indicators for sign-off
            """)
        with col2:
            st.image("variance_monitoring.png", use_container_width=True)

# --- SERVICES PAGE ---
elif selected == "Services":
    st.header("🛠️ End-to-End SAP HCM Migration Services")
    st.markdown("""
    Whether you're starting fresh or migrating legacy systems, we support:

    - 🧭 **Migration Assessment**: Readiness scoring, data profiling, and gap analysis
    - 🔄 **Custom Mapping**: Legacy-to-EC transformation logic per module
    - 🧪 **Parallel Testing**: Validate accuracy before Go-Live
    - 🧼 **Reconciliation & Cleansing**: Deduplication, null resolution, and cleansing strategies
    - 🚀 **Cutover Planning**: Risk mitigation and Go-Live strategy execution
    - 📋 **Compliance Reporting**: Generate variance and audit logs for submission

    👉 Need help setting up? Use the tool live or book a guided session.
    """)
