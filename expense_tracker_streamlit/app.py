import streamlit as st
import pandas as pd
from datetime import datetime

FILE = 'expenses.txt'

# Initialize the file
def initialize_file():
    try:
        with open(FILE, 'x') as f:
            f.write("Date,Category,Amount,Description\n")
    except FileExistsError:
        pass

# Add a new expense
def add_expense(date, category, amount, description):
    with open(FILE, 'a') as f:
        f.write(f"{date},{category},{amount},{description}\n")

# Load expenses into a DataFrame
def load_expenses():
    try:
        return pd.read_csv(FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])

# Save updated expenses
def save_expenses(df):
    df.to_csv(FILE, index=False)

# Calculate total expenses
def total_expense(df):
    return df["Amount"].sum() if not df.empty else 0

# ---------- Streamlit App ----------
initialize_file()
st.set_page_config(page_title="Expense Tracker 💸")
st.title("📒 Expense Tracker")

# Sidebar for navigation
menu = st.sidebar.selectbox("Navigate", ["➕ Add Expense", "📋 View Expenses", "📊 Expense Summary"])

# --- Add Expense ---
if menu == "➕ Add Expense":
    st.subheader("Add a New Expense")
    date = st.date_input("Date", datetime.today())
    category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Bills", "Other"])
    amount = st.number_input("Amount (₹)", min_value=0.0, format="%.2f")
    description = st.text_input("Description")

    if st.button("Add Expense"):
        if amount > 0:
            add_expense(date, category, amount, description)
            st.success("✅ Expense added successfully!")
        else:
            st.error("❌ Enter a valid amount.")

# --- View Expenses with Delete Option ---
elif menu == "📋 View Expenses":
    st.subheader("All Expenses")
    df = load_expenses()
    
    if df.empty:
        st.info("No expenses recorded yet.")
    else:
        df_display = df.copy()
        df_display.index.name = 'Index'
        st.dataframe(df_display)

        delete_index = st.number_input("Enter the index of the row to delete:", min_value=0, max_value=len(df)-1, step=1)
        if st.button("Delete Selected Expense"):
            df.drop(index=delete_index, inplace=True)
            df.reset_index(drop=True, inplace=True)
            save_expenses(df)
            st.success("🗑️ Expense deleted successfully!")
            st.experimental_rerun()

# --- Expense Summary ---
elif menu == "📊 Expense Summary":
    st.subheader("Summary")
    df = load_expenses()
    if df.empty:
        st.warning("No data to summarize.")
    else:
        st.metric("💰 Total Expenses", f"₹{total_expense(df):.2f}")
        
        category_summary = df.groupby("Category")["Amount"].sum().reset_index()
        st.bar_chart(category_summary.set_index("Category"))

        df["Date"] = pd.to_datetime(df["Date"])
        monthly_summary = df.groupby(df["Date"].dt.to_period("M"))["Amount"].sum().reset_index()
        monthly_summary["Date"] = monthly_summary["Date"].astype(str)
        st.line_chart(monthly_summary.set_index("Date"))
