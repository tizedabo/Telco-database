
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlalchemy as sa
import plotly.express as px
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:post@5432@localhost:5432/telecom')


query = "SELECT * FROM xdr_data"
df = pd.read_sql_query(query, engine)

# Handle missing values, outliers, and data inconsistencies
df.dropna(inplace=True)  # Replace with appropriate handling if necessary
df.drop_duplicates(inplace=True)

# Convert data types if needed
#df['column_name'] = df['column_name'].astype('category')



st.set_page_config(page_title="Tellco Dashboard", page_icon=":bar_chart:", layout="wide")
st.write("TELLCO DATA ANALYSIS DASHBORD")
#st.write(df)
#st.selectbox()   
#st.sidebar.title("Pages")
#st.slider("Select a value:", min_value=0, max_value=10)

# Set page title and layout
st.set_page_config(page_title="Telco Data Analysis Dashboard")
st.title("Telco Data Analysis")

# Create sidebar for filters
with st.sidebar:
    st.header("Filters")
    options = ["user engagement", "Handset overview", "application usage"]
selected_option = st.selectbox("Select an option:", options)
user_engagement_df = df[['Bearer Id', 'MSISDN/Number', 'Dur. (ms)', 'Total UL (Bytes)','Total DL (Bytes)']]
user_engagement_df = user_engagement_df.groupby(
    'MSISDN/Number').agg({'Bearer Id': 'count', 'Dur. (ms)': 'sum', 'Total UL (Bytes)': 'sum','Total DL (Bytes)':'sum'})
user_engagement_df = user_engagement_df.rename(
    columns={'Bearer Id': 'xDR Sessions'})
user_engagement_df.head()


user_app_engagement_df = df[['MSISDN/Number', 'Social Media DL (Bytes)', 'Google DL (Bytes)',
    'Email DL (Bytes)', 'Youtube DL (Bytes)', 'Netflix DL (Bytes)',
    'Gaming DL (Bytes)', 'Other DL (Bytes)']]

user_app_engagement_df = user_app_engagement_df.groupby(
    'MSISDN/Number').sum()
user_app_engagement_df.head()

top_manufacturers = df.groupby('Handset Manufacturer')['IMEI'].count().nlargest(3).reset_index()
top_manufacturers.columns = ['manufacturer', 'usage_count']
print("Top 3 Handset Manufacturers:")
print(top_manufacturers)

# Filter data based on user inputs

filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date) & (df['customer_segment'] == customer_segment)]

# Display key metrics
st.header("Key Metrics")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Revenue", filtered_df['total_revenue'].sum())
with col2:
    st.metric("Total Customers", filtered_df['customer_id'].nunique())
with col3:
    st.metric("Churn Rate", filtered_df['churn'].mean() * 100, "%")

# Create visualizations
st.header("Visualizations")
st.subheader("Customer Segmentation")
fig1 = px.pie(filtered_df, names='customer_segment', values='total_revenue', title="Customer Segmentation by Revenue")
st.plotly_chart(fig1)

st.subheader("Churn Analysis")
fig2 = px.bar(filtered_df, x='churn', y='total_revenue', title="Churn Analysis by Revenue")
st.plotly_chart(fig2)

# Add more visualizations as needed
