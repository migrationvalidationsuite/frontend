import streamlit as st
import base64
import os
from streamlit_option_menu import option_menu

# --- PAGE CONFIG ---
st.set_page_config(layout="wide", page_title="MVS", page_icon="📊")

# --- BACKGROUND IMAGE AS BASE64 ---
def get_base64_bg(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

bg_base64 = get_base64_bg("pexels-cookiecutter-1148820.jpg")

# --- CUSTOM STYLE ---
st.markdown(f"""
    <style>
        .block-container {{
            padding-top: 1rem;
        }}

        .main-banner {{
            background-color: #e6f0ff;
            padding: 15px 0;
            width: 100%;
            border-radius: 12px;
            text-align: center;
            margin-bottom: 30px;
        }}

        body {{
            background-image: url("data:image/jpeg;base64,{bg_base64}");
            background-size: cover;
            background-attachment: fixed;
            background-repeat: no-repeat;
        }}

        .video-center {{
            display: flex;
            justify-content: center;
            padding-top: 20px;
        }}
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAV ---
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
        }
    )

# --- HOME PAGE ---
if selected == "Home":
    st.markdown("""
        <div class="main-banner">
            <h2>Migration and Validation Suite</h2>
            <h4>MVS</h4>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
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

    with col2:
        st.image("pexels-divinetechygirl-1181263.jpg", width=360)

    st.markdown("**Supported Migration Paths:**")
    st.markdown("""
    - SAP HCM → SuccessFactors  
    - SAP HCM → S/4HANA  
    - Legacy HR Systems → SAP Cloud or On-Prem
    """)

    # --- EMBEDDED VIDEO CENTERED ---
    st.markdown("""
        <div class="video-center">
            <iframe width="560" height="315" src="https://www.youtube.com/embed/vnikhnk8rCk" frameborder="0" allowfullscreen></iframe>
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
