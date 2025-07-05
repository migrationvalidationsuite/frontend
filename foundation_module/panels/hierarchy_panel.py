import streamlit as st
import pandas as pd
from utils.file_utils import load_data, create_download_button
from utils.hierarchy_utils import build_hierarchy, optimize_table_display

def show_hierarchy_panel(state):
    st.header("Hierarchy Builder")
    
    # File upload section with clear instructions
    with st.expander("📤 Upload Files", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            hrp1000_file = st.file_uploader(
                "Upload HRP1000 (Org Units)",
                type=["csv", "xlsx"],
                help="Must contain 'Object ID' and 'Name' columns"
            )
        with col2:
            hrp1001_file = st.file_uploader(
                "Upload HRP1001 (Relationships)", 
                type=["csv", "xlsx"],
                help="Must contain 'Source ID' and 'Target object ID' columns"
            )
    
    # Build hierarchy button with validation
    if st.button("🚀 Build Hierarchy", type="primary", use_container_width=True):
        if not hrp1000_file or not hrp1001_file:
            st.error("Please upload both files to proceed")
            return
            
        with st.spinner("Building organizational hierarchy..."):
            try:
                # Load data with validation
                hrp1000 = load_data(hrp1000_file)
                hrp1001 = load_data(hrp1001_file)
                
                # Validate required columns
                required_hrp1000 = ['Object ID', 'Name']
                missing_hrp1000 = [col for col in required_hrp1000 if col not in hrp1000.columns]
                if missing_hrp1000:
                    raise ValueError(f"HRP1000 missing required columns: {', '.join(missing_hrp1000)}")
                
                required_hrp1001 = ['Source ID', 'Target object ID']
                missing_hrp1001 = [col for col in required_hrp1001 if col not in hrp1001.columns]
                if missing_hrp1001:
                    raise ValueError(f"HRP1001 missing required columns: {', '.join(missing_hrp1001)}")
                
                # Convert date columns if they exist
                date_cols = ['Start date', 'End Date', 'Changed on']
                for col in date_cols:
                    if col in hrp1000:
                        hrp1000[col] = pd.to_datetime(hrp1000[col], format='%d/%m/%Y', errors='coerce')
                    if col in hrp1001:
                        hrp1001[col] = pd.to_datetime(hrp1001[col], format='%d/%m/%Y', errors='coerce')
                
                # Store data and build hierarchy
                state['hrp1000'] = hrp1000
                state['hrp1001'] = hrp1001
                state['hierarchy'] = build_hierarchy(hrp1000, hrp1001)
                
                st.success("Hierarchy built successfully!")
                
            except ValueError as ve:
                st.error(f"Validation error: {str(ve)}")
                st.info("Please check your files contain all required columns")
            except Exception as e:
                st.error(f"Failed to build hierarchy: {str(e)}")
                st.stop()
    
    # Hierarchy display and customization
    if state.get('hierarchy'):
        st.divider()
        
        # Level renaming interface
        with st.expander("🔠 Customize Level Names", expanded=False):
            cols = st.columns(4)
            for level in range(1, 21):
                with cols[(level-1) % 4]:
                    state['level_names'][level] = st.text_input(
                        f"Level {level}",
                        value=state['level_names'].get(level, f"Level {level}"),
                        key=f"level_name_{level}"
                    )
        
        # Interactive tabs
        tab1, tab2 = st.tabs(["📋 Hierarchy Table", "🔗 Relationships"])
        
        with tab1:
            # Apply level names to display
            display_df = state['hierarchy']['hierarchy_table'].copy()
            display_df['Level'] = display_df['Level'].map(state['level_names'])
            display_df = optimize_table_display(display_df)
            
            st.dataframe(
                display_df,
                height=600,
                use_container_width=True,
                hide_index=True
            )
            
            # Download buttons
            st.divider()
            st.subheader("Export Data")
            create_download_button(
                data=state['hierarchy']['hierarchy_table'],
                file_name="org_hierarchy",
                file_type="csv"
            )
            create_download_button(
                data=state['hierarchy']['hierarchy_table'],
                file_name="org_hierarchy",
                file_type="excel"
            )
        
        with tab2:
            display_assoc = state['hierarchy']['level_associations'].copy()
            display_assoc['Level'] = display_assoc['Level'].map(state['level_names'])
            display_assoc = optimize_table_display(display_assoc)
            
            st.dataframe(
                display_assoc,
                height=600,
                use_container_width=True,
                hide_index=True
            )
            
            st.divider()
            st.subheader("Export Relationships")
            create_download_button(
                data=state['hierarchy']['level_associations'],
                file_name="org_relationships",
                file_type="csv"
            )