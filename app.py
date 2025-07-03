import streamlit as st
import base64
from streamlit_option_menu import option_menu
import os

st.set_page_config(layout="wide", page_title="MVS", page_icon="📊")

# --- REMOVE TOP WHITE SPACE & MAKE RESPONSIVE ---
st.markdown("""
    <style>
        .block-container {
            padding-top: 0.5rem !important;
        }
        @media (max-width: 768px) {
            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }
        }
    </style>
""", unsafe_allow_html=True)

# --- BACKGROUND IMAGE SETUP ---
def set_background(image_file):
    with open(image_file, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    st.markdown(f"""
        <style>
            .stApp {{
                background: linear-gradient(rgba(255,255,255,0.85), rgba(255,255,255,0.85)), 
                            url("data:image/jpeg;base64,{data}");
                background-size: cover;
                background-attachment: fixed;
                background-position: center;
            }}
        </style>
    """, unsafe_allow_html=True)

set_background("pexels-googledeepmind-17483873.jpg")

# --- SIDEBAR NAVIGATION ---
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

    # 🚀 DEMO BUTTON (Placeholder)
    st.markdown("""
        <div style="margin-top:100px;text-align:center;">
            <button style="background-color:#003366;color:white;padding:10px 20px;border:none;border-radius:5px;font-size:16px;">
                🚀 Launch Demo
            </button>
        </div>
    """, unsafe_allow_html=True)

# -------------------- HOME --------------------
if selected == "Home":
    # --- Header banner ---
    st.markdown("""
        <div style='background-color:#e6f0ff;padding:15px;border-radius:10px;margin-bottom:20px;'>
            <div style='max-width:900px;margin:auto;'>
                <h2 style='text-align:center;'>Effortless Data Migration, Done Right</h2>
                <h3 style='text-align:center;'>MVS (Migration & Validation Suite)</h3> 
            </div>
        </div>
    """, unsafe_allow_html=True)

    # --- Top section: Migration Benefits (text + image/video) ---
    col1, col2 = st.columns([3, 2.5])
    with col1:
        st.markdown("### Enable secure, scalable, and audit-ready HR data migration across SAP landscapes")
        st.markdown("Supports Migration for SAP HCM (on-premise and cloud), SAP S/4HANA, and legacy HR systems.")

        st.markdown("**Power your transformation with:**")
        st.markdown("""
        - **Schema Mapping & Transformation**  
          Seamlessly aligns and converts source structures into SAP-ready formats across platforms.
        - **Pre-Migration Validation**  
          Identifies data issues early on through audit trials for cloud and S/4HANA adoption.
        - **Rollback & Audit-Ready Tracking**  
          Enables safe, reversible data loads with full traceability of rules, configurations, and actions.
        """)

        st.markdown("**Supported Migration Paths:**")
        st.markdown("""
        - SAP HCM → SuccessFactors  
        - SAP HCM → S/4HANA  
        - Legacy HR Systems → SAP Cloud or On-Premise
        """)

    with col2:
        st.image("pexels-divinetechygirl-1181263.jpg", use_container_width=True)
        st.video("https://youtu.be/o_PcYfH36TI")

    # --- Why MVS Works (Icons LEFT, Capabilities RIGHT) ---
    col1, col2 = st.columns([3, 2.5])
    with col1:
        st.markdown("### Why MVS?")
        st.markdown("""
        <p>MVS is a robust solution for orchestrating HR data migration across hybrid environments, including SAP On-Premise, S/4HANA, SuccessFactors, and legacy systems.</p>
        """, unsafe_allow_html=True)

        icons = ["data_icon.png", "check_icon.png", "chart_icon.png"]
        descriptions = [
            "Template-driven, secure transfers between systems.",
            "Detailed checks at the field level to catch issues throughout the migration process.",
            "Automated comparisons between source and target systems."
        ]

        for icon, desc in zip(icons, descriptions):
            icon_col, text_col = st.columns([1, 6])
            with icon_col:
                if os.path.exists(icon):
                    with open(icon, "rb") as f:
                        img_data = base64.b64encode(f.read()).decode()
                    st.markdown(
                        f"""<img src="data:image/png;base64,{img_data}" width="40" style="margin-top:10px;">""",
                        unsafe_allow_html=True
                    )
            with text_col:
                st.markdown(f"<p style='margin-top:18px;'>{desc}</p>", unsafe_allow_html=True)

    with col2:
        
        st.markdown("#### Key Capabilities:")
        st.markdown("""
        <ul>
            <li>AI-powered mapping & validation</li>
            <li>Real-time preview & profiling</li>
            <li>Cross-object and row-level validation</li>
            <li>Licensing controls & role-based access</li>
            <li>Audit logs, rollback & monitoring</li>
            <li>Designed to reduce manual effort and shorten project timelines</li>
            <li>Supports stakeholder collaboration with clear audit and status visibility</li>
            <li>Ability to easily create and manage transformation rules with an intuitive, interactive interface</li>
        </ul>
        """, unsafe_allow_html=True)

    # --- SAP Highlights Section ---
    st.markdown("""
    <div style='background-color:#002b5c;padding:40px;margin-top:50px;border-radius:10px;'>
        <h3 style='color:white;text-align:center;'>Built for SAP Cloud & On-Premise</h3>
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
        col1, col2 = st.columns([2.9, 3])

        with col1:
            st.markdown("## End-to-End SAP HR Transformation Journey")
            st.markdown("""
A secure, scalable, audit-ready solution for migrating HR data across SAP On-Premise, S/4HANA, SuccessFactors, and legacy systems.

**What We Migrate & Validate:**
- **Foundation Data:** Legal entities, hierarchy structures, cost centers, locations, pay scale information, job functions and classifications, and work schedule objects  
- **Position Data:** Hierarchies, reporting lines, position classifications, and relationships  
- **Employee Master Data:** Personal details, assignments, and job- and pay-related data  
- **Payroll & Time Data:** Including attendance, leave, and absence records  

We also **validate and compare payroll results** across systems to ensure accuracy and consistency post-migration.
            """)

            # --- INTERACTIVE BUTTONS ---
            col_a, col_b = st.columns(2)

            with col_a:
                if st.button("Foundation Data"):
                    st.info("""
- Legal Entities  
- Business Units  
- Cost Centers  
- Locations  
- Pay Scales  
- Job Classifications  
- Work Schedule Objects
                    """)

                if st.button("Employee Master Data"):
                    st.info("""
- Personal & Contact Information  
- Employee Assignments  
- Job and Pay Details  
- Employment History  
                    """)

            with col_b:
                if st.button("Position Data"):
                    st.info("""
- Hierarchies and Structures  
- Reporting Lines  
- Position Types and Groups  
- Relationships and Dependencies  
                    """)

                if st.button("Payroll & Time Data"):
                    st.info("""
- Attendance and Leave Balances  
- Absence Records  
- Payroll Fields  
- Calculation Fields  
                    """)

        with col2:
            st.image("edmdr.png", use_container_width=True)

            st.markdown("### Supported Scenarios")
            st.markdown("""
- SAP ECC → SuccessFactors (EC, Time, Payroll)  
- SAP ECC → S/4HANA (HCM, Payroll, PA (Personnel Administration), OM (Organizational Management))  
- Legacy/Non-SAP → SAP HCM and SuccessFactors
            """)

            st.markdown("### Key Features")
            st.markdown("""
- **Transformation Engine:** Transformation engine with rollback support  
- **Template Uploads:** Pre-configured mapping, reduced effort  
- **Role-Based Access:** Permission management based on user roles  
- **Validation Reports:** Flags issues across all stages  
- **Rule Engine:** Reusable, localized logic
            """)

        # ✅ Bottom banner image
        st.image("datamig_img.png", use_container_width=True)

    # --- VALIDATION ---
    elif sol_choice == "Validation":
        col1, col2 = st.columns([3, 2.7])
        with col1:
            st.markdown("## Ensuring Data Accuracy Between Systems")
            st.markdown("""
Our validation services ensure HR data is correctly mapped, transformed, and loaded across every migration stage. We validate data between source systems, load files, and reporting outputs to confirm consistency and production readiness.

**What We Validate:**
- Required Fields: Detect missing/null values in critical fields  
- Format Compliance: Enforce expected types and structures  
- Mapping Accuracy: Verify source-to-target alignment  
- Source-to-File Match: Ensure extracted data mirrors load-ready files  
- Post-Load Validation: Confirm target system reflects intended records  
- Change Monitoring: Identify and isolate high-impact issues  
            """)

        with col2:
            st.markdown("### Key Features")
            st.markdown("""
- Rules-Based Validation Engine  
- Categorized Exception Reporting  
- Iterative Revalidation Workflow  
- Full Audit Logging for Compliance  
- Support for all Employee Information  
            """)
            st.image("validation_lifecycle.png", use_container_width=False, width=350)

    # --- DISCREPANCY ANALYSIS ---
    elif sol_choice == "Discrepancy Analysis Report":
        col1, col2 = st.columns([3, 2.6])
        with col1:
            st.markdown("## Reconciliation Across Systems")
            st.markdown("""
Our monitoring validates accurate data loads post-migration–across platforms like SuccessFactors, S/4HANA, or SAP HCM. It ensures alignment, traceability, and readiness for live HR/payroll processes.

**What We Monitor:**
- **Field-Level Accuracy:** Detect mismatches in critical values  
- **Record Completeness:** Spot missing/extra records  
- **Business-Critical Fields:** Focus on payroll, time, and org structures  
- **Change Tracking:** View changes before/after load  

We cover field-level, record-level, and format-level checks to ensure clean post-migration integrity across HR modules.  
Visual dashboards and summary reports offer real-time reconciliation status for faster resolution and compliance.
            """)

        with col2:
            st.markdown("### Key Features")
            st.markdown("""
- Source-to-Target Comparisons  
- Discrepancy Summary Reports  
- Visual Reconciliation Dashboards  
- Logged Issues for Governance & Audit  
            """)
            st.image("pexels-divinetechygirl-1181341.jpg", use_container_width=False, width=350)
