import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import difflib
from io import StringIO

# Optional: Import LLM if available
try:
    from langchain.llms import Ollama
    from langchain.chains import LLMChain
    from langchain.prompts import PromptTemplate
    llm_enabled = True
except:
    llm_enabled = False

st.set_page_config(page_title="Enhanced Payroll Mapper", layout="wide")
st.title("🔍 Enhanced Payroll Mapping & Cleansing Tool")

# === Sidebar Cleansing Options ===
with st.sidebar:
    st.header("Cleansing Options")
    trim_whitespace = st.checkbox("Trim Whitespace", True)
    lowercase = st.checkbox("Standardize Casing (lowercase)", True)
    empty_to_nan = st.checkbox("Convert empty to NaN", True)
    drop_null_rows = st.checkbox("Drop rows with missing required fields", False)

uploaded_0008 = st.file_uploader("Upload PA0008.xlsx", type=["xlsx"])
uploaded_0014 = st.file_uploader("Upload PA0014.xlsx", type=["xlsx"])

@st.cache_data
def load_data(file):
    return pd.read_excel(file)

def cleanse_dataframe(df):
    df_clean = df.copy()
    for col in df_clean.columns:
        if df_clean[col].dtype == 'object':
            if trim_whitespace:
                df_clean[col] = df_clean[col].astype(str).str.strip()
            if lowercase:
                df_clean[col] = df_clean[col].astype(str).str.lower()
    if empty_to_nan:
        df_clean.replace("", np.nan, inplace=True)
    if drop_null_rows:
        df_clean.dropna(inplace=True)
    return df_clean

def show_comparison(original, cleansed):
    diff_df = original.copy()
    for col in original.columns:
        if col in cleansed.columns:
            diff_df[col] = np.where(original[col] != cleansed[col], "🟡 " + cleansed[col].astype(str), cleansed[col])
    return diff_df

def display_metadata(df, label):
    st.subheader(f"🧾 Metadata for {label}")
    st.markdown("""
    - **Data Types** show what kind of values each column holds (e.g., string, integer).
    - **Null Count** helps identify where data is missing.
    - **Unique Values** tells you the variety in each column.
    """)
    st.write("**Data Types:**")
    st.write(df.dtypes)
    st.write("**Null Count:**")
    st.write(df.isnull().sum())
    st.write("**Unique Values:**")
    st.write(df.nunique())

def show_dashboard(df):
    st.subheader("📊 Dashboard: Visual Overview of Cleansing Impact")
    selected_col = st.selectbox("Select column to explore:", df.columns)

    st.markdown("**Null Count Chart**")
    nulls = df.isnull().sum()
    fig = px.bar(x=nulls.index, y=nulls.values, labels={"x": "Field", "y": "Null Count"}, title="Nulls per Column")
    st.plotly_chart(fig)

    st.markdown("**Value Distribution**")
    if pd.api.types.is_numeric_dtype(df[selected_col]):
        fig2 = px.histogram(df, x=selected_col, title=f"{selected_col} Distribution")
        st.plotly_chart(fig2)
    else:
        top_vals = df[selected_col].value_counts().nlargest(10)
        fig2 = px.bar(x=top_vals.index, y=top_vals.values, title=f"Top Values in {selected_col}")
        st.plotly_chart(fig2)

def descriptive_statistics(df):
    st.subheader("📈 Descriptive Statistics")
    st.markdown("This table summarizes the key metrics across your data, including count, mean, std deviation etc.")
    st.dataframe(df.describe(include='all'))

def show_validation(df):
    st.subheader("✅ Validation Panel")
    st.markdown("We validate your cleansed data by highlighting common issues like missing values or negatives.")

    st.write("**Missing Values Summary**")
    st.dataframe(df.isnull().sum())

    if 'amount' in df.columns:
        st.write("**Negative Amounts (if any):**")
        st.dataframe(df[df['amount'] < 0])

    st.markdown("**Data Lineage Note:**")
    st.info("All cleansed columns were transformed based on options selected in the sidebar. Values were stripped, lowercased, and cleaned before validation.")

def get_nlp_answer(query, df):
    if not llm_enabled:
        return "❌ Ollama not available. Please install LangChain and run `ollama run mistral` locally."
    llm = Ollama(model="mistral")
    context = f"Data columns: {', '.join(df.columns)}\nPreview:\n{df.head().to_string()}"
    prompt = PromptTemplate(
        input_variables=["question", "context"],
        template="""You are a helpful data assistant. Given the following data context:

{context}

Answer the following question in detail:

{question}
"""
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run({"question": query, "context": context})

# === MAIN LOGIC ===
if uploaded_0008 and uploaded_0014:
    df_0008 = load_data(uploaded_0008)
    df_0014 = load_data(uploaded_0014)

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Cleanse", "Metadata", "Validation", "Dashboard", "Statistics", "Ask Your Data"])

    with tab1:
        st.subheader("🧹 Cleanse & Compare")
        df_0008_clean = cleanse_dataframe(df_0008)
        df_0014_clean = cleanse_dataframe(df_0014)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**PA0008 - Original**")
            st.dataframe(df_0008)
        with col2:
            st.markdown("**PA0008 - Cleansed**")
            st.dataframe(show_comparison(df_0008, df_0008_clean))

        col3, col4 = st.columns(2)
        with col3:
            st.markdown("**PA0014 - Original**")
            st.dataframe(df_0014)
        with col4:
            st.markdown("**PA0014 - Cleansed**")
            st.dataframe(show_comparison(df_0014, df_0014_clean))

    with tab2:
        display_metadata(df_0008_clean, "PA0008")
        display_metadata(df_0014_clean, "PA0014")

    with tab3:
        show_validation(df_0008_clean)

    with tab4:
        show_dashboard(df_0008_clean)

    with tab5:
        descriptive_statistics(df_0008_clean)

    with tab6:
        st.subheader("💬 Ask Your Data")
        user_query = st.text_input("Ask a question about the data:")
        if user_query:
            answer = get_nlp_answer(user_query, df_0008_clean)
            st.markdown("**Answer:**")
            st.write(answer)
