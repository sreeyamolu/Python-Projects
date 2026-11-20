# Pet Care Management System

## Project Overview
The **Pet Care Management System** is a Python-based database management application developed using SQLite3. It helps manage pet owners, pets, vaccination records, and appointments through a simple Command Line Interface (CLI).

The project demonstrates database management, CRUD operations, user authentication, role-based authorization, input validation, and exception handling.

## Technologies Used
- Python 3.x
- SQLite3
- Visual Studio Code
- Command Line Interface (CLI)

## Project Features

### 1. User Authentication
- User Registration
- User Login
- User Logout
- Password hashing

### 2. Role-Based Authorization
The system supports two user roles:

**Admin**
- Add records
- View records
- Search records
- Update records
- Delete records
- Manage all modules

**User**
- View records
- Search records
- Limited access to the system

The first registered user is assigned the Admin role. Subsequent registered users are assigned the User role.

### 3. Owner Management
- Add Owner
- View Owners
- Search Owner
- Update Owner
- Delete Owner

### 4. Pet Management
- Add Pet
- View Pets
- Search Pet
- Update Pet
- Delete Pet

### 5. Vaccination Management
- Add Vaccination Details
- View Vaccination Records
- Search Vaccination
- Update Vaccination
- Delete Vaccination

### 6. Appointment Management
- Add Appointment
- View Appointments
- Search Appointment
- Update Appointment
- Delete Appointment

### 7. Input Validation
The system includes:
- Empty input validation
- Numeric input validation
- Invalid ID validation
- Duplicate record checking
- Phone number validation
- Age validation
- Date format validation
- Appointment and vaccination date validation
- Invalid menu selection handling

### 8. Exception Handling
- SQLite database error handling
- Duplicate record handling
- Missing record handling
- Foreign key constraint handling
- Invalid input handling

## Database Design

The project uses SQLite3 with five tables.

| Table | Description |
|---|---|
| Users | Stores login credentials and user roles |
| Owner | Stores pet owner details |
| Pet | Stores pet information |
| Vaccination | Stores vaccination details |
| Appointment | Stores appointment information |

### Table Relationships

- One Owner can have multiple Pets.
- One Pet can have multiple Vaccination records.
- One Pet can have multiple Appointment records.

### Primary Keys and Foreign Keys

- `user_id` – Primary Key in Users
- `owner_id` – Primary Key in Owner
- `pet_id` – Primary Key in Pet
- `vaccination_id` – Primary Key in Vaccination
- `appointment_id` – Primary Key in Appointment

Foreign Keys:
- `owner_id` in Pet references Owner.
- `pet_id` in Vaccination references Pet.
- `pet_id` in Appointment references Pet.

## Project Structure

```text
Pet_Care_Management_System/
│
├── main.py
├── database.py
├── auth.py
├── owner.py
├── pet.py
├── vaccination.py
├── appointment.py
├── pet_care.db
├── README.md
└── .gitignore
```

## How to Run the Project

### Step 1: Install Python
Install Python 3.x on your computer.

### Step 2: Open the Project
Open the `Pet_Care_Management_System` folder in Visual Studio Code.

### Step 3: Run the Application
Open the VS Code terminal and execute:

```bash
python main.py
```

If the Python command is not recognized on Windows, use your installed Python executable path.

### Step 4: Register an Account
- Select Register from the main menu.
- Create a username and password.
- The first registered account becomes Admin.

### Step 5: Login
Login using your registered username and password.

### Step 6: Manage Records
Use the role-specific menus to manage Owners, Pets, Vaccinations, and Appointments.

## Database Creation

The SQLite database is created automatically when the application runs for the first time.

The database file is named:

`pet_care.db`

## CRUD Operations

The application supports all four CRUD operations:

- **Create:** Add new records.
- **Read:** View and search existing records.
- **Update:** Modify existing records.
- **Delete:** Remove records.

## Expected Outcome

The Pet Care Management System provides a simple and organized way to manage pet owners, pets, vaccination records, and appointments.

It demonstrates practical implementation of Python programming, SQLite database operations, authentication, role-based access control, input validation, and exception handling.

## Project Type
- Difficulty: Intermediate
- Programming Language: Python 3.x
- Database: SQLite3
- Interface: Command Line Interface (CLI)

## Author
Developed as part of a Python and SQLite Database Management System Major Project Assignment.