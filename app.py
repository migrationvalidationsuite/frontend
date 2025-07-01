import streamlit as st
from streamlit_option_menu import option_menu
import base64
import os

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

# -------------------- HOME --------------------
if selected == "Home":
    # Header banner
    st.markdown("""
        <div style='background-color:#e6f0ff;padding:15px;border-radius:10px;margin-bottom:20px;margin-top:-40px;'>
            <div style='max-width:900px;margin:auto;'>
                <h2 style='text-align:center;'>Migration and Validation Suite</h2>
                <h3 style='text-align:center;'>MVS</h3> 
            </div>
        </div>
    """, unsafe_allow_html=True)

    col_text, col_img = st.columns([3, 2])

    with col_text:
        st.markdown("### Enable secure, scalable, and audit-ready HR data migration across SAP landscapes")
        st.markdown("Supports SAP HCM (on-premise and cloud), SAP S/4HANA, and legacy HR systems.")

        st.markdown("**Key Capabilities:**")
        st.markdown("""
        - **Mapping & Transformation**  
          Converts source structures into SAP-ready formats.

        - **Validation & Licensing**  
          Identifies issues early and ensures cloud/S/4HANA readiness.

        - **Safe Rollback**  
          Enables reversible test and production runs.

        - **Audit-Ready**  
          Tracks rule logic, configs, and data actions.
        """)

        st.markdown("**Supported Migration Paths:**", unsafe_allow_html=True)
        st.markdown("""
        <div style='padding-left:15px;'>
        - SAP HCM → SuccessFactors<br>
        - SAP HCM → S/4HANA<br>
        - Legacy HR Systems → SAP Cloud or On-Prem
        </div>
        """, unsafe_allow_html=True)

    with col_img:
        st.image("pexels-divinetechygirl-1181263.jpg", use_container_width=True)
        st.video("https://youtu.be/vnikhnk8rCk")

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

    elif sol_choice == "Validation":
        col1, col2 = st.columns([3, 2])
        with col1:
            st.markdown("## Validation: Accuracy from Source to Target")
            st.markdown("""
            Ensures data is mapped, transformed, and loaded correctly across all stages of migration.

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
            - Rules-Based Engine  
            - Exception Reporting  
            - Revalidation Workflow  
            - Audit Logs  
            """)
            st.image("validation_lifecycle.png", use_container_width=False, width=350)

    elif sol_choice == "Discrepancy Analysis Report":
        col1, col2 = st.columns([3, 2])
        with col1:
            st.markdown("## Discrepancy Analysis: Reconciliation Across Systems")
            st.markdown("""
            Verifies that migrated data is accurate, complete, and consistent in the target system.

            **What We Monitor:**
            - Field-Level Accuracy  
            - Record Completeness  
            - Critical Field Checks  
            """)

        with col2:
            st.markdown("### Key Features")
            st.markdown("""
            - Source-to-Target Comparisons  
            - Discrepancy Reports  
            - Visual Dashboards  
            - Audit Trail  
            """)
            st.image("pexels-divinetechygirl-1181341.jpg", use_container_width=False, width=350)
