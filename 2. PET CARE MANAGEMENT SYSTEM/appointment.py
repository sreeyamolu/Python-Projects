import sqlite3
from datetime import datetime
from database import get_connection

# 1. Add Appointment
def add_appointment():
    pet_id = input("Enter Pet ID: ").strip()
    appointment_date = input("Enter Appointment Date (YYYY-MM-DD): ").strip()
    reason = input("Enter Reason: ").strip()
    status = input("Enter Status: ").strip()

    # Empty Input Validation
    if not pet_id or not appointment_date or not reason or not status:
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
        date_obj = datetime.strptime(appointment_date, "%Y-%m-%d")

        if date_obj.strftime("%Y-%m-%d") != appointment_date:
            print("Invalid date format! Use YYYY-MM-DD.")
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

        # Duplicate Appointment Validation
        cursor.execute("""
        SELECT appointment_id FROM Appointment
        WHERE pet_id = ?
        AND appointment_date = ?
        AND reason = ?
        """, (pet_id, appointment_date, reason))

        if cursor.fetchone() is not None:
            print("This appointment already exists!")
            return

        # Insert Appointment
        cursor.execute("""
        INSERT INTO Appointment
        (pet_id, appointment_date, reason, status)
        VALUES (?, ?, ?, ?)
        """, (pet_id, appointment_date, reason, status))

        conn.commit()
        print("Appointment added successfully!")

    except sqlite3.Error as e:
        print("Database error:", e)

    finally:
        conn.close()

# 2. View Appointments
def view_appointments():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT Appointment.appointment_id, Pet.pet_name,
           Appointment.appointment_date,
           Appointment.reason, Appointment.status
    FROM Appointment
    JOIN Pet ON Appointment.pet_id = Pet.pet_id
    """)

    records = cursor.fetchall()

    if records:
        print("\n===== APPOINTMENT RECORDS =====")
        for row in records:
            print(row)
    else:
        print("No appointment records found!")

    conn.close()


# 3. Search Appointment

def search_appointment():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        appointment_id = input("Enter Appointment ID: ").strip()

        if not appointment_id:
            print("Appointment ID cannot be empty!")
            return

        if not appointment_id.isdigit():
            print("Appointment ID must be a number!")
            return

        appointment_id = int(appointment_id)

        if appointment_id <= 0:
            print("Invalid Appointment ID!")
            return

        cursor.execute("""
        SELECT * FROM Appointment
        WHERE appointment_id = ?
        """, (appointment_id,))

        record = cursor.fetchone()

        if record:
            print("Appointment Details:", record)
        else:
            print("Appointment not found!")

    except sqlite3.Error as e:
        print("Database Error:", e)

    finally:
        conn.close()



# 4. Update Appointment

def update_appointment():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        appointment_id = input("Enter Appointment ID to update: ").strip()

        if not appointment_id:
            print("Appointment ID cannot be empty!")
            return

        if not appointment_id.isdigit():
            print("Appointment ID must be a number!")
            return

        appointment_id = int(appointment_id)

        if appointment_id <= 0:
            print("Invalid Appointment ID!")
            return

        cursor.execute("""
        SELECT * FROM Appointment
        WHERE appointment_id = ?
        """, (appointment_id,))

        record = cursor.fetchone()

        if record is None:
            print("Appointment not found!")
            return

        appointment_date = input("Enter New Appointment Date (YYYY-MM-DD): ").strip()
        reason = input("Enter New Reason: ").strip()
        status = input("Enter New Status: ").strip()

        if not appointment_date or not reason or not status:
            print("All fields are required!")
            return

        try:
            datetime.strptime(appointment_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format! Use YYYY-MM-DD.")
            return

        cursor.execute("""
        UPDATE Appointment
        SET appointment_date = ?, reason = ?, status = ?
        WHERE appointment_id = ?
        """, (appointment_date, reason, status, appointment_id))

        conn.commit()
        print("Appointment updated successfully!")

    except sqlite3.Error as e:
        print("Database Error:", e)

    finally:
        conn.close()



# 5. Delete Appointment

def delete_appointment():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        appointment_id = input("Enter Appointment ID to delete: ").strip()

        if not appointment_id:
            print("Appointment ID cannot be empty!")
            return

        if not appointment_id.isdigit():
            print("Appointment ID must be a number!")
            return

        appointment_id = int(appointment_id)

        if appointment_id <= 0:
            print("Invalid Appointment ID!")
            return

        cursor.execute("""
        DELETE FROM Appointment
        WHERE appointment_id = ?
        """, (appointment_id,))

        if cursor.rowcount > 0:
            conn.commit()
            print("Appointment deleted successfully!")
        else:
            print("Appointment not found!")

    except sqlite3.Error as e:
        print("Database Error:", e)

    finally:
        conn.close()

