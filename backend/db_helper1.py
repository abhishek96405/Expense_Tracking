import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger
from datetime import date

logger = setup_logger('db_helper')

@contextmanager
def get_db_cursor(commit: bool = False):
    """
    Context manager to get a database cursor.
    Commits the transaction if `commit=True`.
    """
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="expense_manager"
    )
    cursor = connection.cursor(dictionary=True)
    try:
        yield cursor
        if commit:
            connection.commit()
    finally:
        cursor.close()
        connection.close()

def fetch_expenses_for_date(expense_date):
    """Fetch all expenses for a specific date."""
    logger.info(f"Fetching expenses for date: {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        return cursor.fetchall()

def delete_expenses_for_date(expense_date):
    """Delete all expenses for a specific date."""
    logger.info(f"Deleting expenses for date: {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))

def insert_expense(expense_date, amount, category, notes):
    """Insert a new expense record."""
    logger.info(f"Inserting expense - Date: {expense_date}, Amount: {amount}, Category: {category}, Notes: {notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            """
            INSERT INTO expenses (expense_date, amount, category, notes)
            VALUES (%s, %s, %s, %s)
            """,
            (expense_date, amount, category, notes)
        )

def fetch_expense_summary(start_date, end_date):
    """Fetch summarized expenses grouped by category within a date range."""
    logger.info(f"Fetching expense summary from {start_date} to {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
            """
            SELECT category, SUM(amount) as total
            FROM expenses
            WHERE expense_date BETWEEN %s AND %s
            GROUP BY category
            """,
            (start_date, end_date)
        )
        return cursor.fetchall()

def fetch_monthly_summary(start_date: date, end_date: date):
    """Fetch monthly summary grouped by category between start_date and end_date."""
    logger.info(f"Fetching monthly summary from {start_date} to {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
            """
            SELECT category, SUM(amount) as total
            FROM expenses
            WHERE expense_date BETWEEN %s AND %s
            GROUP BY category
            """,
            (start_date, end_date)
        )
        return cursor.fetchall()

if __name__ == "__main__":
    print(fetch_expenses_for_date("2024-09-30"))
    print(fetch_expense_summary("2024-08-01", "2024-08-05"))
    print(fetch_monthly_summary)