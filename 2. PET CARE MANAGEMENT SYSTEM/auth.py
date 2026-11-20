
import sqlite3
import hashlib
from database import get_connection


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# User Registration
def register_user():
    print("\n===== USER REGISTRATION =====")

    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if not username or not password:
        print("Username and password cannot be empty!")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT COUNT(*) FROM Users")
        count = cursor.fetchone()[0]

        # First registered user will be Admin
        if count == 0:
            role = "Admin"
        else:
            role = "User"

        hashed_password = hash_password(password)

        cursor.execute("""
        INSERT INTO Users (username, password, role)
        VALUES (?, ?, ?)
        """, (username, hashed_password, role))

        conn.commit()

        print("Registration successful!")
        print("Your role:", role)

    except sqlite3.IntegrityError:
        print("Username already exists!")

    finally:
        conn.close()


# User Login
def login_user():
    print("\n===== USER LOGIN =====")

    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if not username or not password:
        print("Username and password cannot be empty!")
        return None

    hashed_password = hash_password(password)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT user_id, username, role
    FROM Users
    WHERE username = ? AND password = ?
    """, (username, hashed_password))

    user = cursor.fetchone()
    conn.close()

    if user:
        print("\nLogin successful!")
        print("Welcome", user[1])
        print("Role:", user[2])
        return user
    else:
        print("Invalid username or password!")
        return None


# User Logout
def logout_user():
    print("\nYou have logged out successfully!")
