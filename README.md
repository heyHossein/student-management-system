# Student Management System

A console-based **Student Management System** built with **Python** and **MySQL**.

This project allows users to manage student information such as name, age, and score through an interactive command-line menu. Student data is stored in a MySQL database.

## Features

* Add a new student
* Display all students
* Search for a student by ID or name
* Delete a student
* Edit student information
* Sort students by score
* Search students by minimum score
* Display student statistics
* Delete all students
* Store student data in a MySQL database
* Exit the program

## Student Statistics

The statistics section provides useful information including:

* Number of students
* Highest score
* Lowest score
* Average score
* Number of passing students
* Number of failing students
* Best student
* Worst student

## Technologies

* Python 3.x
* MySQL
* mysql-connector-python
* python-dotenv
* Git & GitHub

## Requirements

* Python 3.x
* MySQL Server
* `mysql-connector-python`
* `python-dotenv`

Install the required Python packages with:

```bash
pip install mysql-connector-python python-dotenv
```

## Database Setup

Create a MySQL database named:

```sql
student_management_system
```

The project automatically creates the `students` table when the application starts if it does not already exist.

The table contains:

* `id` — Auto-incrementing primary key
* `name` — Student name
* `age` — Student age
* `score` — Student score

## Environment Variables

Create a `.env` file in the project root directory and add your MySQL connection information:

```env
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=student_management_system
```

> Do not commit the `.env` file to GitHub. It is included in `.gitignore` to keep database credentials private.

## How to Run

Clone the repository:

```bash
git clone https://github.com/heyHossein/student-management-system.git
```

Navigate to the project directory:

```bash
cd student-management-system
```

Install the required dependencies:

```bash
pip install mysql-connector-python python-dotenv
```

Make sure MySQL Server is running and your `.env` file is configured correctly.

Then run:

```bash
python main.py
```

Or simply run `main.py` using your preferred Python IDE.

## Project Structure

```text
student-management-system/
│
├── main.py
├── database.py
├── README.md
├── .gitignore
└── .env
```

> `.env` is used locally and should not be uploaded to GitHub.

## Project Architecture

The project is divided into two main files:

### `main.py`

Handles:

* User interaction
* Console menu
* Reading user input
* Calling database functions

### `database.py`

Handles:

* MySQL database connection
* Creating the `students` table
* Adding students
* Searching students
* Editing students
* Deleting students
* Sorting students
* Calculating statistics

This separation keeps the user interface and database operations organized.

## Version History

### v1.0.0

Initial version of the project.

* Student data was stored in a Python list.
* Basic student management features were implemented.
* The project focused on practicing Python fundamentals.

### v2.0.0

Major upgrade to a MySQL-based database system.

* Replaced in-memory list storage with MySQL
* Added database connection using `mysql-connector-python`
* Added environment variable support using `python-dotenv`
* Added automatic table creation
* Added student IDs using an auto-incrementing primary key
* Separated database operations into `database.py`
* Updated the application to work with persistent student data

## Notes

This project is an educational project created to practice:

* Python fundamentals
* Functions
* Loops
* Conditional statements
* User input
* SQL
* MySQL
* Database operations
* CRUD operations
* Environment variables
* Git and GitHub
* Project versioning

## Future Improvements

Possible improvements for future versions include:

* Better input validation
* Error handling for database connection failures
* Using classes and Object-Oriented Programming
* Adding more advanced search and filtering options
* Improving the user experience
* Adding a graphical user interface (GUI)
* Adding automated tests

## License

This project is available for educational and learning purposes.
