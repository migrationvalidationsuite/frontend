with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Home", "Solutions", "Launch Pad"],  # ✅ renamed
        icons=["house", "layers", "rocket"],
        default_index=0,
        styles={...}
    )

# ✅ Reset to main scenario selector whenever Launch Pad is selected
if selected == "Launch Pad":
    st.session_state.demo_page = "main"

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
- Legal Entities  
- Business Units  
- Cost Centers  
- Locations  
- Pay Scales  
- Job Classifications  
- Work Schedule Objects
                    """)

                if st.button("Employee Master Data", key="emd_btn"):
                    st.session_state.show_emd = not st.session_state.show_emd
                if st.session_state.show_emd:
                    st.info("""
- Personal & Contact Information  
- Employee Assignments  
- Job and Pay Details  
- Employment History
                    """)

            with col_b:
                if st.button("Position Data", key="pd_btn"):
                    st.session_state.show_pd = not st.session_state.show_pd
                if st.session_state.show_pd:
                    st.info("""
- Hierarchies and Structures  
- Reporting Lines  
- Position Types and Groups  
- Relationships and Dependencies
                    """)

                if st.button("Payroll & Time Data", key="ptd_btn"):
                    st.session_state.show_ptd = not st.session_state.show_ptd
                if st.session_state.show_ptd:
                    st.info("""
- Attendance and Leave Balances  
- Absence Records  
- Payroll Fields  
- Calculation Fields
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

    # --- VALIDATION ---
    elif sol_choice == "Validation":
        col1, col2 = st.columns([3, 2.7])
        with col1:
            st.markdown("## Ensuring Data Accuracy Between Systems")
            st.markdown("""
Our validation services ensure HR data is correctly mapped, transformed, and loaded across every migration stage. We validate data between source systems, load files, and reporting outputs to confirm consistency and production readiness.

**What We Validate:**
- Required Fields: Detect missing/null values in critical fields  
- Format Compliance: Enforce expected types and structures  
- Mapping Accuracy: Verify source-to-target alignment  
- Source-to-File Match: Ensure extracted data mirrors load-ready files  
- Post-Load Validation: Confirm target system reflects intended records  
- Change Monitoring: Identify and isolate high-impact issues
            """)

        with col2:
            st.markdown("### Key Features")
            st.markdown("""
- Rules-Based Validation Engine  
- Categorized Exception Reporting  
- Iterative Revalidation Workflow  
- Full Audit Logging for Compliance  
- Support for all Employee Information
            """)
            st.image("validation_lifecycle.png", use_container_width=False, width=350)

    # --- DISCREPANCY ANALYSIS ---
    elif sol_choice == "Discrepancy Analysis Report":
        col1, col2 = st.columns([3, 2.6])
        with col1:
            st.markdown("## Reconciliation Across Systems")
            st.markdown("""
Our monitoring validates accurate data loads post-migration–across platforms like SuccessFactors, S/4HANA, or SAP HCM. It ensures alignment, traceability, and readiness for live HR/payroll processes.

**What We Monitor:**
- **Field-Level Accuracy:** Detect mismatches in critical values  
- **Record Completeness:** Spot missing/extra records  
- **Business-Critical Fields:** Focus on payroll, time, and org structures  
- **Change Tracking:** View changes before/after load

We cover field-level, record-level, and format-level checks to ensure clean post-migration integrity across HR modules.  
Visual dashboards and summary reports offer real-time reconciliation status for faster resolution and compliance.
            """)

        with col2:
            st.markdown("### Key Features")
            st.markdown("""
- Source-to-Target Comparisons  
- Discrepancy Summary Reports  
- Visual Reconciliation Dashboards  
- Logged Issues for Governance & Audit
            """)
            st.image("pexels-divinetechygirl-1181341.jpg", use_container_width=False, width=350)

