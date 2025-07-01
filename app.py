import streamlit as st
from streamlit_option_menu import option_menu
import base64
import os

st.set_page_config(layout="wide", page_title="MVS", page_icon="🚰")

# Remove top padding to reduce white space
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Home", "Solutions", "Services"],
        icons=["house", "layers", "wrench"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#f8f9fa"},
            "icon": {"color": "#003366", "font-size": "18px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "5px",
                "--hover-color": "#e6f0ff",
            },
            "nav-link-selected": {"background-color": "#cfe2ff", "font-weight": "bold"},
        },
    )

# --- HOME PAGE ---
if selected == "Home":
    st.markdown("""
    <div style='background-color:#e6f0ff;padding:15px;border-radius:10px;margin-bottom:20px;'>
        <h2 style='text-align:center;'>Migration and Validation Suite</h2>
        <h3 style='text-align:center;'>MVS</h3> 
    </div>
    """, unsafe_allow_html=True)

    # --- Top 3-column layout for Purpose, Outcome, Scope ---
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### Purpose")
        st.markdown("""
        Enable governed HR and Payroll migration from SAP ECC to SuccessFactors (Employee Central and Employee Central Payroll), as well as to the S/4HANA Payroll system:  
        - Schema mapping & transformation engine  
        - Pre-load validation, rollback, and licensing  
        - Audit-ready configurations for scale  
        """)

    with col2:
        st.markdown("### Outcome")
        st.markdown("""
        Deliver a secure, scalable migration tool with:  
        - Reduced manual effort  
        - Built-in governance and traceability  
        - Efficient, reliable deployment processes  
        """)

    with col3:
        st.markdown("### Scope")
        st.markdown("""
        This tool facilitates the end-to-end transfer of SAP On-Premise data to SuccessFactors, including:  
        - Schema mapping  
        - Field-level configuration  
        - Transformation engine  
        - Validation Reports  
        - Licensing and packaging  
        - Testing (unit, integration, UAT)  
        - Deployment support  
        """)

    # --- Spacer for visual gap ---
    st.markdown("<br><hr><br>", unsafe_allow_html=True)

    # --- Two-column layout for Image and Video ---
    img_col, vid_col = st.columns([2, 1])

    with img_col:
    st.image("pexels-divinetechygirl-1181263.jpg", use_container_width=True)

    with vid_col:
    st.video("https://youtu.be/vnikhnk8rCk")


    st.markdown("### Accelerate Your SAP Employee Central Migration")
    st.markdown("#### Purpose-built migration, validation and discrepancy analysis to make your HR Data Migration and Payroll effortless.")

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
                    col.markdown(
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
    headings = ["Data Migration", "Validation", "Discrepancy Analysis Report"]
    descriptions = [
        "Template-driven, secure transfers from legacy to SF.",
        "Field-level checks to catch errors before go-live.",
        "Automated comparisons between ECC and SF data."
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

    st.markdown("#### Key Features")
    st.markdown("""
    - AI-powered mapping & validation  
    - Drag-and-drop transformation rules  
    - Real-time preview & profiling  
    - Cross-object and row-level validation  
    - Export SuccessFactors-ready templates with metadata  
    - Licensing controls & role-based access  
    - Audit logs, rollback & monitoring  
    """)

    st.markdown("""
    <div style='background-color:#002b5c;padding:40px;margin-top:50px;border-radius:10px;'>
        <h3 style='color:white;text-align:center;'>Built for SAP & SuccessFactors</h3>
        <p style='color:white;text-align:center;'>Our platform is designed to simplify, safeguard, and speed up your transformation journey.</p>
        <div style='display:flex;justify-content:space-around;margin-top:30px;'>
            <div style='width:30%;text-align:center;'>
                <h4 style='color:white;'>Data Migration Made Easy</h4>
                <p style='color:white;'>Designed to support smooth data preparation and migration for SAP environments.</p>
            </div>
            <div style='width:30%;text-align:center;'>
                <h4 style='color:white;'>Data Integrity & Compliance</h4>
                <p style='color:white;'>Granular field-level validation ensures readiness for audits and business continuity.</p>
            </div>
            <div style='width:30%;text-align:center;'>
                <h4 style='color:white;'>Document-Ready Migrations</h4>
                <p style='color:white;'>Accelerate documentation processes with clean, structured output files ready for upload.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SOLUTIONS PAGE ---
elif selected == "Solutions":
    sol_choice = option_menu(
        menu_title="Our Solutions",
        options=["Data Migration", "Validation", "Discrepancy Analysis Report"],
        icons=["cloud-upload", "check2-square", "bar-chart"],
        orientation="horizontal",
        key="solutions_nav"
    )

    if sol_choice == "Data Migration":
        col1, col2 = st.columns([1, 1])
        with col1:
            st.header("Employee Central Data Migration")
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
            st.header("Validation Services")
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

    elif sol_choice == "Discrepancy Analysis Report":
        col1, col2 = st.columns([1, 1])
        with col1:
            st.header("ECC to SF Monitoring")
            st.markdown("""
            After your migration, compare SAP ECC and SF data:
            - Detect mismatches in values and field formats  
            - Identify extra/missing records across modules  
            - Focus on critical payroll-impacting fields  

            Features:
            - Side-by-side comparisons  
            - Field-level reports  
            - Graphical dashboards to track issues  
            """)
        with col2:
            st.image("pexels-divinetechygirl-1181341.jpg", use_container_width=True)

# --- SERVICES PAGE ---
elif selected == "Services":
    st.markdown("## End-to-End SAP HCM and SuccessFactors Migration Services")
    st.markdown("""
    Whether you are migrating to Employee Central or optimizing your existing setup, our services are tailored to simplify your journey:

    - **Migration Assessment**: Evaluate system readiness, define project scope, and analyze risks  
    - **Custom Configuration Mapping**: Field-by-field transformation from legacy SAP to SF  
    - **Parallel Testing Support**: Validate payroll and reporting pre-Go Live  
    - **Data Reconciliation & Cleansing**: Ensure consistency and load accuracy  
    - **Cutover Strategy & Execution**: Execute phased and low-risk deployments  
    - **Discrepancy Analysis & Compliance Reports**: Monitor discrepancies and maintain audit trails  
    """)
