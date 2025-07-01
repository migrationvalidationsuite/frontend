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

# -------------------- HOME --------------------
import streamlit as st
import base64
import os
from streamlit_option_menu import option_menu

# --- PAGE CONFIG ---
st.set_page_config(layout="wide", page_title="MVS", page_icon="📊")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
        }

        body {
            background-image: url('pexels-googledeepmind-17483873.jpg');
            background-size: cover;
            background-attachment: fixed;
        }

        .overlay {
            background-color: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            border-radius: 12px;
        }

        .mvs-banner {
            background-color: #e6f0ff;
            padding: 20px 50px;
            border-radius: 12px;
            margin-bottom: 30px;
            text-align: center;
            width: 80%;
            margin-left: auto;
            margin-right: auto;
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
            <h2>Migration and Validation Suite</h2>
            <h4>MVS</h4>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='overlay'>", unsafe_allow_html=True)

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
        <div style='text-align:center; margin-top:30px;'>
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

    st.markdown("</div>", unsafe_allow_html=True)  # Close .overlay

# --- SOLUTIONS PAGE ---
selected = "Solutions"  # You can change this to dynamic selection logic

if selected == "Solutions":
    sol_choice = option_menu(
        menu_title="Our Solutions",
        options=["Data Migration", "Validation", "Discrepancy Analysis Report"],
        icons=["cloud-upload", "check2-square", "bar-chart"],
        orientation="horizontal",
        key="solutions_nav"
    )

    # --- DATA MIGRATION ---
    if sol_choice == "Data Migration":
        col1, col2 = st.columns([3, 2])
        with col1:
            st.markdown("## Data Migration: End-to-End SAP HR Transformation")
            st.markdown("""
            A secure, scalable, audit-ready solution for migrating HR data across SAP On-Premise, S/4HANA, SuccessFactors, and legacy systems.
            
            **Supported Scenarios:**
            - SAP On-Premise → SuccessFactors (EC, Payroll)
            - SAP On-Premise → S/4HANA (HCM, Payroll, OM)
            - Legacy/Non-SAP → SAP HCM or SuccessFactors

            **We Migrate:**
            - Foundation Objects: Legal entities, locations, cost centers
            - Org & Position Hierarchies: Structures, reporting lines, org charts
            - Employee Master Data: Personal, job, and pay info
            - Payroll & Time Data: Optional for testing and continuity
            """)

        with col2:
            st.markdown("### Key Features")
            st.markdown("""
            - Field-Level Traceability: Logged transformations with rollback  
            - Template Uploads: Pre-configured formats reduce errors  
            - Role-Based Access: GDPR/SOX-compliant  
            - Validation Reports: Catch issues pre–go-live  
            - Rule Engine: Reusable, localized transformation logic
            """)
            st.image("datamig_img.png", use_container_width=True)

    # --- VALIDATION ---
    elif sol_choice == "Validation":
        col1, col2 = st.columns([3, 2])
        with col1:
            st.markdown("## Validation: Accuracy from Source to Target")
            st.markdown("""
            Ensures data is mapped, transformed, and loaded correctly across all stages of migration, with comparisons between source, files, and system outputs.

            **What We Validate:**
            - Required Fields: Flags missing/null critical values  
            - Data Format & Types: Enforces SAP/SF standards  
            - Mapping Accuracy: Validates transformation rules  
            - Source-to-File Match: Ensures load files mirror source  
            - Post-Load Check: Confirms final system reflects expected results  
            """)

        with col2:
            st.markdown("### Key Features")
            st.markdown("""
            - Rules-Based Engine: Supports complex business logic  
            - Exception Reporting: Highlights and categorizes errors  
            - Revalidation Workflow: Iterative checks for SIT/UAT  
            - Audit Logs: Full traceability for compliance
            """)
            st.image("validation_lifecycle.png", use_container_width=False, width=350)

    # --- DISCREPANCY ANALYSIS ---
    elif sol_choice == "Discrepancy Analysis Report":
        col1, col2 = st.columns([3, 2])
        with col1:
            st.markdown("## Discrepancy Analysis: Reconciliation Across Systems")
            st.markdown("""
            Verifies that migrated data is accurate, complete, and consistent in the target system post-load, supporting operational readiness.

            **What We Monitor:**
            - Field-Level Accuracy: Detects mismatches in key values  
            - Record Completeness: Flags missing/extra records  
            - Critical Field Checks: Focus on payroll, time, org data  
            """)

        with col2:
            st.markdown("### Key Features")
            st.markdown("""
            - Source-to-Target Comparisons: Full visibility across extracts, loads, reports  
            - Discrepancy Reports: Actionable summaries of mismatches  
            - Visual Dashboards: Track reconciliation status in real time  
            - Audit Trail: Logged results for governance and compliance  
            """)
            st.image("pexels-divinetechygirl-1181341.jpg", use_container_width=False, width=350)

