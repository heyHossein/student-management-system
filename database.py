import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

db = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)

print("Database connected successfully!")


def create_table():
    cursor = db.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INT NOT NULL,
        score FLOAT NOT NULL
    )
    """

    cursor.execute(query)
    db.commit()
    cursor.close()


create_table()


def add_student(name, age, score):
    cursor = db.cursor()

    query = """
    INSERT INTO students (name, age, score)
    VALUES (%s, %s, %s)
    """

    values = (name, age, score)

    cursor.execute(query, values)
    db.commit()
    cursor.close()


def show_students():
    cursor = db.cursor()

    query = "SELECT * FROM students"

    cursor.execute(query)

    students = cursor.fetchall()

    for student in students:
        print(
            f"ID: {student[0]}, name: {student[1]}, age: {student[2]}, score: {student[3]}")

    cursor.close()


def search_student(search_value, search_by):
    cursor = db.cursor()

    if search_by == "id":
        query = """
        SELECT * FROM students
        WHERE id = %s
        """
        values = (search_value,)

    elif search_by == "name":
        query = """
        SELECT * FROM students
        WHERE name = %s
        """
        values = (search_value,)

    else:
        print("Invalid search type.")
        cursor.close()
        return

    cursor.execute(query, values)

    students = cursor.fetchall()

    if students:
        for student in students:
            print(
                f"ID: {student[0]}, "
                f"name: {student[1]}, "
                f"age: {student[2]}, "
                f"score: {student[3]}"
            )
    else:
        print("Student not found.")

    cursor.close()


def delete_student(id):
    cursor = db.cursor()

    query = """
    DELETE FROM students
    WHERE id = %s
    """

    values = (id,)

    cursor.execute(query, values)

    if cursor.rowcount > 0:
        db.commit()
        print("Student deleted successfully.")
    else:
        print("Student not found.")

    cursor.close()


def statistics():
    cursor = db.cursor()

    query = """
    SELECT 
        COUNT(*),
        MAX(score),
        MIN(score),
        AVG(score)
    FROM students
    """

    cursor.execute(query)

    result = cursor.fetchone()

    if result[0] == 0:
        cursor.close()
        return "No information has been recorded!"

    number_of_students = result[0]
    highest_score = result[1]
    lowest_score = result[2]
    average_of_scores = result[3]

    query = """
    SELECT COUNT(*)
    FROM students
    WHERE score >= 10
    """

    cursor.execute(query)
    passes = cursor.fetchone()[0]

    query = """
    SELECT COUNT(*)
    FROM students
    WHERE score < 10
    """

    cursor.execute(query)
    fails = cursor.fetchone()[0]

    query = """
    SELECT id, name, score
    FROM students
    ORDER BY score DESC
    LIMIT 1
    """

    cursor.execute(query)
    best_student = cursor.fetchone()

    query = """
    SELECT id, name, score
    FROM students
    ORDER BY score ASC
    LIMIT 1
    """

    cursor.execute(query)
    worst_student = cursor.fetchone()

    cursor.close()

    return f"""
    Statistics:
    number_of_students: {number_of_students}
    highest_score: {highest_score}
    lowest_score: {lowest_score}
    average_of_scores: {average_of_scores}
    count of passes: {passes}
    count of failers: {fails}
    best student: ID {best_student[0]}, name: {best_student[1]}, score: {best_student[2]}
    worst student: ID {worst_student[0]}, name: {worst_student[1]}, score: {worst_student[2]}
    """


def edit_student(id, new_name, new_age, new_score):
    cursor = db.cursor()

    query = """
    UPDATE students
    SET name = %s,
        age = %s,
        score = %s
    WHERE id = %s
    """

    values = (new_name, new_age, new_score, id)

    cursor.execute(query, values)

    if cursor.rowcount > 0:
        db.commit()
        print("Student Updated!")
    else:
        print("Student not found")

    cursor.close()


def sort_students():
    cursor = db.cursor()

    choice = input("""
        Sort by score:
        1. Highest to Lowest
        2. Lowest to Highest
        Choose:
        """
                   )

    if choice == "1":
        query = """
        SELECT * FROM students
        ORDER BY score DESC
        """
    elif choice == "2":
        query = """
        SELECT * FROM students
        ORDER BY score ASC
        """
    else:
        print("Invalid choice.")
        cursor.close()
        return

    cursor.execute(query)
    students = cursor.fetchall()

    if students:
        print("The Students:")

        for student in students:
            print(
                f"ID: {student[0]}, name: {student[1]}, age: {student[2]}, score: {student[3]}")
    else:
        print("Students list is empty.")

    cursor.close()


def search_by_score(score):
    cursor = db.cursor()

    query = """
    SELECT * FROM students
    WHERE score >= %s
    """

    values = (score,)

    cursor.execute(query, values)
    students = cursor.fetchall()

    if students:
        for student in students:
            print(
                f"ID: {student[0]}, name: {student[1]}, age: {student[2]}, score: {student[3]}")
    else:
        print("No student found.")

    cursor.close()


def delete_all_students():
    cursor = db.cursor()

    query = """
    DELETE FROM students
    """

    cursor.execute(query)

    if cursor.rowcount > 0:
        db.commit()
        print("All students deleted successfully.")
    else:
        print("Students list is empty.")

    cursor.close()
