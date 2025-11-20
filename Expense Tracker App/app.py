import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==============================
# Initialize Data File
# ================================
FILE = "expenses.csv"

if not os.path.exists(FILE):
    df = pd.DataFrame(columns=["Date", "Category", "Amount"])
    df.to_csv(FILE, index=False)

# ===================================
# Load Data
# ==============================
def load_data():
    return pd.read_csv(FILE)

def save_data(df):
    df.to_csv(FILE, index=False)

# ==============================
# Streamlit UI
# ==============================
st.title("💰 Personal Expense Tracker with Budget Alert")

st.sidebar.header("Settings")
budget = st.sidebar.number_input("Set Monthly Budget (৳)", value=20000)

st.header("➕ Add Expense")

date = st.date_input("Date", datetime.today())
category = st.selectbox("Category", ["Food", "Transport", "Bills", "Shopping", "Health", "Other"])
amount = st.number_input("Amount (৳)", min_value=1)

if st.button("Add Expense"):
    df = load_data()
    new_data = pd.DataFrame({"Date": [date], "Category": [category], "Amount": [amount]})
    df = pd.concat([df, new_data], ignore_index=True)
    save_data(df)
    st.success("Expense added successfully!")

# ==============================
# Show Expense Summary
# ==============================
st.header("📊 Expense Summary")

df = load_data()
df["Date"] = pd.to_datetime(df["Date"])

# Total Expense
total_spent = df["Amount"].sum()
st.metric("Total Spent This Month", f"৳ {int(total_spent)}")

# Budget Alert
if total_spent > budget:
    st.error("⚠️ You have exceeded your monthly budget!")
else:
    st.info(f"Remaining Budget: ৳ {int(budget - total_spent)}")

# Category Chart
st.subheader("Spending by Category")
category_summary = df.groupby("Category")["Amount"].sum()

st.bar_chart(category_summary)

# Show Table
st.subheader("📅 All Expenses")
st.dataframe(df)

# Delete all data
if st.button("Clear All Data"):
    df = pd.DataFrame(columns=["Date", "Category", "Amount"])
    save_data(df)
    st.warning("All data cleared!")
