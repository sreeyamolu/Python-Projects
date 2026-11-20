
from database import create_tables

from auth import register_user, login_user, logout_user

from owner import (
    add_owner, view_owners, search_owner,
    update_owner, delete_owner
)

from pet import (
    add_pet, view_pets, search_pet,
    update_pet, delete_pet
)

from vaccination import (
    add_vaccination, view_vaccinations, search_vaccination,
    update_vaccination, delete_vaccination
)

from appointment import (
    add_appointment, view_appointments, search_appointment,
    update_appointment, delete_appointment
)


# Create Database and Tables
create_tables()


# Owner Management
def owner_menu(role):
    while True:
        print("\n===== OWNER MANAGEMENT =====")

        if role == "Admin":
            print("1. Add Owner")
            print("2. View Owners")
            print("3. Search Owner")
            print("4. Update Owner")
            print("5. Delete Owner")
            print("6. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                add_owner()
            elif choice == "2":
                view_owners()
            elif choice == "3":
                search_owner()
            elif choice == "4":
                update_owner()
            elif choice == "5":
                delete_owner()
            elif choice == "6":
                break
            else:
                print("Invalid choice!")

        else:
            print("1. View Owners")
            print("2. Search Owner")
            print("3. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                view_owners()
            elif choice == "2":
                search_owner()
            elif choice == "3":
                break
            else:
                print("Invalid choice!")


# Pet Management
def pet_menu(role):
    while True:
        print("\n===== PET MANAGEMENT =====")

        if role == "Admin":
            print("1. Add Pet")
            print("2. View Pets")
            print("3. Search Pet")
            print("4. Update Pet")
            print("5. Delete Pet")
            print("6. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                add_pet()
            elif choice == "2":
                view_pets()
            elif choice == "3":
                search_pet()
            elif choice == "4":
                update_pet()
            elif choice == "5":
                delete_pet()
            elif choice == "6":
                break
            else:
                print("Invalid choice!")

        else:
            print("1. View Pets")
            print("2. Search Pet")
            print("3. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                view_pets()
            elif choice == "2":
                search_pet()
            elif choice == "3":
                break
            else:
                print("Invalid choice!")


# Vaccination Management
def vaccination_menu(role):
    while True:
        print("\n===== VACCINATION MANAGEMENT =====")

        if role == "Admin":
            print("1. Add Vaccination")
            print("2. View Vaccinations")
            print("3. Search Vaccination")
            print("4. Update Vaccination")
            print("5. Delete Vaccination")
            print("6. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                add_vaccination()
            elif choice == "2":
                view_vaccinations()
            elif choice == "3":
                search_vaccination()
            elif choice == "4":
                update_vaccination()
            elif choice == "5":
                delete_vaccination()
            elif choice == "6":
                break
            else:
                print("Invalid choice!")

        else:
            print("1. View Vaccinations")
            print("2. Search Vaccination")
            print("3. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                view_vaccinations()
            elif choice == "2":
                search_vaccination()
            elif choice == "3":
                break
            else:
                print("Invalid choice!")


# Appointment Management
def appointment_menu(role):
    while True:
        print("\n===== APPOINTMENT MANAGEMENT =====")

        if role == "Admin":
            print("1. Add Appointment")
            print("2. View Appointments")
            print("3. Search Appointment")
            print("4. Update Appointment")
            print("5. Delete Appointment")
            print("6. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                add_appointment()
            elif choice == "2":
                view_appointments()
            elif choice == "3":
                search_appointment()
            elif choice == "4":
                update_appointment()
            elif choice == "5":
                delete_appointment()
            elif choice == "6":
                break
            else:
                print("Invalid choice!")

        else:
            print("1. View Appointments")
            print("2. Search Appointment")
            print("3. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                view_appointments()
            elif choice == "2":
                search_appointment()
            elif choice == "3":
                break
            else:
                print("Invalid choice!")


# Role-Based Menu
def user_menu(user):
    username = user[1]
    role = user[2]

    while True:
        print("\n===== PET CARE MANAGEMENT SYSTEM =====")
        print("Welcome:", username)
        print("Role:", role)

        print("1. Owner Management")
        print("2. Pet Management")
        print("3. Vaccination Management")
        print("4. Appointment Management")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            owner_menu(role)
        elif choice == "2":
            pet_menu(role)
        elif choice == "3":
            vaccination_menu(role)
        elif choice == "4":
            appointment_menu(role)
        elif choice == "5":
            logout_user()
            break
        else:
            print("Invalid choice!")


# Main Menu
while True:
    print("\n===== PET CARE MANAGEMENT SYSTEM =====")
    print("1. User Registration")
    print("2. User Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_user()

    elif choice == "2":
        user = login_user()

        if user:
            user_menu(user)

    elif choice == "3":
        print("Thank you for using Pet Care Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
