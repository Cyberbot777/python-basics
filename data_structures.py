# Data Structures Practice
# This script demonstrates working with dictionaries and lists to manage student data.

# Create dictionaries for multiple students
student1 = {"name": "Richard", "age": 25, "grades": [85, 90, 95]}
student2 = {"name": "Alice", "age": 22, "grades": [90, 85, 92]}
student3 = {"name": "Mike", "age": 29, "grades": [99, 86, 90]}

# Add new grades to Richard and Alice
student1["grades"].append(88)
student2["grades"].append(84)

# Add major to Richard
student1["major"] = "Computer Science"

# Calculate and print Richard's average
average1 = sum(student1["grades"]) / len(student1["grades"])
print(f"Richard's updated info: {student1}")
print(f"Richard's average: {average1}")

# Create a list of students
students = [student1, student2, student3]

# Calculate averages for all students
print("\nCalculating averages for all students:")
for student in students:
    avg = sum(student["grades"]) / len(student["grades"])
    print(f"{student['name']}'s average: {avg}")

# Classify grades as A (90+) or B/lower for each student
print("\nClassifying grades:")
for student in students:
    print(f"\nGrades for {student['name']}:") # Added colon for consistency
    for grade in student["grades"]:
        if grade >= 90:  # Added space for readability
            print(f"{grade} is an A!")
        else:
            print(f"{grade} is a B or lower.")