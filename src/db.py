import sqlite3

DB_NAME = "expenses.db"

def get_conn():
    return sqlite3.connect(DB_NAME, check_same_thread=False)

def init_db():
    conn = get_conn()
    cur = conn.cursor()

    # Users table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    # Expenses table (linked to user)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        amount REAL,
        category TEXT,
        note TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()

# ---------- AUTH ----------
def register_user(username, password):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, password) VALUES (?,?)", (username, password))
    conn.commit()
    conn.close()

def login_user(username, password):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username=? AND password=?", (username, password))
    user = cur.fetchone()
    conn.close()
    return user

# ---------- EXPENSES ----------
def add_expense(user_id, amount, category, note):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO expenses (user_id, amount, category, note) VALUES (?,?,?,?)",
        (user_id, amount, category, note)
    )
    conn.commit()
    conn.close()

def list_expenses(user_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, amount, category, note FROM expenses WHERE user_id=?",
        (user_id,)
    )
    rows = cur.fetchall()
    conn.close()
    return rows
def update_expense(expense_id, user_id, amount, category, note):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE expenses
        SET amount = ?, category = ?, note = ?
        WHERE id = ? AND user_id = ?
        """,
        (amount, category, note, expense_id, user_id)
    )
    conn.commit()
    conn.close()


def delete_expense(expense_id, user_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM expenses WHERE id = ? AND user_id = ?",
        (expense_id, user_id)
    )
    conn.commit()
    conn.close()
