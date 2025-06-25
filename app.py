import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="SAP EC Migration Demo", layout="wide")

# --- NAVIGATION MENU ---
selected = option_menu(
    menu_title=None,
    options=["Home", "Solutions", "Insights"],
    icons=["house", "briefcase", "lightbulb"],
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#ffffff"},
        "nav-link": {"font-size": "18px", "font-weight": "600", "color": "black"},
        "nav-link-selected": {"background-color": "#e6f0ff"},
    }
)

# --- HOME PAGE ---
if selected == "Home":
    st.markdown("## Accelerate Your SAP Employee Central Migration")
    st.markdown("""
        #### Purpose-built migration, validation and variance monitoring to make your SAP HCM transformation effortless.
    """)
    st.image("landing_hero.png", use_container_width=True)

    st.markdown("---")
    st.subheader("Why Choose Our Tool?")
    st.markdown("""
    - 🔄 Seamless Data Transformation: Map, cleanse, and migrate with accuracy.
    - ✅ Built-in Validation: Eliminate bad data before it hits production.
    - 📊 Variance Detection: Compare ECC and EC data at a granular level.
    """)
    st.markdown("Explore the 'Solutions' tab above for a detailed walkthrough.")

# --- SOLUTIONS PAGE ---
elif selected == "Solutions":
    sol_choice = option_menu(
        menu_title="Our Solutions",
        options=["Data Migration", "Validation", "Variance Monitoring"],
        icons=["upload", "check2-circle", "bar-chart-line"],
        orientation="horizontal"
    )

    if sol_choice == "Data Migration":
        st.header("📂 Employee Central Data Migration")
        st.markdown("""
        Our tool supports secure, auditable migration of:
        - Foundation Objects (Legal Entity, Business Unit, Location)
        - Hierarchical Position Structures
        - Employee Master Data and Assignments

        With robust templates, custom mappings, and field-level traceability.
        """)
        st.image("Employee_Central_Data_Migration.png", caption="Migration Flow", use_container_width=True)

    elif sol_choice == "Validation":
        st.header("✅ Validation Services")
        st.markdown("""
        Ensure every single record complies with:
        - Required field presence (null detection)
        - Data types and value formatting
        - Referential logic (e.g., employee reports-to validation)
        
        Prevent downstream errors with pre-upload quality checks.
        """)
        st.image("validation_lifecycle.png", caption="Validation Lifecycle", use_container_width=True)

    elif sol_choice == "Variance Monitoring":
        st.header("📊 ECC to EC Variance Monitoring")
        st.markdown("""
        After your migration, compare SAP ECC and EC data:
        - Detect mismatches in values and field formats
        - Identify extra/missing records across modules
        - Focus on critical payroll-impacting fields

        Variance dashboards help you close the loop with confidence.
        """)
        st.image("variance_monitoring.png", caption="Variance Audit Flow", use_container_width=True)

# --- INSIGHTS PAGE ---
elif selected == "Insights":
    st.header("📘 Insights & Use Cases")
    st.markdown("""
    > Coming soon: Explore real-world SAP SuccessFactors projects powered by our platform.

    - How a retail company migrated 50,000+ records in 2 weeks
    - Lessons from parallel testing in payroll-critical environments
    - What to automate vs. manually validate in SAP EC

    Bookmark this space!
    """)
