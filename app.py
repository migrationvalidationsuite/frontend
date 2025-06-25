import streamlit as st
from streamlit_option_menu import option_menu
import os

st.set_page_config(
    page_title="SAP EC Migration & Monitoring",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- GLOBAL STYLE ---
st.markdown("""
    <style>
        .main {
            background-color: #f7fbff;
        }
        .css-18e3th9 {
            padding: 2rem 1rem 2rem 1rem;
        }
        .css-1d391kg h2 {
            color: #003366;
        }
        .feature-block {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- NAVIGATION MENU ---
selected = option_menu(
    menu_title=None,
    options=["Home", "Solutions", "Services"],
    icons=["house-door-fill", "layers-fill", "tools"],
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#e3f2fd"},
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

    st.markdown("## 🚀 Accelerate Your SAP Employee Central Migration")
    st.markdown("""
    <p style="font-size:17px; font-weight:500">Purpose-built migration, validation and variance monitoring to make your SAP HCM transformation effortless.</p>
    """, unsafe_allow_html=True)

    # --- Feature Grid ---
    features = [
        ("migration.png", "Streamline Your SAP HCM Migration"),
        ("testing.png", "De-Risk Parallel Testing"),
        ("security.png", "Ensure Data Security & Governance"),
        ("variance.png", "Monitor Field-Level Variance"),
        ("validation.png", "Smart Validation Engine"),
        ("confidence.png", "Enhance Stakeholder Confidence")
    ]

    for i in range(0, len(features), 3):
        cols = st.columns(3)
        for col, (icon_path, label) in zip(cols, features[i:i+3]):
            with col:
                st.markdown(f"<div class='feature-block'>", unsafe_allow_html=True)
                if os.path.exists(icon_path):
                    st.image(icon_path, width=60)
                else:
                    st.markdown("🔹")
                st.markdown(f"<p style='font-size:14px; font-weight:500'>{label}</p>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")

    # --- WHY CHOOSE OUR TOOL ---
    st.markdown("""
    <h4>💡 Why Choose Our Tool?</h4>
    <ul>
        <li>✅ Seamless Data Transformation: Map, cleanse, and migrate with accuracy</li>
        <li>🔍 Built-in Validation: Eliminate bad data before it hits production</li>
        <li>📊 Variance Detection: Compare ECC and EC data at a granular level</li>
    </ul>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    for col, icon, heading, desc in zip(
        [col1, col2, col3],
        ["data_icon.png", "check_icon.png", "chart_icon.png"],
        ["Data Migration", "Validation", "Variance Monitoring"],
        [
            "Template-driven, secure transfers from legacy to EC.",
            "Field-level checks to catch errors before go-live.",
            "Automated comparisons between ECC and EC data."
        ]
    ):
        with col:
            st.markdown("<div class='feature-block'>", unsafe_allow_html=True)
            if os.path.exists(icon):
                st.image(icon, width=50)
            else:
                st.markdown("📦")
            st.markdown(f"<h5>{heading}</h5>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size:14px'>{desc}</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

# Other pages (Solutions and Services) remain unchanged for now.
# Let me know if you want them updated visually/stylistically too.
