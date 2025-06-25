import streamlit as st
from streamlit_option_menu import option_menu
import base64

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
        <h2 style='text-align:center;'>Pioneering the Future of SAP HCM – From Data-Driven Migrations to Enterprise-Ready Variance Management</h2>
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
                st.markdown(
                    f"""
                    <div style='text-align:center'>
                        <img src="data:image/png;base64,{base64.b64encode(open(icon, "rb").read()).decode()}" width="50" style="margin:auto;"/>
                        <p style="margin-top:10px;">{label}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    st.markdown("---")
    st.markdown("### Why Choose Our Tool?")
    cols = st.columns(3)
    with cols[0]:
        st.image("datamigration.png", width=60)
        st.markdown("**Data Migration**", unsafe_allow_html=True)
        st.write("Template-driven, secure transfers from legacy to EC.")

    with cols[1]:
        st.image("validation.png", width=60)
        st.markdown("**Validation**", unsafe_allow_html=True)
        st.write("Field-level checks to catch errors before go-live.")

    with cols[2]:
        st.image("pexels-divinetechygirl-1181341.jpg", width=60)
        st.markdown("**Variance Monitoring**", unsafe_allow_html=True)
        st.write("Automated comparisons between ECC and EC data.")

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
    solution_choice = option_menu(
        menu_title="Our Solutions",
        options=["Data Migration", "Validation", "Variance Monitoring"],
        icons=["cloud-upload", "check2-square", "bar-chart"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal"
    )

    if solution_choice == "Data Migration":
        st.header("📂 Employee Central Data Migration")
        st.image("Employee_Central_Data_Migration.png", use_container_width=True)
        st.markdown("""
        Our tool supports secure, auditable migration of:
        - Foundation Objects (Legal Entity, Business Unit, Location)
        - Hierarchical Position Structures
        - Employee Master Data and Assignments

        **Features:**
        - Field-level traceability and rollback
        - Template-based uploads
        - Role-based access for audit compliance
        """)

    elif solution_choice == "Validation":
        st.header("🛡️ Validation Services")
        st.image("validation_lifecycle.png", use_container_width=True)
        st.markdown("""
        Ensure every single record complies with:
        - Required field presence (null detection)
        - Data types and value formatting
        - Referential logic (e.g., manager mappings, org chart validation)

        **Features:**
        - Smart rules engine
        - Summary reports with error categorization
        - Revalidation after fixes
        """)

    elif solution_choice == "Variance Monitoring":
        st.header("📊 ECC to EC Variance Monitoring")
        st.image("pexels-divinetechygirl-1181341.jpg", use_container_width=True)
        st.markdown("""
        After your migration, compare SAP ECC and EC data:
        - Detect mismatches in values and field formats
        - Identify extra/missing records across modules
        - Focus on critical payroll-impacting fields

        **Features:**
        - Side-by-side comparisons
        - Field-level variance reports
        - Graphical dashboards to track issues
        """)

# --- SERVICES PAGE (OPTIONAL STUB) ---
elif selected == "Services":
    st.header("🛠️ End-to-End SAP HCM Migration Services")
    st.markdown("""
    Our services streamline your transition to SAP Employee Central with:
    - Migration Assessments and Roadmapping
    - Secure Data Cleansing and Transformation
    - Parallel Testing with Payroll Precision
    - Post-Go-Live Variance Reporting
    """)
