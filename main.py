import database


# Program Communication Brain
def main():
    while True:
        user_selection = show_menu()

        if user_selection == 1:
            name = input("name: ")
            age = int(input("age: "))
            score = float(input("score: "))

            database.add_student(name, age, score)
            print("Student added!")

        elif user_selection == 2:
            database.show_students()

        elif user_selection == 3:
            search_by = input("Search by ID or name: ").lower()

            if search_by == "id":
                search_value = int(input("Enter student ID: "))
                database.search_student(search_value, "id")

            elif search_by == "name":
                search_value = input("Enter student name: ")
                database.search_student(search_value, "name")

            else:
                print("Invalid search type.")

        elif user_selection == 4:
            student_id = int(input("Enter student ID to delete: "))
            database.delete_student(student_id)

        elif user_selection == 5:
            print(database.statistics())

        elif user_selection == 6:
            print("""
            good bye!!!
            """)
            break

        elif user_selection == 7:
            student_id = int(input("Enter student ID you want to edit: "))
            new_name = input("Enter the new name: ")
            new_age = int(input("Enter the new age: "))
            new_score = float(input("Enter the new score: "))

            database.edit_student(
                student_id,
                new_name,
                new_age,
                new_score
            )

        elif user_selection == 8:
            database.sort_students()

        elif user_selection == 9:
            score = float(input("Enter the minimum score: "))
            database.search_by_score(score)

        elif user_selection == 10:
            database.delete_all_students()

        else:
            print("Please enter a valid number.")


# The menu that the user sees
def show_menu():
    print("""
    ======== Student Management ========
    1. Add Student
    2. Show Students
    3. Search Student
    4. Delete Student
    5. Statistics
    6. Exit
    7. Edit Student
    8. Sort Students
    9. Search By Score
    10. Delete All Students
    """)

    user_selection = int(input("Choose: "))
    return user_selection


main()
