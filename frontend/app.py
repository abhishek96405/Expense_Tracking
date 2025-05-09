import streamlit as st
from add_update_ui import add_update_tab
from analytics_by_category import analytics_category_tab
from analytics_by_month import analytics_months_tab


def main():
    st.set_page_config(page_title="Expense Tracker", layout="wide")
    st.title("💸 Expense Tracking System")

    tab1, tab2, tab3 = st.tabs([
        "➕ Add/Update",
        "📊 Analytics By Category",
        "📅 Analytics By Month"
    ])

    with tab1:
        add_update_tab()

    with tab2:
        analytics_category_tab()

    with tab3:
        analytics_months_tab()


if __name__ == "__main__":
    main()
