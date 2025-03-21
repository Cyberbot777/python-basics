# Grade Analyzer
# This script analyzes student grades using nested loops, while loops, and advanced conditionals.
def calculate_average(grades):
    """
    Calculate the average of a list of grades.

    Args:
        grades (list): A list of numeric grades.

    Returns:
        float: The average of the grades, or 0 if the list is empty.
    """
    if not grades:
        return 0
    return sum(grades) / len(grades)

def get_letter_grade(avg):
    """
    Assign a letter grade based on the average.

    Args:
        avg (float): The average grade.

    Returns:
        str: The letter grade (A, B, C, D, F).
    """
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

# Create dictionaries for multiple students
student1 = {"name": "Richard", "age": 25, "grades": [85, 90, 95, 88]}
student2 = {"name": "Alice", "age": 22, "grades": [90, 85, 92, 84]}
student3 = {"name": "Mike", "age": 29, "grades": [99, 86, 90]}

# Create a list of students
students = [student1, student2, student3]

# Nested loops: Analyze each student's grades
print("Analyzing student grades:")
for student in students:
    print(f"\nStudent: {student['name']}")
    total_above_90 = 0
    for grade in student["grades"]:
        if grade >= 90:
            total_above_90 += 1
    print(f"Number of grades 90 or above: {total_above_90}")

# Calculate averages and assign letter grades
print("\nCalculating averages and letter grades:")
for student in students:
    avg = calculate_average(student["grades"])
    letter_grade = get_letter_grade(avg)
    print(f"{student['name']}: Average = {avg:.2f}, Letter Grade = {letter_grade}")

# While loop: Allow the user to add a grade for a student
print("\nAdd a new grade for a student (enter 'quit' to stop):")
while True:
    student_name = input("Enter student name (or 'quit'): ").strip()
    if student_name.lower() == "quit":
        break
    # Find the student
    found = False
    for student in students:
        if student["name"].lower() == student_name.lower():
            found = True
            try:
                new_grade = float(input(f"Enter new grade for {student['name']}: "))
                if 0 <= new_grade <= 100:
                    student["grades"].append(new_grade)
                    print(f"Added grade {new_grade} to {student['name']}'s grades.")
                    # Recalculate average and letter grade
                    avg = calculate_average(student["grades"])
                    letter_grade = get_letter_grade(avg)
                    print(f"Updated: {student['name']}: Average = {avg:.2f}, Letter Grade = {letter_grade}")
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric grade.")
            break
    if not found:
        print(f"Student '{student_name}' not found.")
