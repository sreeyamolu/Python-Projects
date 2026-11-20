
import sqlite3


def get_connection():
    conn = sqlite3.connect("pet_care.db")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Users Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
    """)

    # Owner Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Owner (
        owner_id INTEGER PRIMARY KEY AUTOINCREMENT,
        owner_name TEXT NOT NULL,
        phone TEXT,
        address TEXT
    )
    """)

    # Pet Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Pet (
        pet_id INTEGER PRIMARY KEY AUTOINCREMENT,
        pet_name TEXT NOT NULL,
        animal_type TEXT,
        breed TEXT,
        age INTEGER,
        owner_id INTEGER,
        FOREIGN KEY (owner_id)
        REFERENCES Owner(owner_id)
    )
    """)

    # Vaccination Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Vaccination (
        vaccination_id INTEGER PRIMARY KEY AUTOINCREMENT,
        pet_id INTEGER,
        vaccine_name TEXT NOT NULL,
        vaccine_date TEXT,
        next_due_date TEXT,
        FOREIGN KEY (pet_id)
        REFERENCES Pet(pet_id)
    )
    """)

    # Appointment Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Appointment (
        appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        pet_id INTEGER,
        appointment_date TEXT,
        reason TEXT,
        status TEXT,
        FOREIGN KEY (pet_id)
        REFERENCES Pet(pet_id)
    )
    """)

    conn.commit()
    conn.close()

    print("Database and tables created successfully!")
