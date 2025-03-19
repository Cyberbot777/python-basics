# Data Structures Practice
# This script demonstrates working with dictionaries and lists to manage student data.

# Function to calculate average grades
def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

# Create dictionaries for multiple students
student1 = {"name": "Richard", "age": 25, "grades": [85, 90, 95]}
student2 = {"name": "Alice", "age": 22, "grades": [90, 85, 92]}
student3 = {"name": "Mike", "age": 29, "grades": [99, 86, 90]}

# Add new grades to Richard and Alice
student1["grades"].append(88)
student2["grades"].append(84)

# Add major to Richard
student1["major"] = "Computer Science"

# Calculate and print Richard's average using the function
average1 = calculate_average(student1["grades"])
print(f"Richard's updated info: {student1}")
print(f"Richard's average: {average1:.2f}")

# Create a list of students
students = [student1, student2, student3]

# Calculate averages for all students using the function
print("\nCalculating averages for all students:")
for student in students:
    avg = calculate_average(student["grades"])
    print(f"{student['name']}'s average: {avg:.2f}")

# Sort each student's grades in descending order and print them
print("\n\nSorted grades (descending):")
for student in students:
    sorted_grades = sorted(student["grades"], reverse=True)
    print(f"{student['name']}'s sorted grades: {sorted_grades}")

# Classify grades as A (90+) or B/lower for each student
print("\nClassifying grades:")
for student in students:
    print(f"\nGrades for {student['name']}:")
    for grade in student["grades"]:
        if grade >= 90:
            print(f"{grade} is an A!")
        else:
            print(f"{grade} is a B or lower.")

# Add passed status based on average
print("\nPass/Fail status:")
for student in students:
    avg = calculate_average(student["grades"])
    student["passed"] = avg >= 90
    print(f"{student['name']} {'Passed' if student['passed'] else 'Failed'} with average {avg:.2f}")
