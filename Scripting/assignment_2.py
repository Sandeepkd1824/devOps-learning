# Initial dictionary for student grades
grades = {
    "sandeep": "B",
    "manwal": "C",
    "kd": "D"
}

while True:
    print("\nSelect an option:")
    print("1. Grade Checker (Enter marks to get grade)")
    print("2. Student Grades (View/Add/Update)")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        # Grade Checker
        try:
            marks = int(input("Enter your marks: "))
            if marks >= 90:
                print("Grade A")
            elif marks >= 80:
                print("Grade B")
            elif marks >= 70:
                print("Grade C")
            elif marks >= 60:
                print("Grade D")
            else:
                print("Fail")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "2":
        # Student Grades
        while True:
            print("\nStudent Grades Menu:")
            print("a. View all grades")
            print("b. Add a new student")
            print("c. Update an existing student's grade")
            print("d. Back to main menu")
            
            sub_choice = input("Enter your choice (a/b/c/d): ").lower()
            
            if sub_choice == "a":
                for student, grade in grades.items():
                    print(student, ":", grade)
            elif sub_choice == "b":
                name = input("Enter student's name: ")
                grade = input("Enter student's grade: ").upper()
                grades[name] = grade
                print(f"{name} added with grade {grade}.")
            elif sub_choice == "c":
                name = input("Enter student's name to update: ")
                if name in grades:
                    grade = input("Enter new grade: ").upper()
                    grades[name] = grade
                    print(f"{name}'s grade updated to {grade}.")
                else:
                    print(f"{name} not found in records.")
            elif sub_choice == "d":
                break
            else:
                print("Invalid choice. Try again.")

    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
