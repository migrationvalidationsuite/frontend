import streamlit as st
import base64
from streamlit_option_menu import option_menu
import os

st.set_page_config(layout="wide", page_title="MVS", page_icon="📊")

# --- SESSION STATE FOR DEMO NAVIGATION ---
if 'demo_page' not in st.session_state:
    st.session_state.demo_page = "main"

def go_to_demo(page):
    st.session_state.demo_page = page

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
        options=["Home", "Solutions", "Launch Demo"],
        icons=["house", "layers", "rocket"],
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
            "nav-link-selected": {
                "background-color": "#a3c2f2",  # darker blue
                "font-weight": "bold"
            }

            },
        }  # ✅ This closing parenthesis was missing
    )

# -------------------- HOME --------------------
if selected == "Home":
    st.markdown("""
        <div style='background-color:#e6f0ff;padding:15px;border-radius:10px;margin-bottom:20px;'>
            <div style='max-width:900px;margin:auto;'>
                <h2 style='text-align:center;'>Effortless Data Migration, Done Right</h2>
                <h3 style='text-align:center;'>MVS (Migration & Validation Suite)</h3> 
            </div>
        </div>
    """, unsafe_allow_html=True)

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

elif selected == "Launch Demo":
    from demo_module import render  # ✅ make sure this is imported

    if st.session_state.demo_page == "main":
        st.markdown("""
            <div style='background-color:#e6f0ff;padding:20px;border-radius:10px;margin-bottom:20px;'>
                <h2 style='text-align:center;'>🚀 Launch Pad</h2>
                <h4 style='text-align:center;'>Select a migration scenario to get started</h4>
            </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            b1, b2, b3 = st.columns(3)

            with b1:
                if st.button("SAP HCM → SuccessFactors"):
                    st.session_state.demo_page = "sap_to_sf"

            with b2:
                st.button("SAP HCM → S/4HANA (coming soon)", disabled=True)

            with b3:
                st.button("Legacy HR Systems → SAP Cloud or On-Premise (coming soon)", disabled=True)

            st.image("dmigimg.jpg", use_container_width=True)


    elif st.session_state.demo_page == "sap_to_sf":
        back_col, _ = st.columns([1, 5])
        with back_col:
            if st.button("⬅ Back to Scenarios", key="btn_back", use_container_width=True):
                st.session_state.demo_page = "main"

        st.title("SAP HCM → SuccessFactors")
        st.subheader("What do you want to migrate?")

        def migration_row(label, key, detail_text, next_page=None):
            col1, col2 = st.columns([5, 3.8])
            with col1:
                if st.button(label, key=key, use_container_width=True):
                    if next_page:
                        st.session_state.demo_page = next_page
            with col2:
                with st.expander("ℹ️ Details"):
                    st.markdown(detail_text)

        migration_row("Foundation Data", "fd_demo", """
- Pay Scale Level  
- Pay Scale Level - Pay Component Assignment  
- Pay Scale Group  
- Pay Scale Area  
- Pay Scale Type  
- Pay Calendar  
- Pay Calendar - Pay Period  
- PayComponent  
- Holiday  
- Holiday Calendar  
- Work Schedule  
- Work Schedule Day Model  
- Legal Entity (Company)  
- Business Unit  
- Business Unit - Legal Entity  
- Division  
- Division - Business Unit  
- Department  
- Department - Division  
- Team  
- Team - Department  
- Job Family (Job Function)  
- Job Classification  
- Job Classification AUS  
- Location  
- Cost Centre  
- Positions  
- Addresses  
        """, next_page="foundation_data_view")

        migration_row("Employee Data", "pd_demo", """
- Basic Import  
- Biographical Information (Person Info)  
- Employment Info  
- Job Information  
- Personal Info (Hire Date)  
- National ID Information  
- Compensation Info  
- Payment Information  
- Payment Information - Details  
- Recurring Payments and Allowances  
- Recurring Deductions (Parent)  
- Recurring Deductions - Recurring Items (Child) (with end date)  
- Non Recurring Payments and Allowances  
- Super Fund Code  
- Emergency Contact  
- Phone Information  
- Email Information  
- Work Permit Information  
- Position - Compliance Requirements  
- Alternative Cost Distribution  
- Alternative Cost Distribution for Time  
        """)

        migration_row("Time Data", "td_demo", """
- Time Type  
- Time Account Type  
- Time Account (Accrual/Entitlement)  
- Time Account Details (Accrual/Entitlement)  
- Employee Time (Absences)  
        """)

        migration_row("Payroll Data", "ptd_demo", """
- Time Type  
- Time Account Type  
- Time Account (Accrual/Entitlement)  
- Time Account Details (Accrual/Entitlement)  
- Employee Time (Absences)  
        """)

    elif st.session_state.demo_page == "foundation_data_view":
        back_col, _ = st.columns([1, 5])
        with back_col:
            if st.button("⬅ Back to Demo", key="back_from_foundation", use_container_width=True):
                st.session_state.demo_page = "sap_to_sf"

        st.markdown("### Foundation Data – Interactive View")
        render()

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
            """)

            # --- INTERACTIVE BUTTONS WITH TOGGLE ---
            if "show_fd" not in st.session_state:
                st.session_state.show_fd = False
            if "show_emd" not in st.session_state:
                st.session_state.show_emd = False
            if "show_pd" not in st.session_state:
                st.session_state.show_pd = False
            if "show_ptd" not in st.session_state:
                st.session_state.show_ptd = False

            col_a, col_b = st.columns(2)
            with col_a:
                if st.button("Foundation Data", key="fd_btn"):
                    st.session_state.show_fd = not st.session_state.show_fd
                if st.session_state.show_fd:
                    st.info("""
- Org Hierarchy  
- Cost Center  
- Location  
- Pay Scale Info  
- Job Classification  
- Work Schedule
- Position Data
                    """)

                if st.button("Employee Data", key="pd_btn"):
                    st.session_state.show_pd = not st.session_state.show_pd
                if st.session_state.show_pd:
                    st.info("""
- Basic Information  
- Biographical Information  
- Job Information  
- Employment Information  
- Compensation Info  
- Payments  
- Superannuation  
- Tax Information  
- Time  
- Address Information  
- Email Information  
- Work Permit  
- Alternative Cost Distribution  
                    """)

            with col_b:
                if st.button("Time Data", key="emd_btn"):
                    st.session_state.show_emd = not st.session_state.show_emd
                if st.session_state.show_emd:
                    st.info("""
- Time Type  
- Time Account Type  
- Time Account (Accrual/Entitlement)  
- Time Account Details (Accrual/Entitlement)  
- Employee Time (Absences)  
                    """)

                if st.button("Payroll Data", key="ptd_btn"):
                    st.session_state.show_ptd = not st.session_state.show_ptd
                if st.session_state.show_ptd:
                    st.info("""
- Bank Info  
- Super Funds  
- Daily Work Schedule  
- Period Work Schedule  
- Work Schedule Rules  
- Cost Center  
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
