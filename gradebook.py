# Initialize an empty dictionary of student grades
student_grades = {}

# Function to add a student and grade
def add_student(name, grade):
    student_grades[name] = grade
    print(f"Student {name} was given the grade {grade}")

# Function to remove a student
def remove_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"Student {name} was removed")
    else:
        print(f"Student {name} was not found")

# Function to display all students and their grades
def display_students():
    for student, grade in student_grades.items():
        print(f"{student}: {grade}")

# Function to update a student's grade
def update_grade(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name}'s grade was updated to {grade}")
    else:
        print(f"No student with the name {name} was found")

# Function to find a student's grade
def find_grade(name):
    if name in student_grades:
        print(f"{name}'s grade is {student_grades[name]}")
    else:
        print(f"Student {name} was not found")

# Function to calculate average grade of students
def average_grade():
    total = sum(student_grades.values())
    
    average = total / len(student_grades)
    rounded_average = round(average, 1)
    
    print(f"Average grade across students is {rounded_average}")

# Add some students
add_student("Emily", 3.6)
add_student("Isabelle", 3.1)
add_student("Renee", 3.9)
add_student("Ethan", 2.9)

# Display students and their grades
display_students()

# Update a student's grade
update_grade("Renee", 4.0)

# Remove a student
remove_student("Ethan")
remove_student("Robert")

# Display students and their grades again
display_students()

# Find grade of some students
find_grade("Renee")
find_grade("Ethan")

# Find average grade of students
average_grade()