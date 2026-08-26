students = []


# maghz ertebati barname
def main():
    while True:
        user_selection = show_menu()

        if user_selection == 1:
            name = input("name: ")
            age = int(input("age: "))
            score = float(input("score: "))

            add_student(name, age, score)

        elif user_selection == 2:
            show_students()

        elif user_selection == 3:
            who_to_search = input('''
            Enter the name of student: 
            ''')
            print(search_student(who_to_search))

        elif user_selection == 4:
            who_to_delete = input("Enter the name of student to remove: ")
            print(delete_student(who_to_delete))

        elif user_selection == 5:
            print(statistics())

        elif user_selection == 6:
            print('''
            good bye!!!
            ''')
            break

        elif user_selection == 7:
            who_to_edit = input("Enter the name of student you want to edit: ")
            edit_student(who_to_edit)

        elif user_selection == 8:
            sort_students()

        elif user_selection == 9:
            score = int(input("Enter the minimum score: "))
            search_by_score(score)

        elif user_selection == 10:
            delete_all_students()

        else:
            print("Please enter a valid number.")


# menuei ke karbar hengam RUN mibine
def show_menu():
    print(
        '''
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
        ''')

    user_selection = int(input("Choose: "))
    return user_selection


# karhaei ke system bayad anjam bede
def add_student(name, age, score):
    for student in students:
        if name == student[0]:
            print("Student already exists.")
            break
    else:
        student = [name, age, score]
        students.append(student)
        print('''
                    student added!
                    ''')


def show_students():
    if len(students) != 0:
        print("The Students: ")
        for index, student in enumerate(students):
            print(
                f"{index + 1}. name: {student[0]}, age: {student[1]}, score: {student[2]}")
    else:
        print("Student list is empty.")


def search_student(name):
    for student in students:
        if student[0] == name:
            return f'''Found!
            name: {student[0]}, age: {student[1]}, score: {student[2]}'''
    else:
        return "Student not found."


def delete_student(name):
    for index, student in enumerate(students):
        if student[0] == name:
            students.pop(index)
            return "Deleted Successfully"
    else:
        return "Student not found."


def statistics():
    if len(students) != 0:
        number_of_students = len(students)
        student_scores = []
        total_of_scores = 0
        passes_scores = []
        failed_scores = []

        for student in students:
            student_scores.append(student[2])
            total_of_scores += student[2]
            if student[2] >= 10:
                passes_scores.append(student[2])
            else:
                failed_scores.append(student[2])

        highest_score = max(student_scores)
        for student in students:
            if highest_score == student[2]:
                name_of_best_student = student[0]

        lowest_score = min(student_scores)
        for student in students:
            if lowest_score == student[2]:
                name_of_worst_student = student[0]

        average_of_scores = total_of_scores / len(students)

        return f'''Statistics:
        number_of_students: {number_of_students}, highest_score: {highest_score}, lowest_score: {lowest_score}, average_of_scores: {average_of_scores},
        count of passes: {len(passes_scores)}, count of failers: {len(failed_scores)}, 
        name of best student: {name_of_best_student}, name of worst student: {name_of_worst_student}
        '''
    else:
        return "No information has been recorded!"


def edit_student(name):
    for student in students:
        if student[0] == name:
            new_name = input("Enter the new name: ")
            new_age = int(input("Enter the new age: "))
            new_score = float(input("Enter the new score: "))

            student[0] = new_name
            student[1] = new_age
            student[2] = new_score

            print("Student edited!!!")
            break
    else:
        print("Student not found!!!")


def sort_students():
    if len(students) != 0:
        students.sort()
        print("The Students: ")
        for index, student in enumerate(students):
            print(
                f"{index + 1}. name: {student[0]}, age: {student[1]}, score: {student[2]}")
    else:
        print("Students list is empty.")


def search_by_score(score):
    if len(students) != 0:
        found = False
        for student in students:
            if student[2] >= score:
                print(f"{student[0]}, {student[1]}, {student[2]}")
                found = True
        if found == False:
            print("No student found.")
    else:
        print("Students list is empty.")


def delete_all_students():
    students.clear()
    print("All Students Deleted!!")


main()
