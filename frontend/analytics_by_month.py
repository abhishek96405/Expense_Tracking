import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def analytics_months_tab():
    st.header("📅 Monthly Analytics")

    col1, col2 = st.columns(2)
    with col1:
        year = st.number_input("Year", min_value=2000, max_value=2100, value=2024)
    with col2:
        month = st.number_input("Month", min_value=1, max_value=12, value=8)

    if st.button("Get Monthly Summary"):
        params = {"year": year, "month": month}
        response = requests.get(f"{API_URL}/summary/monthly", params=params)

        if response.status_code != 200:
            st.error("Failed to fetch monthly summary.")
            st.text(f"Status code: {response.status_code}")
            st.text(f"Response text: {response.text}")
            return

        data = response.json()
        st.metric("Total Spent", f"₹{data['total_spent']:.2f}")
        st.metric("Most Expensive Category", data['most_expensive_category'])
        st.metric("Highest Category Total", f"₹{data['highest_category_total']:.2f}")
        st.metric("Average Per Day", f"₹{data['average_per_day']:.2f}")
