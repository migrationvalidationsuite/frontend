import streamlit as st
from streamlit_option_menu import option_menu
import os
import base64

# --- PAGE CONFIG ---
st.set_page_config(layout="wide", page_title="MVS", page_icon="📊")

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Home", "Solutions"],
        icons=["house", "layers"],
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

# -------------------- HOME PAGE --------------------
if selected == "Home":
    # --- HEADER BANNER ---
    st.markdown("""
        <div style='background-color:#e6f0ff;padding:10px 30px;border-radius:10px;margin-bottom:20px;'>
            <h2 style='text-align:center;'>Migration and Validation Suite</h2>
            <h4 style='text-align:center;'>MVS</h4> 
        </div>
    """, unsafe_allow_html=True)

    # --- MAIN CONTENT ---
    col_left, col_right = st.columns([2, 3])
    with col_left:
        st.markdown("### Enable secure, scalable, and audit-ready HR data migration across SAP landscapes")
        st.markdown("Supports SAP HCM (on-premise and cloud), SAP S/4HANA, and legacy HR systems.")

        st.markdown("**Key Capabilities:**")
        st.markdown("""
        - **Schema Mapping & Transformation**  
          Aligns and converts source structures into SAP-ready formats.

        - **Pre-Migration Validation & Licensing**  
          Detects issues early and estimates licensing needs for cloud/S/4HANA.

        - **Rollback & Recovery**  
          Enables safe, reversible test and production loads.

        - **Audit-Ready Tracking**  
          Full traceability of rule logic, configurations, and actions.
        """)

    with col_right:
    st.image("pexels-divinetechygirl-1181263.jpg", width=450)

    # --- SUPPORTED MIGRATION PATHS BELOW IMAGE ---
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("**Supported Migration Paths:**", unsafe_allow_html=True)
    st.markdown("""
    - SAP HCM → SuccessFactors  
    - SAP HCM → S/4HANA  
    - Legacy HR Systems → SAP Cloud or On-Prem
    """)

    # --- VIDEO (below image/content) ---
    st.video("https://youtu.be/vnikhnk8rCk")

    # --- MVS SECTION ---
    col_main, col_icons = st.columns([3, 1])
    with col_main:
        st.markdown("### Migration and Validation Suite (MVS)")
        st.markdown("""
        A robust solution for orchestrating HR data migration across hybrid environments, including SAP On-Premise, S/4HANA, SuccessFactors, and legacy systems.
        """)
        st.markdown("**Key Capabilities:**")
        st.markdown("""
        - AI-powered mapping & validation  
        - Drag-and-drop transformation rules  
        - Real-time preview & profiling  
        - Cross-object and row-level validation  
        - Export SuccessFactors-ready templates with metadata  
        - Licensing controls & role-based access  
        - Audit logs, rollback & monitoring  
        """)

    with col_icons:
        icons = [
            ("data_icon.png", "Template-driven, secure transfers from legacy to SF."),
            ("check_icon.png", "Field-level checks to catch errors before go-live."),
            ("chart_icon.png", "Automated comparisons between ECC and SF data.")
        ]
        for icon_file, caption in icons:
            if os.path.exists(icon_file):
                with open(icon_file, "rb") as img_file:
                    img_data = base64.b64encode(img_file.read()).decode()
                st.markdown(
                    f"""
                    <div style='text-align:center; margin-bottom:20px;'>
                        <img src="data:image/png;base64,{img_data}" width="50" />
                        <p style='font-size:14px;'>{caption}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    # --- BLUE SECTION ---
    st.markdown("""
    <div style='background-color:#002b5c;padding:40px;margin-top:50px;border-radius:10px;'>
        <h3 style='color:white;text-align:center;'>Built for SAP & SuccessFactors</h3>
        <p style='color:white;text-align:center;'>Our platform is designed to simplify, safeguard, and speed up your transformation journey.</p>
        <div style='display:flex;justify-content:space-around;margin-top:30px;'>
            <div style='width:30%;text-align:center;'>
                <h4 style='color:white;'>Data Migration Made Easy</h4>
                <p style='color:white;'>Supports smooth data preparation and migration for SAP environments.</p>
            </div>
            <div style='width:30%;text-align:center;'>
                <h4 style='color:white;'>Data Integrity & Compliance</h4>
                <p style='color:white;'>Field-level validation ensures readiness for audits and continuity.</p>
            </div>
            <div style='width:30%;text-align:center;'>
                <h4 style='color:white;'>Document-Ready Migrations</h4>
                <p style='color:white;'>Generate structured output files ready for upload and compliance.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 👇 Now you can continue with:
# elif selected == "Solutions":

# -------------------- SOLUTIONS --------------------
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
            st.markdown("#### More Than Just Data Transfer")
            st.markdown("""
            - We begin with a Migration Assessment to evaluate system readiness, define project scope, and flag risks early.  
            - Every Custom Configuration Mapping is handled field-by-field from legacy SAP to SuccessFactors, ensuring accuracy and compliance.  
            - Our phased Cutover Strategy & Execution minimizes disruption with low-risk, controlled deployments.  
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
            st.markdown("#### Support for Parallel Testing & Revalidation")
            st.markdown("""
            - We support Parallel Testing to validate outputs and reports before Go Live.  
            - Revalidation loops and Discrepancy Monitoring are built in for compliance.  
            - Our Compliance Reports help stakeholders stay informed with audit trails and validation checkpoints.  
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
            st.markdown("#### Built-In Cleansing & Reconciliation")
            st.markdown("""
            - We help you perform Data Reconciliation & Cleansing to ensure your records are consistent and load-ready.  
            - Post-migration, our tools generate Discrepancy & Compliance Reports for continuity across HR/payroll.  
            """)
        with col2:
            st.image("pexels-divinetechygirl-1181341.jpg", use_container_width=True)
