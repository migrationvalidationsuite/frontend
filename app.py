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
if selected == "Home":
    # Header banner
    st.markdown("""
    <div style='background-color:#e6f0ff;padding:15px;border-radius:10px;margin-bottom:20px;'>
    <div style='max-width:900px;margin:auto;'>
        <h2 style='text-align:center;'>Migration and Validation Suite</h2>
        <h3 style='text-align:center;'>MVS</h3> 
    </div>
    </div>
    """, unsafe_allow_html=True)


    # Overview + image/video
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

    # MVS Summary + Icons
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

    # Blue SAP section
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

# -------------------- SOLUTIONS --------------------

# -------------------- SOLUTIONS --------------------
elif selected == "Solutions":
    st.markdown("## Data Migration: End-to-End SAP HR Transformation")
    st.markdown("A secure, scalable, audit-ready solution for migrating HR data across SAP On-Premise, S/4HANA, SuccessFactors, and legacy systems.")

    st.markdown("### Supported Scenarios:")
    st.markdown("""
    - SAP On-Premise → SuccessFactors (EC, Payroll)  
    - SAP On-Premise → S/4HANA (HCM, Payroll, OM)  
    - Legacy/Non-SAP → SAP HCM or SuccessFactors  
    """)

    st.markdown("### We Migrate:")
    st.markdown("""
    - **Foundation Objects:** Legal entities, locations, cost centers  
    - **Org & Position Hierarchies:** Structures, reporting lines, org charts  
    - **Employee Master Data:** Personal, job, and pay info  
    - **Payroll & Time Data:** Optional for testing and continuity  
    """)

    st.markdown("### Key Features:")
    st.markdown("""
    - **Field-Level Traceability:** Logged transformations with rollback  
    - **Template Uploads:** Pre-configured formats reduce errors  
    - **Role-Based Access:** GDPR/SOX-compliant  
    - **Validation Reports:** Catch issues pre–go-live  
    - **Rule Engine:** Reusable, localized transformation logic  
    """)

    st.markdown("---")
    st.markdown("## Validation: Accuracy from Source to Target")
    st.markdown("Ensures data is mapped, transformed, and loaded correctly across all stages of migration, with comparisons between source, files, and system outputs.")

    st.markdown("### What We Validate:")
    st.markdown("""
    - **Required Fields:** Flags missing/null critical values  
    - **Data Format & Types:** Enforces SAP/SF standards  
    - **Mapping Accuracy:** Validates transformation rules  
    - **Source-to-File Match:** Ensures load files mirror source  
    - **Post-Load Check:** Confirms final system reflects expected results  
    """)

    st.markdown("### Key Features:")
    st.markdown("""
    - **Rules-Based Engine:** Supports complex business logic  
    - **Exception Reporting:** Highlights and categorizes errors  
    - **Revalidation Workflow:** Iterative checks for SIT/UAT  
    - **Audit Logs:** Full traceability for compliance  
    """)

    st.markdown("---")
    st.markdown("## Discrepancy Analysis: Reconciliation Across Systems")
    st.markdown("Verifies that migrated data is accurate, complete, and consistent in the target system post-load, supporting operational readiness.")

    st.markdown("### What We Monitor:")
    st.markdown("""
    - **Field-Level Accuracy:** Detects mismatches in key values  
    - **Record Completeness:** Flags missing/extra records  
    - **Critical Field Checks:** Focus on payroll, time, org data  
    """)

    st.markdown("### Key Features:")
    st.markdown("""
    - **Source-to-Target Comparisons:** Full visibility across extracts, loads, reports  
    - **Discrepancy Reports:** Actionable summaries of mismatches  
    - **Visual Dashboards:** Track reconciliation status in real time  
    - **Audit Trail:** Logged results for governance and compliance  
    """)

