

import streamlit as st
import base64
import os
from streamlit_option_menu import option_menu

# --- PAGE CONFIG ---
st.set_page_config(layout="wide", page_title="MVS", page_icon="📊")

# --- CUSTOM STYLE ---
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
        }
        .mvs-banner {
            background-color: #e6f0ff;
            padding: 10px 30px;
            border-radius: 10px;
            display: inline-block;
            margin-bottom: 20px;
        }
        .stApp {
            background-image: url('pexels-cookiecutter-1148820.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
    </style>
""", unsafe_allow_html=True)

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

# --- HOME PAGE ---
if selected == "Home":
    st.markdown("""
        <div class='mvs-banner'>
            <h2 style='text-align:center;'>Migration and Validation Suite</h2>
            <h4 style='text-align:center;'>MVS</h4> 
        </div>
    """, unsafe_allow_html=True)

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
        st.image("pexels-divinetechygirl-1181263.jpg", use_container_width=True)
        st.markdown("**Supported Migration Paths:**")
        st.markdown("""
        - SAP HCM → SuccessFactors  
        - SAP HCM → S/4HANA  
        - Legacy HR Systems → SAP Cloud or On-Prem
        """)

    st.markdown("""
        <div style='text-align:center;'>
            <iframe width="560" height="315" src="https://www.youtube.com/embed/vnikhnk8rCk" frameborder="0" allowfullscreen></iframe>
        </div>
    """, unsafe_allow_html=True)

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

    icons = [
        ("data_icon.png", "Template-driven, secure transfers from legacy to SF."),
        ("check_icon.png", "Field-level checks to catch errors before go-live."),
        ("chart_icon.png", "Automated comparisons between ECC and SF data.")
    ]

    with col_icons:
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
                    """, unsafe_allow_html=True
                )

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

            **Features:**
            - Field-level traceability and rollback  
            - Template-based uploads  
            - Role-based access for audit compliance  

            **More Than Just Data Transfer**
            - Migration Assessment to evaluate system readiness and flag risks early  
            - Field-by-field Custom Configuration Mapping  
            - Phased Cutover Strategy for low-risk deployment  
            """)
        with col2:
            st.image("Employee_Central_Data_Migration.png", use_container_width=True)

    elif sol_choice == "Validation":
        col1, col2 = st.columns([1, 1])
        with col1:
            st.header("Validation Services")
            st.markdown("""
            Ensure every record complies with:
            - Required field presence  
            - Data types and format  
            - Referential logic (e.g., manager and org chart validation)

            **Features:**
            - Smart rules engine  
            - Summary reports with error categories  
            - Revalidation after fixes  

            **Support for Parallel Testing & Revalidation**
            - Validate outputs before Go Live  
            - Built-in discrepancy monitoring  
            - Audit-ready compliance reports  
            """)
        with col2:
            st.image("validation_lifecycle.png", use_container_width=True)

    elif sol_choice == "Discrepancy Analysis Report":
        col1, col2 = st.columns([1, 1])
        with col1:
            st.header("ECC to SF Monitoring")
            st.markdown("""
            Post-migration comparison of SAP ECC and SuccessFactors data to:

            - Detect value mismatches and format discrepancies  
            - Identify extra or missing records  
            - Focus on payroll-impacting fields  

            **Features:**
            - Side-by-side comparisons  
            - Field-level reports  
            - Visual dashboards

            **Built-In Cleansing & Reconciliation**
            - Reconcile data before monitoring  
            - Generate compliance and discrepancy reports  
            """)
        with col2:
            st.image("pexels-divinetechygirl-1181341.jpg", use_container_width=True)
