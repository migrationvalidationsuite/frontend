import streamlit as st
from streamlit_option_menu import option_menu
import os

st.set_page_config(
    page_title="SAP EC Migration & Monitoring",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="auto"
)

# --- NAVIGATION MENU ---
selected = option_menu(
    menu_title=None,
    options=["Home", "Solutions", "Services"],
    icons=["house-door-fill", "layers-fill", "tools"],
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#f0f4f8"},
        "nav-link": {"font-size": "18px", "font-weight": "600", "color": "#003366", "margin": "0 20px"},
        "nav-link-selected": {"background-color": "#cce0ff", "border-radius": "8px"},
    }
)

# --- HOME PAGE ---
if selected == "Home":
    st.markdown("""
        <div style="background-color:#e6f0ff;padding:25px;border-radius:10px;text-align:center">
            <h2 style="color:#003366;">Pioneering the Future of SAP HCM – From Data-Driven Migrations to Enterprise-Ready Variance Management</h2>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='padding: 20px;'>
        <h3>🚀 Accelerate Your SAP Employee Central Migration</h3>
        <p><strong>Purpose-built migration, validation and variance monitoring to make your SAP HCM transformation effortless.</strong></p>
    </div>
    """, unsafe_allow_html=True)

    features = [
        ("streamline.png", "Streamline Your SAP HCM Migration"),
        ("testing.png", "De-Risk Parallel Testing"),
        ("security.png", "Ensure Data Security & Governance"),
        ("variance.png", "Monitor Field-Level Variance"),
        ("validation.png", "Smart Validation Engine"),
        ("confidence.png", "Enhance Stakeholder Confidence"),
    ]

    # Split into two rows with 3 columns each
    for row in range(2):
        cols = st.columns(3)
        for i in range(3):
            idx = row * 3 + i
            if idx < len(features):
                icon_path, label = features[idx]
                with cols[i]:
                    if os.path.exists(icon_path):
                        st.image(icon_path, width=60)
                    else:
                        st.write("🚫")
                    st.markdown(f"<p style='text-align:center;'>{label}</p>", unsafe_allow_html=True)

    st.markdown("---")

    # WHY CHOOSE US
    st.markdown("""
    <div style='padding: 10px 0;'>
        <h4>💡 Why Choose Our Tool?</h4>
        <ul>
            <li>✅ Seamless Data Transformation: Map, cleanse, and migrate with accuracy</li>
            <li>🔍 Built-in Validation: Eliminate bad data before it hits production</li>
            <li>📊 Variance Detection: Compare ECC and EC data at a granular level</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    icons = ["data_icon.png", "check_icon.png", "chart_icon.png"]
    headings = ["Data Migration", "Validation", "Variance Monitoring"]
    descriptions = [
        "Template-driven, secure transfers from legacy to EC.",
        "Field-level checks to catch errors before go-live.",
        "Automated comparisons between ECC and EC data."
    ]

    for col, icon, heading, desc in zip([col1, col2, col3], icons, headings, descriptions):
        with col:
            if os.path.exists(icon):
                st.image(icon, width=60)
            else:
                st.write("📁")
            st.markdown(f"<h5 style='text-align:center;'>{heading}</h5>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align:center;'>{desc}</p>", unsafe_allow_html=True)

    st.markdown("""
        <style>
            .block-container {
                background-color: #f8fbff;
                padding: 2rem;
            }
        </style>
    """, unsafe_allow_html=True)
