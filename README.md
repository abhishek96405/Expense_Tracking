# 💸 Expense Tracking System

A full-stack personal expense tracking application built using **FastAPI** for the backend and **Streamlit** for the frontend.

## 🚀 Features

- Add, view, and update daily expenses
- Visualize spending by category or month
- Track monthly summaries (total, most expensive category, average per day)
- Backend with FastAPI and MySQL
- Frontend with Streamlit (interactive UI)
- Analytics with charts and tabular data

## 🏗️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **Database**: MySQL
- **Testing**: Pytest

## 📁 Project Structure

```
project_expense_tracking/
├── backend/              # FastAPI app
├── frontend/             # Streamlit frontend
├── database/             # SQL script for schema
├── test/                 # Unit tests
```

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/project_expense_tracking.git
cd project_expense_tracking
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate  # On Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up MySQL database

Run the SQL file in your MySQL environment:

```sql
source database/expense_db_creation.sql;
```

Update the DB config in `db_helper1.py` if needed.

### 5. Run the backend

```bash
cd backend
uvicorn server:app --reload --port 8000
```

### 6. Run the frontend

```bash
cd ../frontend
streamlit run app.py
```

## 📷 Screenshots

![monthly report](Expense_Monthly-Report.png) ![add expense](Add_Expense.png) ![expense analytics](Expense_Analytics.png)

## 🧑‍💻 Author

Abhishek Dharmapuri

---
