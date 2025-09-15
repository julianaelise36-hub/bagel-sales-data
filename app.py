streamlit run app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🥯 Bagel Sales Trends Dashboard")

df = pd.read_csv("bagel sales trends.csv")

st.subheader("Raw Data")
st.write(df.head())

if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])

if 'Date' in df.columns and 'Sales' in df.columns:
    df = df.sort_values('Date')
    st.subheader("Sales Over Time")
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Sales'])
    ax.set_xlabel("Date")
    ax.set_ylabel("Sales")
    st.pyplot(fig)
