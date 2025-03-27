# Student Searcher Program
# This script manages a list of students, allows searching by name or average, and saves data to a file.

# Function to calculate average grade
def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

# Function to validate grades
def validate_grades(grades):
    for grade in grades:
        if not (0 <= grade <= 100):
            return False
    return True

# Function to add a student with validation
def add_student(students, name, grades):
    if not validate_grades(grades):
        raise ValueError("Grades must be between 0 and 100")
    student = {"name": name, "grades": grades}
    students.append(student)

# Function to search for a student by name (exact match)
def search_student(students, name):
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    return None

# Function to search for students by partial name
def search_students_by_partial_name(students, partial_name):
    results = []
    for student in students:
        if partial_name.lower() in student["name"].lower():
            results.append(student)
    return results

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
        print(f"Student {name} not found.")

# Function to search for student by average grade range
def search_students_by_average(students, min_avg, max_avg):
    result = []
    for student in students:
        avg = calculate_average(student["grades"])
        if min_avg <= avg <= max_avg:
            result.append(student)
    return result

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
    return students

# Main program with a menu
def main():
    # Load existing students
    students = load_students()

    # Add some initial students if the list is empty
    if not students:
        add_student(students, "Richard", [85,90,95,88])
        add_student(students, "Alice", [90, 85, 92, 84])
        add_student(students, "Mike", [99, 86, 90])

    while True:
        print("\nStudent Searcher Menu:")
        print("1. View all students")
        print("2. Search for a student by name (exact match)")
        print("3. Search for students by partial name")
        print("4. Search for a student by average grade range")
        print("5. Add a student")
        print("6. Remove a student")
        print("7. Save and exit")
        choice = input("Enter your choice (1-7): ")

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
            partial_name = input("Enter partial name to search: ")
            results = search_students_by_partial_name(students, partial_name)
            if results:
                print("\nStudents matching partial name:")
                for student in results:
                    avg = calculate_average(student["grades"])
                    print(f"{student['name']}: Grades {student['grades']}, Average Grade: {avg:.2f}")
            else:
                print(f"No students found matching {partial_name}.")

        elif choice == "4":
            try:
                min_avg = float(input("Enter minimum average: "))
                max_avg = float(input("Enter maximum average: "))
                if min_avg > max_avg:
                    print("Minimum average cannot be greater than maximum average.")
                    continue
                results = search_students_by_average(students, min_avg, max_avg)
                if results:
                    print("\nStudents within average range:")
                    for student in results:
                        avg = calculate_average(student["grades"])
                        print(f"{student['name']}: Grades {student['grades']}, Average Grade: {avg:.2f}")
                else:
                    print("No students found in that average range.")
            except ValueError:
                print("Error: Averages must be numbers")

        elif choice == "5":
            name = input("Enter student name: ")
            grades_input = input("Enter grades (comma-separated, e.g., 86,90,95):")
            try:
                grades = [int(g) for g in grades_input.split(",")]
                add_student(students, name, grades)
                print(f"Added {name} successfully!")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "6":
            name = input("Enter student name to remove: ")
            remove_student(students, name)

        elif choice == "7":
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


