from fastapi import FastAPI, HTTPException, Query
from datetime import date
from typing import List
from pydantic import BaseModel
import db_helper1

app = FastAPI()

class Expense(BaseModel):
    amount: float
    category: str
    notes: str

class DateRange(BaseModel):
    start_date: date
    end_date: date

@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    """Get all expenses for a specific date."""
    expenses = db_helper1.fetch_expenses_for_date(expense_date)
    if expenses is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expenses from the database.")
    return expenses

@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date, expenses: List[Expense]):
    """Replace all expenses for a given date with a new list."""
    db_helper1.delete_expenses_for_date(expense_date)
    for expense in expenses:
        db_helper1.insert_expense(expense_date, expense.amount, expense.category, expense.notes)
    return {"message": "Expenses updated successfully"}

@app.post("/analytics/")
def get_analytics(date_range: DateRange):
    """Get summary analytics of expenses by category for a given date range."""
    data = db_helper1.fetch_expense_summary(date_range.start_date, date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary from the database.")

    total = sum([row['total'] for row in data])
    breakdown = {}
    for row in data:
        percentage = (row['total'] / total) * 100 if total != 0 else 0
        breakdown[row['category']] = {
            "total": row['total'],
            "percentage": percentage
        }
    return breakdown

@app.get("/summary/monthly")
def monthly_summary(month: int = Query(..., ge=1, le=12), year: int = Query(..., ge=2000)):
    """Get monthly summary of expenses including totals and average per day."""
    start_date = date(year, month, 1)
    if month == 12:
        end_date = date(year + 1, 1, 1)
    else:
        end_date = date(year, month + 1, 1)

    data = db_helper1.fetch_monthly_summary(start_date, end_date)
    total = sum(row['total'] for row in data)

    if not data:
        return {
            "total_spent": 0,
            "most_expensive_category": None,
            "highest_category_total": 0,
            "average_per_day": 0
        }

    most_expensive = max(data, key=lambda x: x['total'])
    days_in_month = (end_date - start_date).days
    avg_per_day = total / days_in_month if days_in_month else 0

    return {
        "total_spent": total,
        "most_expensive_category": most_expensive['category'],
        "highest_category_total": most_expensive['total'],
        "average_per_day": avg_per_day
    }
