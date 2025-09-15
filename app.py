import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt

# Load the CSV file as raw text
with open("bagel sales trends.csv", "r") as file:
    raw = file.read()

# Find where the first monthly sales table starts
lines = raw.splitlines()
start = None
for i, line in enumerate(lines):
    if "Current,Current Gross sales" in line:
        start = i + 1
        break

# Get 12 rows of monthly data
monthly_data = lines[start:start + 12]

# Clean and parse the data
data = []
for row in monthly_data:
    cols = row.split(",")
    if len(cols) >= 2:
        month = cols[0].strip()
        value = cols[1].replace("$", "").replace(",", "").strip()
        try:
            value = float(value)
            data.append((month, value))
        except:
            continue

# Create DataFrame
df = pd.DataFrame(data, columns=["Month", "Sales"])
df["Month"] = pd.to_datetime(df["Month"], format="%b-%y")
df = df.sort_values("Month")

# Show dashboard
st.title("🥯 Bagel Sales Trends Dashboard")
st.write("Current Year Monthly Sales")

st.dataframe(df)

fig, ax = plt.subplots()
ax.plot(df["Month"], df["Sales"], marker='o')
ax.set_xlabel("Month")
ax.set_ylabel("Sales ($)")
ax.set_title("Monthly Sales Over Time")
st.pyplot(fig)
