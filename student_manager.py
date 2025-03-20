# Student Manager
# This script manages student data, calculates averages, and saves/loads data to/from a file.

def calculate_averages(grades, passing_threshold=90):
    """
    Calculate the average of a list of grades and determine pass/fail status.
    
    Args:
        grades (list): A list of numeric grades.
        passing_threshold (float): The threshold for passing (default is 90).
            
    Returns:
        tuple: (average, passed) - The average of the grades and wh ether the student passed.
    """
    if not grades:
        return 0, False
    avg = sum(grades) / len(grades)
    passed = avg >= passing_threshold
    return avg, passed

# Create dictionaries for multiple students
student1 = {"name": "Richard", "age": 25, "grades": [85, 90, 95]}
student2 = {"name": "Alice", "age": 22, "grades": [90, 85, 92]}
student3 = {"name": "Mike", "age": 29, "grades": [99, 86, 90]}

# Add new grades to Richard and Alice
student1["grades"].append(88)
student2["grades"].append(84)

# Add major to Richard
student1["major"] = "Computer Science"

# Create a list of students
students = [student1, student2, student3]

# Calculate averages and pass/fail status for all students
print("Calculating averages and pass/fail status:")
for student in students:
    avg, passed = calculate_averages(student["grades"])
    student["average"] = avg
    student["passed"] = passed
    print(f"{student['name']}: Average = {avg:.2f}, {'Passed' if passed else 'Failed'}")

# Save student data to a file
with open("students.txt", "w") as file:
    for student in students:
        file.write(f"Name: {student['name']}, Average: {student['average']:.2f}, Passed: {student['passed']}\n")

# Read student data from the file and print it
print("\nReading student data from file:")
with open("students.txt", "r") as file:
    print(file.read())