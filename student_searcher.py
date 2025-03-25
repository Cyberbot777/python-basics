# Student Searcher Program
# This script manages a list of students, allows searching by name, and saves data to a file.

# Function to calculate average grade
def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

# Function to add a student
def add_student(students, name, grades):
    student = {"name": name, "grades": grades}
    students.append(student)

# Function to search for a student by name
def search_student(students, name):
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    return None

# Function to save students to a file
def save_students(students, filename="students.txt"):
    try:
        with open(filename, 'w') as file:
            for student in students:
                file.write(f"{student['name']}: {student['grades']}\n")
    except IOError:
        print("Error: Could not save to file.")

# Function to load students from a file
def load_students(filename="students.txt"):
    students = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Skip empty lines
                if not line.strip():
                    continue
                try:
                    # Split the line into name and grades
                    name, grades_str = line.strip().split(": ", 1)
                    # Remove brackets and split grades
                    grades_str = grades_str.strip("[]")
                    # Split grades and filter out empty strings
                    grade_strings = [g for g in grades_str.split(", ") if g]
                    # Convert to integers
                    grades = [int(g) for g in grade_strings]
                    add_student(students, name, grades)
                except ValueError as e:
                    print(f"Error parsing line '{line.strip()}': {e}")
                except Exception as e:
                    print(f"Unexpected error parsing line '{line.strip()}': {e}")
    except FileNotFoundError:
        print("File not found. Starting with an empty student list.")
    except IOError:
        print("Error: Could not read from file.")
    return students  # Moved return outside the try block

# Main program
def main():
    # Load existing students
    students = load_students()

    # Add some initial students if the list is empty
    if not students:
        add_student(students, "Richard", [85, 90, 95, 88])
        add_student(students, "Alice", [90, 85, 92, 84])
        add_student(students, "Mike", [99, 86, 90])

    # Search for a student
    name = input("Enter student name to search: ")
    student = search_student(students, name)
    if student:
        avg = calculate_average(student["grades"])
        print(f"Found {student['name']}: Grades {student['grades']}, Average Grade: {avg:.2f}")
    else:
        print(f"Student {name} not found.")

    # Print all students
    print("\nAll students:")
    for student in students:
        avg = calculate_average(student["grades"])
        print(f"{student['name']}: Grades {student['grades']}, Average Grade: {avg:.2f}")

    # Save students before exiting
    save_students(students)

# Run the program
if __name__ == "__main__":
    main()