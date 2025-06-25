import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="SAP EC Migration Demo", layout="wide")

# --- NAVBAR ---
selected = option_menu(
    menu_title=None,
    options=["Home", "Solutions", "Insights"],
    icons=["house", "grid-3x3-gap", "lightbulb"],
    orientation="horizontal",
    default_index=0,
    styles={
        "container": {"padding": "0!important", "background-color": "#f9f9f9"},
        "nav-link": {"font-size": "16px", "font-weight": "600", "color": "black"},
        "nav-link-selected": {"background-color": "#e0e0e0"},
    }
)

# --- PAGE ROUTING ---
if selected == "Home":
    st.title("SAP EC Migration & Monitoring Tool")
    st.subheader("Streamlined, Compliant, and Scalable HR Data Transformation")
    st.markdown("""
        Welcome to our cloud-based platform for SAP SuccessFactors transformation. Explore tools for:
        - Foundation & Position Data Migration
        - Validation Rule Automation
        - ECC-to-EC Variance Auditing
    """)
    st.image("landing_image.png", use_container_width=True)  # Optional
    st.markdown("Explore more via the Solutions tab.")

elif selected == "Solutions":
    sol_choice = option_menu(
        menu_title="Our Solutions",
        options=["Data Migration", "Validation", "Variance Monitoring"],
        orientation="horizontal"
    )

    if sol_choice == "Data Migration":
        st.header("📂 Employee Central Data Migration")
        st.markdown("""
        Our tool supports clean, auditable migration of:
        - Foundation Objects (Legal Entity, Business Unit, etc.)
        - Position Hierarchies
        - Employee Core Profiles
        """)
        st.image("Employee_Central_Data_Migration.png", caption="Data Migration Flow", use_container_width=True)

    elif sol_choice == "Validation":
        st.header("✅ Validation Services")
        st.markdown("""
        Ensure every record complies with schema rules and HR logic:
        - Null field detection
        - Format & Type mismatches
        - Referential Integrity (e.g., position-to-employee links)
        """)
        st.image("validation_lifecycle.png", caption="Validation Flow", use_container_width=True)

    elif sol_choice == "Variance Monitoring":
        st.header("📊 ECC to EC Variance Monitoring")
        st.markdown("""
        Track field-level mismatches post-migration:
        - Value Differences (before vs. after)
        - Missing/Extra Records
        - Formatting or Logical Gaps
        """)
        st.image("variance_monitoring.png", caption="Variance Workflow", use_container_width=True)

elif selected == "Insights":
    st.header("Insights & Use Cases")
    st.markdown("""
    Coming soon: Explore how global organizations simplify SAP transformation with our tools.
    """)

