import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Diabetes Lifestyle Analysis", layout="wide")

st.title("🩺 Lifestyle & Diabetes Risk Dashboard")
st.markdown("""
This dashboard focuses on how lifestyle choices and work environments impact diabetes risk.
- **Key Metrics:** Vitality Score (Leisure), Overworked Status, BMI Group
- **Data Source:** Databricks Gold Layer
""")

# 2. Data Loading
@st.cache_data
def load_data():
    try:
        # Loading the gold.csv file
        return pd.read_csv("gold.csv")
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

df = load_data()

if df is not None:
    # 3. Sidebar Filters
    st.sidebar.header("Filter Options")
    gender_list = df['gender'].unique()
    selected_gender = st.sidebar.multiselect("Select Gender", options=gender_list, default=gender_list)
    
    bmi_list = df['bmi_group'].unique()
    selected_bmi = st.sidebar.multiselect("Select BMI Group", options=bmi_list, default=bmi_list)

    mask = (df['gender'].isin(selected_gender)) & (df['bmi_group'].isin(selected_bmi))
    filtered_df = df[mask]

    # 4. Top Level Metrics
    m1, m2, m3 = st.columns(3)
    m1.metric("Total Samples", f"{len(filtered_df):,}")
    m2.metric("Avg Leisure Vitality", round(filtered_df['leisure_vitality_score'].mean(), 2))
    overworked_ratio = filtered_df['is_overworked'].mean() * 100
    m3.metric("Overworked Ratio", f"{round(overworked_ratio, 1)}%")

    st.divider()

    # 5. Visualizations
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Diabetes Rate by Leisure Vitality")
        # Line chart showing the trend of diabetes rate decreasing as vitality increases
        chart_data = filtered_df.groupby(filtered_df['leisure_vitality_score'].apply(int))['diabetes_status'].mean().reset_index()
        fig1 = px.line(chart_data, x='leisure_vitality_score', y='diabetes_status', 
                      labels={'leisure_vitality_score': 'Vitality Level (Exercise)', 'diabetes_status': 'Diabetes Rate'},
                      markers=True, template="plotly_white")
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("💼 Diabetes Rate: Overworked vs. Normal")
        # Simple Bar Chart to show the impact of overworking
        # 0 = Normal, 1 = Overworked
        work_data = filtered_df.groupby('is_overworked')['diabetes_status'].mean().reset_index()
        work_data['is_overworked'] = work_data['is_overworked'].map({0: 'Normal Work', 1: 'Overworked (>40h)'})
        
        fig2 = px.bar(work_data, x='is_overworked', y='diabetes_status',
                     color='is_overworked',
                     labels={'diabetes_status': 'Diabetes Probability', 'is_overworked': 'Work Status'},
                     color_discrete_map={'Normal Work': '#636EFA', 'Overworked (>40h)': '#EF553B'})
        st.plotly_chart(fig2, use_container_width=True)

    # 6. BMI Distribution (Moved to bottom)
    st.subheader("🍰 Distribution of BMI Groups in Selected Data")
    fig3 = px.pie(filtered_df, names='bmi_group', hole=0.4, color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig3, use_container_width=True)

    # 7. Data Inspector
    with st.expander("View Raw Data Details"):
        st.dataframe(filtered_df.head(100))

else:
    st.warning("⚠️ Please ensure 'gold.csv' is in the same folder as app.py")