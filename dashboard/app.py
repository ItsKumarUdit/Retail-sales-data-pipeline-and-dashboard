import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("data/cleaned_sales.csv")

st.title("🛍 Retail Sales Dashboard")

# KPIs
st.metric("Total Sales", f"₹{df['TotalAmount'].sum():,.0f}")
st.metric("Total Orders", len(df))
st.metric("Average Order Value", f"₹{df['TotalAmount'].mean():,.0f}")

# Sales over time
fig_sales = px.line(df.groupby('Date')['TotalAmount'].sum().reset_index(),
                    x='Date', y='TotalAmount', title="Sales Over Time")
st.plotly_chart(fig_sales)

# Top Products
fig_products = px.bar(df.groupby('Product')['TotalAmount'].sum().reset_index().sort_values(by="TotalAmount", ascending=False).head(5),
                      x='Product', y='TotalAmount', title="Top Selling Products")
st.plotly_chart(fig_products)

# Payment Method Breakdown
fig_payment = px.pie(df, names='PaymentMethod', values='TotalAmount', title="Payment Method Share")
st.plotly_chart(fig_payment)