import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

# Navbar
selected = option_menu(
    menu_title=None,
    options=["Home", "Solutions", "Services"],
    icons=["house", "layers", "wrench"],
    orientation="horizontal",
)

if selected == "Home":
    # Header Banner
    st.markdown("""
        <div style="text-align: center; background-color: #e0edff; padding: 1rem; border-radius: 0.5rem;">
            <h2 style="color: #003366;">Pioneering the Future of SAP HCM – From Data-Driven Migrations to Enterprise-Ready Variance Management</h2>
        </div>
    """, unsafe_allow_html=True)

    # Banner image
    st.image("pexels-divinetechygirl-1181263.jpg", use_column_width=True)

    # Migration Section
    st.markdown("""
        <h3>🚀 Accelerate Your SAP Employee Central Migration</h3>
        <h5>Purpose-built migration, validation and variance monitoring to make your SAP HCM transformation effortless.</h5>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("streamline.png", width=60)
        st.caption("Streamline Your SAP HCM Migration")
        st.image("monitorvariance.png", width=60)
        st.caption("Monitor Field-Level Variance")
    with col2:
        st.image("derisk.png", width=60)
        st.caption("De-Risk Parallel Testing")
        st.image("validationengine.png", width=60)
        st.caption("Smart Validation Engine")
    with col3:
        st.image("security.png", width=60)
        st.caption("Ensure Data Security & Governance")
        st.image("confidence.png", width=60)
        st.caption("Enhance Stakeholder Confidence")

    st.markdown("---")

    # Why Choose Our Tool
    st.markdown("""
        <h4>💡 Why Choose Our Tool?</h4>
        <ul>
            <li>Seamless Data Transformation: Map, cleanse, and migrate with accuracy ✅</li>
            <li>Built-in Validation: Eliminate bad data before it hits production 🔍</li>
            <li>Variance Detection: Compare ECC and EC data at a granular level 🌃</li>
        </ul>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("datamigration.png", width=60)
        st.markdown("**Data Migration**")
        st.caption("Template-driven, secure transfers from legacy to EC.")
    with col2:
        st.image("validation.png", width=60)
        st.markdown("**Validation**")
        st.caption("Field-level checks to catch errors before go-live.")
    with col3:
        st.image("pexels-divinetechygirl-1181341.jpg", width=60)
        st.markdown("**Variance Monitoring**")
        st.caption("Automated comparisons between ECC and EC data.")

    st.markdown("---")

    # Built for SAP & SuccessFactors
    st.markdown("""
        <div style="background-color:#003366; color:white; padding:2rem; border-radius: 0.5rem;">
            <h4 style="text-align:center;">🌐 Built for SAP & SuccessFactors</h4>
            <p style="text-align:center;">Our platform is fully compatible with modern SAP and SuccessFactors ecosystems, designed to simplify, safeguard, and speed up your transformation journey.</p>
            <br>
            <div style="display:flex; justify-content: space-around;">
                <div style="width: 30%; text-align:center;">
                    <strong>⚒ SAP EC Implementation</strong>
                    <p>Expert-driven configuration and deployment strategies tailored to Employee Central.</p>
                </div>
                <div style="width: 30%; text-align:center;">
                    <strong>📃 Data Integrity & Compliance</strong>
                    <p>Granular field-level validation ensures readiness for audits and business continuity.</p>
                </div>
                <div style="width: 30%; text-align:center;">
                    <strong>📄 Document-Ready Migrations</strong>
                    <p>Accelerate documentation processes with clean, structured output files ready for upload.</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

elif selected == "Solutions":
    st.markdown("## Solutions")
    st.write("Details coming soon...")

elif selected == "Services":
    st.markdown("## Services")
    st.write("Details coming soon...")
