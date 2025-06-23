import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="YouTube Ads Dashboard", layout="wide")

st.title("📊 YouTube Ads Performance Dashboard")
st.markdown("Upload your YouTube ads CSV file (Date, Impressions, Views, Clicks, Cost).")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=["Date"])
    df["CTR (%)"] = (df["Clicks"] / df["Impressions"]) * 100
    df["CPV"] = df["Cost"] / df["Views"]
    df["CPC"] = df["Cost"] / df["Clicks"]
    df["View Rate (%)"] = (df["Views"] / df["Impressions"]) * 100

    st.subheader("📈 Key Metrics")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Impressions", f'{df["Impressions"].sum():,}')
    col2.metric("Total Views", f'{df["Views"].sum():,}')
    col3.metric("Total Clicks", f'{df["Clicks"].sum():,}')
    col4.metric("Total Cost", f'₹{df["Cost"].sum():,.2f}')

    st.subheader("📊 Trends Over Time")
    fig1 = px.line(df, x="Date", y="CTR (%)", color="Campaign", title="CTR (%) Over Time")
    fig2 = px.line(df, x="Date", y="CPV", color="Campaign", title="CPV Over Time")
    fig3 = px.line(df, x="Date", y="View Rate (%)", color="Campaign", title="View Rate (%)")

    st.plotly_chart(fig1, use_container_width=True)
    st.plotly_chart(fig2, use_container_width=True)
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("📄 Data Preview")
    st.dataframe(df)
else:
    st.warning("📁 Please upload a CSV file to see insights.")
