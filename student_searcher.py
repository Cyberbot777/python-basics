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

# Function to remove a student by name
def remove_student(students, name):
    student = search_student(students, name)
    if student:
        # Confirm removal with the user
        confirm = input(f"Are you sure you want to remove {name}? (yes/no): ").lower()
        if confirm in ['yes', 'y']:
            students.remove(student)
            print(f"Removed {name} successfully!")
        else:
            print(f"Removal of {name} canceled.")
    else:
        print(f"Student '{name}' not found.")

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

# Main program with menu
def main():
    # Load existing students
    students = load_students()

    # Add some initial students if the list is empty
    if not students:
        add_student(students, "Richard", [85, 90, 95, 88])
        add_student(students, "Alice", [90, 85, 92, 84])
        add_student(students, "Mike", [99, 86, 90])

    while True:
        print("\nStudent Searcher Menu:")
        print("1. View all students")
        print("2. Search for a student")
        print("3. Add a student")
        print("4. Remove a student")
        print("5. Save and exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print("\nAll students:")
            for student in students:
                avg = calculate_average(student["grades"])
                print(f"{student['name']}: Grades {student['grades']}, Average Grade: {avg:.2f}")

        elif choice == "2":
            name = input("Enter student name to search: ")
            student = search_student(students, name)
            if student:
                avg = calculate_average(student["grades"])
                print(f"Found {student['name']}: Grades {student['grades']}, Average Grade: {avg:.2f}")
            else:
                print(f"Student {name} not found.")

        elif choice == "3":
            name = input("Enter student name: ")
            grades_input = input("Enter grades (comma-separated, e.g., 86,90,95):")
            try:
                grades = [int(g) for g in grades_input.split(",")]
                add_student(students, name, grades)
                print(f"Added {name} successfully!")
            except ValueError:
                print("Error: Grades must be numbers.")

        elif choice == "4":
            name = input("Enter student name to remove: ")
            remove_student(students, name)

        elif choice == "5":
            confirm = input("Are you sure you want to save and exit? (yes/y or no/n): ").lower()
            if confirm in ['yes', 'y']:
                save_students(students)
                print("Saved and exiting.")
                break
            elif confirm in ['no', 'n']:
                print("Exit canceled.")
            else:
                print("Invalid input. Exit canceled.")

        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
