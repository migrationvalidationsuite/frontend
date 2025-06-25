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

    st.markdown("### 🚀 Accelerate Your SAP Employee Central Migration")
    st.markdown("#### Purpose-built migration, validation and variance monitoring to make your SAP HCM transformation effortless.")

    features = [
        ("streamline.png", "Streamline Your SAP HCM Migration"),
        ("testing.png", "De-Risk Parallel Testing"),
        ("security.png", "Ensure Data Security & Governance"),
        ("variance.png", "Monitor Field-Level Variance"),
        ("validation.png", "Smart Validation Engine"),
        ("confidence.png", "Enhance Stakeholder Confidence"),
    ]

    for i in range(0, len(features), 3):
        cols = st.columns(3)
        for col, (icon, text) in zip(cols, features[i:i+3]):
            with col:
                st.image(icon, width=60)
                st.markdown(f"<div style='text-align: center;'>{text}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 💡 Why Choose Our Tool?")
    st.markdown("""
    - ✅ Seamless Data Transformation: Map, cleanse, and migrate with accuracy  
    - 🔍 Built-in Validation: Eliminate bad data before it hits production  
    - 📊 Variance Detection: Compare ECC and EC data at a granular level  
    """)

    col1, col2, col3 = st.columns(3)
    cards = [
        ("data_icon.png", "Data Migration", "Template-driven, secure transfers from legacy to EC."),
        ("check_icon.png", "Validation", "Field-level checks to catch errors before go-live."),
        ("chart_icon.png", "Variance Monitoring", "Automated comparisons between ECC and EC data.")
    ]

    for col, (icon, heading, desc) in zip([col1, col2, col3], cards):
        with col:
            st.image(icon, width=60)
            st.markdown(f"<h5 style='text-align:center;'>{heading}</h5>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align:center;'>{desc}</p>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div style='background-color:#00264d;padding:40px;border-radius:10px;color:white;text-align:center'>
        <h2>Built for SAP Success</h2>
        <p>Our solutions align with the latest SAP Employee Central standards — making your migration journey smoother, smarter, and secure.</p>
        <div style="display:flex;justify-content:space-around;flex-wrap:wrap;margin-top:30px">
            <div style="width:30%;">
                <h4>HCM Migration & Implementation</h4>
                <p>Expert support for accurate and scalable SAP transitions with purpose-built tools.</p>
            </div>
            <div style="width:30%;">
                <h4>Parallel Testing & Validation</h4>
                <p>Smart validation engine to ensure pre-Go Live testing is clean, fast, and reliable.</p>
            </div>
            <div style="width:30%;">
                <h4>Variance & Compliance Reporting</h4>
                <p>Pinpoint mismatches and track key payroll-impacting fields with visual dashboards.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

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

            **Features**:  
            - Field-level traceability and rollback  
            - Template-based uploads  
            - Role-based access for audit compliance  
            """)
        with col2:
            st.image("Employee_Central_Data_Migration.png", use_container_width=True)

    elif sol_choice == "Validation":
        col1, col2 = st.columns([1, 1])
        with col1:
            st.header("🛡️ Validation Services")
            st.markdown("""
            Ensure every single record complies with:
            - Required field presence (null detection)  
            - Data types and value formatting  
            - Referential logic (e.g., manager mappings, org chart validation)  

            **Features**:  
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

            **Features**:  
            - Side-by-side comparisons  
            - Field-level variance reports  
            - Graphical dashboards to track issues  
            """)
        with col2:
            st.image("pexels-divinetechygirl-1181341.jpg", use_container_width=True)

# --- SERVICES PAGE ---
elif selected == "Services":
    st.header("🛠️ End-to-End SAP HCM Migration Services")
    st.markdown("""
    Whether you’re migrating to Employee Central or optimizing your existing setup, our services are tailored to simplify your journey:

    - **Migration Assessment**: System readiness, scope definition, and risk analysis  
    - **Custom Configuration Mapping**: Field-by-field mapping of legacy to EC  
    - **Parallel Testing Support**: Payroll and reporting checks pre-Go Live  
    - **Data Reconciliation & Cleansing**: Ensuring consistency and clean load files  
    - **Cutover Strategy & Execution**: Phased, low-risk deployments  
    - **Variance & Compliance Reports**: Side-by-side views and compliance logs  
    """)

