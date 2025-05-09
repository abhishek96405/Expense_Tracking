import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def analytics_category_tab():
    st.header("📊 Analytics by Category")

    # Date input fields
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 1))
    with col2:
        end_date = st.date_input("End Date", datetime(2024, 8, 5))

    # Fetch and display analytics
    if st.button("Get Analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        response = requests.post(f"{API_URL}/analytics/", json=payload)

        if response.status_code != 200:
            st.error("Failed to fetch analytics.")
            return

        data = response.json()
        df = pd.DataFrame({
            "Category": list(data.keys()),
            "Total": [data[cat]["total"] for cat in data],
            "Percentage": [data[cat]["percentage"] for cat in data]
        })

        df_sorted = df.sort_values(by="Percentage", ascending=False)

        st.subheader("Summary Table")
        st.dataframe(df_sorted, use_container_width=True)

        st.subheader("Category Breakdown")
        st.bar_chart(df_sorted.set_index("Category")[["Total"]])
