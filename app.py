import streamlit as st
from streamlit_option_menu import option_menu
import base64
import os

st.set_page_config(layout="wide")

# Navigation Menu
selected = option_menu(
    menu_title=None,
    options=["Home", "Solutions", "Services"],
    icons=["house", "layers", "wrench"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#f8f9fa"},
        "icon": {"color": "black", "font-size": "18px"},
        "nav-link": {"font-size": "18px", "text-align": "center", "margin": "0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#cfe2ff"},
    },
)

# --- HOME PAGE ---
if selected == "Home":
    st.markdown("""
    <div style='background-color:#e6f0ff;padding:15px;border-radius:10px;'>
        <h2 style='text-align:center;'>Strategic SAP On-Premise to SuccessFactors migration product </h2>
        <h3 style='text-align:center;'>HRSC-DaSH </h3>

    </div>
    """, unsafe_allow_html=True)

    st.image("pexels-divinetechygirl-1181263.jpg", use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🚀 Accelerate Your SAP Employee Central Migration")
    st.markdown("#### Purpose-built migration, validation and variance monitoring to make your SAP HCM transformation effortless.")

    # Icons (2 rows x 3 columns)
    icons_data = [
        ("streamline.png", "Streamline Your SAP HCM Migration"),
        ("testing.png", "De-Risk Parallel Testing"),
        ("security.png", "Ensure Data Security & Governance"),
        ("variance.png", "Monitor Field-Level Variance"),
        ("validation.png", "Smart Validation Engine"),
        ("confidence.png", "Enhance Stakeholder Confidence"),
    ]
    for i in range(0, len(icons_data), 3):
        cols = st.columns(3)
        for col, (icon, label) in zip(cols, icons_data[i:i+3]):
            with col:
                if os.path.exists(icon):
                    with open(icon, "rb") as f:
                        img_data = base64.b64encode(f.read()).decode()
                    st.markdown(
                        f"""
                        <div style='text-align:center'>
                            <img src="data:image/png;base64,{img_data}" width="50" style="margin:auto;"/>
                            <p style="margin-top:10px;">{label}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

    st.markdown("---")
    st.markdown("### Why Choose Our Tool?")

    cols = st.columns(3)
    headings = ["Data Migration", "Validation", "Variance Monitoring"]
    descriptions = [
        "Template-driven, secure transfers from legacy to EC.",
        "Field-level checks to catch errors before go-live.",
        "Automated comparisons between ECC and EC data."
    ]
    icons = ["data_icon.png", "check_icon.png", "chart_icon.png"]

    for col, icon, heading, desc in zip(cols, icons, headings, descriptions):
        if os.path.exists(icon):
            with open(icon, "rb") as img_file:
                img_data = base64.b64encode(img_file.read()).decode()
            col.markdown(
                f"""
                <div style='text-align:center'>
                    <img src="data:image/png;base64,{img_data}" width="50" style="margin-bottom:10px;"/>
                    <h5>{heading}</h5>
                    <p>{desc}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Strategic Context Section
    st.markdown("---")
    st.markdown("#### Why This Tool, Why Now?")
    st.markdown("""
    <table style='width:100%;text-align:left;'>
        <tr>
            <th style='color:red;'>Challenge</th>
            <th style='color:green;'>Opportunity</th>
            <th style='color:navy;'>Strategic Fit</th>
        </tr>
        <tr>
            <td>SAP customers face costly, error-prone manual migrations.</td>
            <td>Automates mapping, validation, deployment, reducing time/risk by over 50%.</td>
            <td>Aligns with automation and governance-first data strategy.</td>
        </tr>
        <tr>
            <td>Fragmented tools and inconsistent QA delay rollouts.</td>
            <td>Configurable, repeatable pipelines for HR/payroll/time-off without hardcoding.</td>
            <td>Transforms IT from support to enabler with faster, less disruptive delivery.</td>
        </tr>
        <tr>
            <td>No rollback or audit trail risks continuity.</td>
            <td>Built-in licensing, rollback, and pre-prod validation ensure security.</td>
            <td>Meets audit and compliance needs for SAP cloud transition.</td>
        </tr>
    </table>
    """, unsafe_allow_html=True)

    # Purpose, Outcome, Features
    st.markdown("---")
    st.markdown("#### Purpose")
    st.markdown("""
    Accelerate and de-risk SAP HCM transformations by enabling governed migration of HR data from SAP HCM to SuccessFactors.
    This includes:
    - Rule-based transformation & AI suggestions
    - Pre-load validation, licensing, rollback
    - Configurable mapping with audit logs
    - Multi-tenant architecture for scalability
    """)

    st.markdown("#### Outcome")
    st.markdown("""
    Deliver a secure, audit-ready, and scalable migration tool that enables:
    - Reduced manual effort
    - Embedded traceability and governance
    - Fast, reliable deployments with minimal technical burden
    """)

    st.markdown("#### Key Features")
    st.markdown("""
    - 🧠 AI-powered mapping & validation
    - 🔄 Drag-and-drop transformation rules
    - ✅ Real-time preview & profiling
    - 🛡️ Cross-object and row-level validation
    - 📦 Export SuccessFactors-ready templates with metadata
    - 🔐 Licensing controls & role-based access
    - 📈 Audit logs, rollback & monitoring
    """)

    # Built for SAP section
    st.markdown("""
    <div style='background-color:#002b5c;padding:40px;margin-top:50px;border-radius:10px;'>
        <h3 style='color:white;text-align:center;'>🌐 Built for SAP & SuccessFactors</h3>
        <p style='color:white;text-align:center;'>Our platform is fully compatible with modern SAP and SuccessFactors ecosystems, designed to simplify, safeguard, and speed up your transformation journey.</p>
        <div style='display:flex;justify-content:space-around;margin-top:30px;'>
            <div style='width:30%;text-align:center;'>
                <h4 style='color:white;'>🛠️ SAP EC Implementation</h4>
                <p style='color:white;'>Expert-driven configuration and deployment strategies tailored to Employee Central.</p>
            </div>
            <div style='width:30%;text-align:center;'>
                <h4 style='color:white;'>📃 Data Integrity & Compliance</h4>
                <p style='color:white;'>Granular field-level validation ensures readiness for audits and business continuity.</p>
            </div>
            <div style='width:30%;text-align:center;'>
                <h4 style='color:white;'>📄 Document-Ready Migrations</h4>
                <p style='color:white;'>Accelerate documentation processes with clean, structured output files ready for upload.</p>
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
        orientation="horizontal",
        key="solutions_nav"
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
            st.header("🛡️ Validation Services")
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
