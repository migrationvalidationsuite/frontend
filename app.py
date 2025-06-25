
import streamlit as st
from streamlit_option_menu import option_menu
import base64

def load_image_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

st.set_page_config(
    page_title="SAP EC Migration & Monitoring",
    page_icon="📊",
    layout="wide"
)

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

if selected == "Home":
    st.markdown(
        '<div style="background-color:#e6f0ff;padding:25px;border-radius:10px;text-align:center">'
        '<h2 style="color:#003366;">Pioneering the Future of SAP HCM – From Data-Driven Migrations to Enterprise-Ready Variance Management</h2>'
        '</div>',
        unsafe_allow_html=True
    )

    st.image("pexels-divinetechygirl-1181263.jpg", use_container_width=True)

    st.markdown("### 🚀 Accelerate Your SAP Employee Central Migration")
    st.markdown("#### Purpose-built migration, validation and variance monitoring to make your SAP HCM transformation effortless.")

    features = [
        ("streamline.png", "Streamline Your SAP HCM Migration"),
        ("testing.png", "De-Risk Parallel Testing"),
        ("security.png", "Ensure Data Security & Governance"),
        ("variance.png", "Monitor Field-Level Variance"),
        ("validation.png", "Smart Validation Engine"),
        ("confidence.png", "Enhance Stakeholder Confidence"),
    ]

    for i in range(0, len(features), 3):
        cols = st.columns(3)
        for col, (icon, text) in zip(cols, features[i:i+3]):
            encoded = load_image_base64(icon)
            col.markdown(f'''
                <div style='text-align:center'>
                    <img src='data:image/png;base64,{encoded}' width='50'/>
                    <p>{text}</p>
                </div>
            ''', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 💡 Why Choose Our Tool?")
    st.markdown("""
- ✅ Seamless Data Transformation: Map, cleanse, and migrate with accuracy  
- 🔍 Built-in Validation: Eliminate bad data before it hits production  
- 📊 Variance Detection: Compare ECC and EC data at a granular level  
""")

    col1, col2, col3 = st.columns(3)
    cards = [
        ("data_icon.png", "📄 Data Migration", "Template-driven, secure transfers from legacy to EC."),
        ("check_icon.png", "✔️ Validation", "Field-level checks to catch errors before go-live."),
        ("chart_icon.png", "📊 Variance Monitoring", "Automated comparisons between ECC and EC data.")
    ]

    for col, (icon, heading, desc) in zip([col1, col2, col3], cards):
        encoded = load_image_base64(icon)
        col.markdown(f'''
            <div style='text-align:center'>
                <img src='data:image/png;base64,{encoded}' width='50'/>
                <h5>{heading}</h5>
                <p>{desc}</p>
            </div>
        ''', unsafe_allow_html=True)

    st.markdown(
        '''
        <div style="background-color:#001f4d;color:white;padding:40px;text-align:center;border-radius:8px;margin-top:40px;">
            <h3>🌐 Built for SAP & SuccessFactors</h3>
            <p>Our platform is fully compatible with modern SAP and SuccessFactors ecosystems, designed to simplify, safeguard, and speed up your transformation journey.</p>
            <div style="display:flex;justify-content:center;gap:60px;flex-wrap:wrap;margin-top:30px;">
                <div style="flex:1;min-width:250px;">
                    <h4>🛠️ SAP EC Implementation</h4>
                    <p>Expert-driven configuration and deployment strategies tailored to Employee Central.</p>
                </div>
                <div style="flex:1;min-width:250px;">
                    <h4>📋 Data Integrity & Compliance</h4>
                    <p>Granular field-level validation ensures readiness for audits and business continuity.</p>
                </div>
                <div style="flex:1;min-width:250px;">
                    <h4>🗂️ Document-Ready Migrations</h4>
                    <p>Accelerate documentation processes with clean, structured output files ready for upload.</p>
                </div>
            </div>
        </div>
        ''',
        unsafe_allow_html=True
    )
