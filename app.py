import streamlit as st
import base64
from streamlit_option_menu import option_menu
import os

st.set_page_config(layout="wide", page_title="MVS", page_icon="📊")

# --- BACKGROUND IMAGE as base64 ---
def get_base64_bg(image_file):
    with open(image_file, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    return data

bg_image_base64 = get_base64_bg("pexels-googledeepmind-17483873.jpg")

# --- CSS: true background layer with white overlay on top ---
st.markdown(f"""
    <style>
        .stApp {{
            position: relative;
        }}
        .background {{
            position: fixed;
            top: 0;
            left: 0;
            height: 100%;
            width: 100%;
            background-image: url("data:image/jpeg;base64,{bg_image_base64}");
            background-size: cover;
            background-position: center;
            z-index: -2;
        }}
        .overlay {{
            position: fixed;
            top: 0;
            left: 0;
            height: 100%;
            width: 100%;
            background-color: rgba(255, 255, 255, 0.85);
            z-index: -1;
        }}
        .block-container {{
            z-index: 1;
            position: relative;
            padding-top: 2rem;
        }}
    </style>
    <div class="background"></div>
    <div class="overlay"></div>
""", unsafe_allow_html=True)


# --- SIDEBAR ---
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Home", "Solutions"],
        icons=["house", "layers"],
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

    # Main section on top of background
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
        """)

    with col_img:
        st.image("pexels-divinetechygirl-1181263.jpg", use_container_width=True)
        st.video("https://youtu.be/vnikhnk8rCk")


    st.markdown("</div></div>", unsafe_allow_html=True)

# Add the rest of your content as needed...

    # MVS Summary
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

    # Blue section
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
elif selected == "Solutions":
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

    # --- DISCREPANCY ANALYSIS ---
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
