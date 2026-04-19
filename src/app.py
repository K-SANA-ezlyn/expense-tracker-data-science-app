import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime

from auth import login, check_login
from database import load_data, save_data

# ---------------- LOGIN ----------------
login()

if not check_login():
    st.warning("Please login to continue")
    st.stop()

st.title("💰 Simple Expense Tracker App")

# ---------------- LOAD DATA ----------------
df = load_data()

# ---------------- ADD EXPENSE ----------------
st.subheader("Add Expense")

col1, col2 = st.columns(2)

with col1:
    date = st.date_input("Date", datetime.date.today())

with col2:
    category = st.selectbox("Category", ["Food", "Travel", "Rent", "Shopping", "Bills"])

amount = st.number_input("Amount", min_value=0)

if st.button("Add Expense"):
    new_row = pd.DataFrame([[date, category, amount]],
                           columns=["Date", "Category", "Amount"])

    df = pd.concat([df, new_row], ignore_index=True)
    save_data(df)
    st.success("Expense Added")

# ---------------- SHOW DATA ----------------
st.subheader("All Expenses")
st.dataframe(df)

# ---------------- DELETE ----------------
st.subheader("Delete Expense")

if not df.empty:
    index = st.number_input("Enter Row Index", min_value=0, max_value=len(df)-1)

    if st.button("Delete"):
        df = df.drop(index)
        save_data(df)
        st.success("Deleted")

# ---------------- CATEGORY ANALYSIS ----------------
st.subheader("Category Analysis")

if not df.empty:
    category_sum = df.groupby("Category")["Amount"].sum()

    fig, ax = plt.subplots()
    category_sum.plot(kind="bar", ax=ax)
    st.pyplot(fig)

# ---------------- TOTAL ----------------
st.subheader("Summary")

if not df.empty:
    st.write("Total Spending:", df["Amount"].sum())
    st.write("Highest Category:", df.groupby("Category")["Amount"].sum().idxmax())
