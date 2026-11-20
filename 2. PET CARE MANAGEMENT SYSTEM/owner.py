import sqlite3
from database import get_connection


# Add Owner


def add_owner():
    name = input("Enter Owner Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    address = input("Enter Address: ").strip()

    # Empty Input Validation
    if not name or not phone or not address:
        print("All fields are required! Please try again.")
        return

    # Phone Number Validation
    if not phone.isdigit() or len(phone) != 10:
        print("Invalid phone number! Enter a 10-digit number.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Duplicate Phone Number Validation
        cursor.execute(
            "SELECT owner_id FROM Owner WHERE phone = ?",
            (phone,)
        )

        if cursor.fetchone() is not None:
            print("This phone number already exists!")
            return

        cursor.execute("""
        INSERT INTO Owner (owner_name, phone, address)
        VALUES (?, ?, ?)
        """, (name, phone, address))

        conn.commit()
        print("Owner added successfully!")

    except sqlite3.Error as e:
        print("Database error:", e)

    finally:
        conn.close()




# View Owners
def view_owners():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Owner")
    owners = cursor.fetchall()

    if owners:
        print("\n===== OWNER DETAILS =====")
        for owner in owners:
            print("Owner ID:", owner[0])
            print("Name:", owner[1])
            print("Phone:", owner[2])
            print("Address:", owner[3])
            print("------------------------")
    else:
        print("No owners found!")

    conn.close()


# Search Owner
def search_owner():
    owner_id = input("Enter Owner ID: ").strip()

    # Empty Input Validation
    if not owner_id:
        print("Owner ID cannot be empty!")
        return

    # Owner ID Validation
    try:
        owner_id = int(owner_id)

        if owner_id <= 0:
            print("Invalid Owner ID!")
            return

    except ValueError:
        print("Owner ID must be a number!")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT * FROM Owner WHERE owner_id = ?",
            (owner_id,)
        )

        owner = cursor.fetchone()

        if owner:
            print("\nOwner ID:", owner[0])
            print("Name:", owner[1])
            print("Phone:", owner[2])
            print("Address:", owner[3])
        else:
            print("Owner not found!")

    except sqlite3.Error as e:
        print("Database error:", e)

    finally:
        conn.close()

# Update Owner

def update_owner():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        owner_id = input("Enter Owner ID to update: ").strip()

        if not owner_id:
            print("Owner ID cannot be empty!")
            return

        if not owner_id.isdigit():
            print("Owner ID must be a number!")
            return

        owner_id = int(owner_id)

        if owner_id <= 0:
            print("Invalid Owner ID!")
            return

        cursor.execute(
            "SELECT * FROM Owner WHERE owner_id = ?",
            (owner_id,)
        )

        owner = cursor.fetchone()

        if owner:
            name = input("Enter New Name: ").strip()
            phone = input("Enter New Phone: ").strip()
            address = input("Enter New Address: ").strip()

            if not name or not phone or not address:
                print("All fields are required!")
                return

            if not phone.isdigit() or len(phone) != 10:
                print("Phone number must contain exactly 10 digits!")
                return

            cursor.execute("""
            SELECT * FROM Owner
            WHERE phone = ? AND owner_id != ?
            """, (phone, owner_id))

            if cursor.fetchone():
                print("This phone number already exists!")
                return

            cursor.execute("""
            UPDATE Owner
            SET owner_name = ?, phone = ?, address = ?
            WHERE owner_id = ?
            """, (name, phone, address, owner_id))

            conn.commit()
            print("Owner updated successfully!")

        else:
            print("Owner not found!")

    except sqlite3.Error as e:
        print("Database Error:", e)

    finally:
        conn.close()


# Delete Owner

def delete_owner():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        owner_id = input("Enter Owner ID to delete: ").strip()

        if not owner_id:
            print("Owner ID cannot be empty!")
            return

        if not owner_id.isdigit():
            print("Owner ID must be a number!")
            return

        owner_id = int(owner_id)

        if owner_id <= 0:
            print("Invalid Owner ID!")
            return

        cursor.execute(
            "SELECT * FROM Owner WHERE owner_id = ?",
            (owner_id,)
        )

        owner = cursor.fetchone()

        if owner:
            try:
                cursor.execute(
                    "DELETE FROM Owner WHERE owner_id = ?",
                    (owner_id,)
                )
                conn.commit()
                print("Owner deleted successfully!")

            except sqlite3.IntegrityError:
                print("Cannot delete this owner because pets are linked to this owner.")

        else:
            print("Owner not found!")

    except sqlite3.Error as e:
        print("Database Error:", e)

    finally:
        conn.close()
