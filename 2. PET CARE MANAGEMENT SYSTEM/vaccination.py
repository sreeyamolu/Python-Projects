import sqlite3
from database import get_connection
from datetime import datetime


# 1. Add Vaccination
def add_vaccination():
    pet_id = input("Enter Pet ID: ").strip()
    vaccine_name = input("Enter Vaccine Name: ").strip()
    vaccine_date = input("Enter Vaccination Date (YYYY-MM-DD): ").strip()
    next_due_date = input("Enter Next Due Date (YYYY-MM-DD): ").strip()

    # Empty Input Validation
    if not pet_id or not vaccine_name or not vaccine_date or not next_due_date:
        print("All fields are required! Please try again.")
        return

    # Pet ID Validation
    try:
        pet_id = int(pet_id)

        if pet_id <= 0:
            print("Invalid Pet ID!")
            return

    except ValueError:
        print("Pet ID must be a number!")
        return

    # Date Validation
    try:
        vaccine_date_obj = datetime.strptime(vaccine_date, "%Y-%m-%d")
        next_due_date_obj = datetime.strptime(next_due_date, "%Y-%m-%d")

        if vaccine_date_obj.strftime("%Y-%m-%d") != vaccine_date:
            print("Invalid vaccination date format!")
            return

        if next_due_date_obj.strftime("%Y-%m-%d") != next_due_date:
            print("Invalid next due date format!")
            return

        if next_due_date_obj < vaccine_date_obj:
            print("Next due date cannot be before vaccination date!")
            return

    except ValueError:
        print("Invalid date! Use YYYY-MM-DD format.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Check Pet ID
        cursor.execute(
            "SELECT pet_id FROM Pet WHERE pet_id = ?",
            (pet_id,)
        )

        if cursor.fetchone() is None:
            print("Pet ID not found!")
            return

        # Duplicate Vaccination Validation
        cursor.execute("""
        SELECT vaccination_id FROM Vaccination
        WHERE pet_id = ?
        AND vaccine_name = ?
        AND vaccine_date = ?
        """, (pet_id, vaccine_name, vaccine_date))

        if cursor.fetchone() is not None:
            print("This vaccination record already exists!")
            return

        # Insert Vaccination
        cursor.execute("""
        INSERT INTO Vaccination
        (pet_id, vaccine_name, vaccine_date, next_due_date)
        VALUES (?, ?, ?, ?)
        """, (pet_id, vaccine_name, vaccine_date, next_due_date))

        conn.commit()
        print("Vaccination added successfully!")

    except sqlite3.Error as e:
        print("Database error:", e)

    finally:
        conn.close()


# 2. View Vaccinations
def view_vaccinations():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT Vaccination.vaccination_id, Pet.pet_name,
           Vaccination.vaccine_name, Vaccination.vaccine_date,
           Vaccination.next_due_date
    FROM Vaccination
    JOIN Pet ON Vaccination.pet_id = Pet.pet_id
    """)

    records = cursor.fetchall()

    if records:
        print("\n===== VACCINATION RECORDS =====")
        for row in records:
            print(row)
    else:
        print("No vaccination records found!")

    conn.close()


# 3. Search Vaccination
def search_vaccination():
    vaccination_id = input("Enter Vaccination ID: ").strip()

    # Empty Input Validation
    if not vaccination_id:
        print("Vaccination ID cannot be empty!")
        return

    # Vaccination ID Validation
    try:
        vaccination_id = int(vaccination_id)

        if vaccination_id <= 0:
            print("Invalid Vaccination ID!")
            return

    except ValueError:
        print("Vaccination ID must be a number!")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
        SELECT * FROM Vaccination
        WHERE vaccination_id = ?
        """, (vaccination_id,))

        record = cursor.fetchone()

        if record:
            print("Vaccination Details:", record)
        else:
            print("Vaccination record not found!")

    except sqlite3.Error as e:
        print("Database error:", e)

    finally:
        conn.close()


# 4. Update Vaccination

def update_vaccination():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        vaccination_id = input("Enter Vaccination ID to update: ").strip()

        if not vaccination_id:
            print("Vaccination ID cannot be empty!")
            return

        if not vaccination_id.isdigit():
            print("Vaccination ID must be a number!")
            return

        vaccination_id = int(vaccination_id)

        if vaccination_id <= 0:
            print("Invalid Vaccination ID!")
            return

        cursor.execute("""
        SELECT * FROM Vaccination
        WHERE vaccination_id = ?
        """, (vaccination_id,))

        record = cursor.fetchone()

        if record is None:
            print("Vaccination record not found!")
            return

        vaccine_name = input("Enter New Vaccine Name: ").strip()
        vaccine_date = input("Enter New Vaccination Date (YYYY-MM-DD): ").strip()
        next_due_date = input("Enter New Due Date (YYYY-MM-DD): ").strip()

        if not vaccine_name or not vaccine_date or not next_due_date:
            print("All fields are required!")
            return

        try:
            vaccine_date_obj = datetime.strptime(vaccine_date, "%Y-%m-%d")
            due_date_obj = datetime.strptime(next_due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format! Use YYYY-MM-DD.")
            return

        if due_date_obj < vaccine_date_obj:
            print("Due date cannot be before vaccination date!")
            return

        cursor.execute("""
        UPDATE Vaccination
        SET vaccine_name = ?, vaccine_date = ?, next_due_date = ?
        WHERE vaccination_id = ?
        """, (vaccine_name, vaccine_date, next_due_date, vaccination_id))

        conn.commit()
        print("Vaccination updated successfully!")

    except sqlite3.Error as e:
        print("Database Error:", e)

    finally:
        conn.close()



# 5. Delete Vaccination

def delete_vaccination():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        vaccination_id = input("Enter Vaccination ID to delete: ").strip()

        if not vaccination_id:
            print("Vaccination ID cannot be empty!")
            return

        if not vaccination_id.isdigit():
            print("Vaccination ID must be a number!")
            return

        vaccination_id = int(vaccination_id)

        if vaccination_id <= 0:
            print("Invalid Vaccination ID!")
            return

        cursor.execute("""
        DELETE FROM Vaccination
        WHERE vaccination_id = ?
        """, (vaccination_id,))

        if cursor.rowcount > 0:
            conn.commit()
            print("Vaccination deleted successfully!")
        else:
            print("Vaccination record not found!")

    except sqlite3.Error as e:
        print("Database Error:", e)

    finally:
        conn.close()

