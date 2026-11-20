import sqlite3
from database import get_connection

# Add Pet
def add_pet():
    # Get Pet Details
    name = input("Enter Pet Name: ").strip()
    animal_type = input("Enter Animal Type: ").strip()
    breed = input("Enter Breed: ").strip()
    age = input("Enter Age: ").strip()
    owner_id = input("Enter Owner ID: ").strip()

    # Empty Input Validation
    if not name or not animal_type or not breed or not age or not owner_id:
        print("All fields are required! Please try again.")
        return

    # Age Validation
    try:
        age = int(age)

        if age < 0:
            print("Age cannot be negative!")
            return

    except ValueError:
        print("Invalid age! Please enter a number.")
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
        # Check Owner ID
        cursor.execute(
            "SELECT owner_id FROM Owner WHERE owner_id = ?",
            (owner_id,)
        )

        if cursor.fetchone() is None:
            print("Owner not found! Please add a valid owner.")
            return

        # Duplicate Pet Validation
        cursor.execute("""
        SELECT pet_id FROM Pet
        WHERE pet_name = ?
        AND animal_type = ?
        AND breed = ?
        AND owner_id = ?
        """, (name, animal_type, breed, owner_id))

        if cursor.fetchone() is not None:
            print("This pet already exists!")
            return

        # Insert Pet
        cursor.execute("""
        INSERT INTO Pet (pet_name, animal_type, breed, age, owner_id)
        VALUES (?, ?, ?, ?, ?)
        """, (name, animal_type, breed, age, owner_id))

        conn.commit()
        print("Pet added successfully!")

    except sqlite3.Error as e:
        print("Database error:", e)

    finally:
        conn.close()



# View Pets
def view_pets():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT Pet.pet_id, Pet.pet_name, Pet.animal_type,
           Pet.breed, Pet.age, Owner.owner_name
    FROM Pet
    JOIN Owner ON Pet.owner_id = Owner.owner_id
    """)

    pets = cursor.fetchall()

    if pets:
        print("\n===== PET DETAILS =====")

        for pet in pets:
            print("Pet ID:", pet[0])
            print("Pet Name:", pet[1])
            print("Animal Type:", pet[2])
            print("Breed:", pet[3])
            print("Age:", pet[4])
            print("Owner Name:", pet[5])
            print("------------------------")
    else:
        print("No pets found!")

    conn.close()


# Search Pet
def search_pet():
    pet_id = input("Enter Pet ID: ").strip()

    # Empty Input Validation
    if not pet_id:
        print("Pet ID cannot be empty!")
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

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
        SELECT Pet.pet_id, Pet.pet_name, Pet.animal_type,
               Pet.breed, Pet.age, Owner.owner_name
        FROM Pet
        JOIN Owner ON Pet.owner_id = Owner.owner_id
        WHERE Pet.pet_id = ?
        """, (pet_id,))

        pet = cursor.fetchone()

        if pet:
            print("\nPet ID:", pet[0])
            print("Pet Name:", pet[1])
            print("Animal Type:", pet[2])
            print("Breed:", pet[3])
            print("Age:", pet[4])
            print("Owner Name:", pet[5])
        else:
            print("Pet not found!")

    except sqlite3.Error as e:
        print("Database error:", e)

    finally:
        conn.close()


# Update Pet

def update_pet():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        pet_id = input("Enter Pet ID to update: ").strip()

        if not pet_id:
            print("Pet ID cannot be empty!")
            return

        if not pet_id.isdigit():
            print("Pet ID must be a number!")
            return

        pet_id = int(pet_id)

        if pet_id <= 0:
            print("Invalid Pet ID!")
            return

        cursor.execute(
            "SELECT * FROM Pet WHERE pet_id = ?",
            (pet_id,)
        )

        pet = cursor.fetchone()

        if pet:
            name = input("Enter New Pet Name: ").strip()
            animal_type = input("Enter New Animal Type: ").strip()
            breed = input("Enter New Breed: ").strip()
            age = input("Enter New Age: ").strip()
            owner_id = input("Enter New Owner ID: ").strip()

            if not name or not animal_type or not breed or not age or not owner_id:
                print("All fields are required!")
                return

            if not age.isdigit():
                print("Age must be a number!")
                return

            if int(age) < 0:
                print("Age cannot be negative!")
                return

            if not owner_id.isdigit():
                print("Owner ID must be a number!")
                return

            owner_id = int(owner_id)

            if owner_id <= 0:
                print("Invalid Owner ID!")
                return

            cursor.execute(
                "SELECT owner_id FROM Owner WHERE owner_id = ?",
                (owner_id,)
            )

            if cursor.fetchone() is None:
                print("Owner not found!")
            else:
                cursor.execute("""
                UPDATE Pet
                SET pet_name = ?, animal_type = ?, breed = ?,
                    age = ?, owner_id = ?
                WHERE pet_id = ?
                """, (name, animal_type, breed, int(age), owner_id, pet_id))

                conn.commit()
                print("Pet updated successfully!")

        else:
            print("Pet not found!")

    except sqlite3.Error as e:
        print("Database Error:", e)

    finally:
        conn.close()



# Delete Pet

def delete_pet():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        pet_id = input("Enter Pet ID to delete: ").strip()

        if not pet_id:
            print("Pet ID cannot be empty!")
            return

        if not pet_id.isdigit():
            print("Pet ID must be a number!")
            return

        pet_id = int(pet_id)

        if pet_id <= 0:
            print("Invalid Pet ID!")
            return

        cursor.execute(
            "SELECT * FROM Pet WHERE pet_id = ?",
            (pet_id,)
        )

        pet = cursor.fetchone()

        if pet:
            try:
                cursor.execute(
                    "DELETE FROM Pet WHERE pet_id = ?",
                    (pet_id,)
                )
                conn.commit()
                print("Pet deleted successfully!")

            except sqlite3.IntegrityError:
                print("Cannot delete this pet because vaccination or appointment records are linked to it.")

        else:
            print("Pet not found!")

    except sqlite3.Error as e:
        print("Database Error:", e)

    finally:
        conn.close()

