import streamlit as st
from streamlit_option_menu import option_menu
import base64

st.set_page_config(layout="wide")

# Navigation Menu
selected = option_menu(
    menu_title=None,
    options=["Home", "Solutions", "Services"],
    icons=["house", "layers", "wrench"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#f8f9fa"},
        "icon": {"color": "black", "font-size": "18px"},
        "nav-link": {"font-size": "18px", "text-align": "center", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#cfe2ff"},
    },
)

# Home Page
if selected == "Home":
    st.image("pexels-divinetechygirl-1181263.jpg", use_container_width=True)

    st.markdown("""
    <div style='background-color:#e6f0ff;padding:15px;border-radius:10px;'>
        <h2 style='text-align:center;'>Pioneering the Future of SAP HCM – From Data-Driven Migrations to Enterprise-Ready Variance Management</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🚀 Accelerate Your SAP Employee Central Migration")
    st.markdown("#### Purpose-built migration, validation and variance monitoring to make your SAP HCM transformation effortless.")

    icons_data = [
        ("streamline.png", "Streamline Your SAP HCM Migration"),
        ("testing.png", "De-Risk Parallel Testing"),
        ("security.png", "Ensure Data Security & Governance"),
        ("variance.png", "Monitor Field-Level Variance"),
        ("validation.png", "Smart Validation Engine"),
        ("confidence.png", "Enhance Stakeholder Confidence"),
    ]

    for i in range(0, len(icons_data), 3):
        cols = st.columns(3)
        for col, (icon, label) in zip(cols, icons_data[i:i+3]):
            with col:
                st.markdown(
                    f"""
                    <div style='text-align:center'>
                        <img src="data:image/png;base64,{base64.b64encode(open(icon, "rb").read()).decode()}" width="50" style="display:block;margin:auto;"/>
                        <p style="margin-top:10px;">{label}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    st.markdown("---")
    st.markdown("### 🌝 Why Choose Our Tool?")
    st.markdown("""
    - ✅ Seamless Data Transformation: Map, cleanse, and migrate with accuracy
    - 🔍 Built-in Validation: Eliminate bad data before it hits production
    - 🌟 Variance Detection: Compare ECC and EC data at a granular level
    """)

    st.markdown("<br>", unsafe_allow_html=True)
    cols = st.columns(3)
    with cols[0]:
        st.image("datamigration.png", width=60)
        st.markdown("**📄 Data Migration**")
        st.write("Template-driven, secure transfers from legacy to EC.")

    with cols[1]:
        st.image("validation.png", width=60)
        st.markdown("**✔ Validation**")
        st.write("Field-level checks to catch errors before go-live.")

    with cols[2]:
        st.image("pexels-divinetechygirl-1181341.jpg", width=60)
        st.markdown("**🌟 Variance Monitoring**")
        st.write("Automated comparisons between ECC and EC data.")

    st.markdown("""
    <div style='background-color:#002b5c;padding:40px;margin-top:40px;border-radius:10px;'>
        <h3 style='color:white;text-align:center;'>🌐 Built for SAP & SuccessFactors</h3>
        <p style='color:white;text-align:center;'>Our platform is fully compatible with modern SAP and SuccessFactors ecosystems, designed to simplify, safeguard, and speed up your transformation journey.</p>
        <div style='display:flex;justify-content:space-around;margin-top:30px;'>
            <div style='width:30%;text-align:center;'>
                <h4 style='color:white;'>🛠️ SAP EC Implementation</h4>
                <p style='color:white;'>Expert-driven configuration and deployment strategies tailored to Employee Central.</p>
            </div>
            <div style='width:30%;text-align:center;'>
                <h4 style='color:white;'>📃 Data Integrity & Compliance</h4>
                <p style='color:white;'>Granular field-level validation ensures readiness for audits and business continuity.</p>
            </div>
            <div style='width:30%;text-align:center;'>
                <h4 style='color:white;'>📄 Document-Ready Migrations</h4>
                <p style='color:white;'>Accelerate documentation processes with clean, structured output files ready for upload.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# You can continue adding the other tabs like "Solutions" and "Services" similarly
