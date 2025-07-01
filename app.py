import streamlit as st
import base64
from streamlit_option_menu import option_menu
import os

st.set_page_config(layout="wide", page_title="MVS", page_icon="📊")
# --- REMOVE TOP WHITE SPACE ---
st.markdown("""
    <style>
        .block-container {
            padding-top: 0.5rem !important;
        }
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- BACKGROUND IMAGE ---
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

# Set the background
set_background("pexels-googledeepmind-17483873.jpg")

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
    st.markdown("""
        <div style='background-color:#e6f0ff;padding:15px;border-radius:10px;margin-bottom:20px;'>
            <div style='max-width:900px;margin:auto;'>
                <h2 style='text-align:center;'>Migration and Validation Suite</h2>
                <h3 style='text-align:center;'>MVS</h3> 
            </div>
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

        # --- Supported Migration Paths under image ---
        st.markdown("**Supported Migration Paths:**")
        st.markdown("""
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
