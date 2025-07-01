import streamlit as st
from streamlit_option_menu import option_menu
import base64
import os

st.set_page_config(layout="wide", page_title="MVS", page_icon="📊")

st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

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

if selected == "Home":
    # --- Header Banner ---
    st.markdown("""
    <div style='background-color:#e6f0ff;padding:15px 40px;border-radius:10px;margin-bottom:20px;max-width:80%;margin-left:auto;margin-right:auto;'>
        <h2 style='text-align:center;'>Migration and Validation Suite</h2>
        <h3 style='text-align:center;'>MVS</h3> 
    </div>
    """, unsafe_allow_html=True)

    # --- Overview Section ---
    col_text, col_img = st.columns([3, 2])

    with col_text:
        st.markdown("### Enable secure, scalable, and audit-ready HR data migration across SAP landscapes")
        st.markdown("""
        Supports SAP HCM (on-premise and cloud), SAP S/4HANA, and legacy HR systems.

        **Key Capabilities:**

        - **Schema Mapping & Transformation**  
          Aligns and converts source structures into SAP-ready formats.

        - **Pre-Migration Validation & Licensing**  
          Detects issues early and estimates licensing needs for cloud/S/4HANA.

        - **Rollback & Recovery**  
          Enables safe, reversible test and production loads.

        - **Audit-Ready Tracking**  
          Full traceability of rule logic, configurations, and actions.

        **Supported Migration Paths:**

        - SAP HCM → SuccessFactors  
        - SAP HCM → S/4HANA  
        - Legacy HR Systems → SAP Cloud or On-Prem
        """)

    with col_img:
        st.image("pexels-divinetechygirl-1181263.jpg", use_container_width=True)
        st.video("https://youtu.be/vnikhnk8rCk")

    # --- MVS Summary with Icons to the Right ---
    left_col, right_col = st.columns([3, 1])

    with left_col:
        st.markdown("""
        <h3>Migration and Validation Suite (MVS)</h3>
        <p>A robust solution for orchestrating HR data migration across hybrid environments, including SAP On-Premise, S/4HANA, SuccessFactors, and legacy systems.</p>

        <h4>Key Capabilities:</h4>
        <ul>
            <li>AI-powered mapping & validation</li>
            <li>Drag-and-drop transformation rules</li>
            <li>Real-time preview & profiling</li>
            <li>Cross-object and row-level validation</li>
            <li>Export SuccessFactors-ready templates with metadata</li>
            <li>Licensing controls & role-based access</li>
            <li>Audit logs, rollback & monitoring</li>
        </ul>
        """, unsafe_allow_html=True)

    with right_col:
        icons = ["data_icon.png", "check_icon.png", "chart_icon.png"]
        descriptions = [
            "Template-driven, secure transfers from legacy to SF.",
            "Field-level checks to catch errors before go-live.",
            "Automated comparisons between ECC and SF data."
        ]

        for icon, desc in zip(icons, descriptions):
            if os.path.exists(icon):
                with open(icon, "rb") as f:
                    img_data = base64.b64encode(f.read()).decode()
                right_col.markdown(
                    f"""
                    <div style='text-align:center; margin-bottom:20px;'>
                        <img src="data:image/png;base64,{img_data}" width="50"/>
                        <p style="margin-top:10px;">{desc}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    # --- Blue Background SAP Section ---
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
