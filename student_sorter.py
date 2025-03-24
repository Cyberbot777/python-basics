# Student Sorter
# This script implements bubble sort and uses it to sort students by their averages.

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

def bubble_sort(arr):
    """
    Sort a list using the bubble sort algorithm.

    Args:
        arr (list): A list of numbers to sort.

    Returns:
        list: The sorted list in ascending order.
    """
    if not arr:
        return arr
        # Check if all elements are comparable
    for item in arr:
        if not isinstance(item, (int, float)):
            raise TypeError(f"All elements must be numbers, found {item}")
    n = len(arr)
    for i in range(n):
        # Flag to optimize by breaking if no swaps are needed
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            if not swapped:
                break
    return arr

# Create dictionaries for multiple students
student1 = {"name": "Richard", "age": 25, "grades": [85, 90, 95, 88]}
student2 = {"name": "Alice", "age": 22, "grades": [90, 85, 92, 84]}
student3 = {"name": "Mike", "age": 29, "grades": [99, 86, 90]}

# Create a list of students
students = [student1, student2, student3]

# Calculate averages for all students
print("Calculating student averages:")
for student in students:
    avg = calculate_average(student["grades"])
    student["average"] = avg
    print(f"{student['name']}: Average = {avg:.2f}")

# Test bubble sort on a sample list
sample_list = [64, 34, 25, 12, 22, 11, 90]
print("\nTesting sort sample list")
print(f"Original list: {sample_list}")
sorted_list = bubble_sort(sample_list.copy())
print(f"Sorted list: {sorted_list}")

# Sort students by their averages using bubble sort (ascending)
print("\nSorting students by average (using bubble sort, ascending):")
averages = [student["average"] for student in students]
sorted_averages = bubble_sort(averages.copy())
# Map sorted averages back to students
sorted_students = []
for avg in sorted_averages:
    for student in students:
        if student["average"] == avg and student not in sorted_students:
            sorted_students.append(student)
            break
# Print sorted students
for student in sorted_students:
    print(f"{student['name']}: Average = {student['average']:.2f}")

# Sort students by their averages using bubble sort (descending)
print("\nSorting students by average (using bubble sort, descending):")
sorted_averages_desc = bubble_sort(averages.copy())
sorted_averages_desc.reverse()  # Reverse for descending order
# Map sorted averages back to students
sorted_students_desc = []
for avg in sorted_averages_desc:
    for student in students:
        if student["average"] == avg and student not in sorted_students_desc:
            sorted_students_desc.append(student)
            break
# Print sorted students
for student in sorted_students_desc:
    print(f"{student['name']}: Average = {student['average']:.2f}")

# Compare with Python's built-in sorting
print("\nSorting students by average (using built-in sort, for comparison):")
sorted_students_builtin = sorted(students, key=lambda x: x["average"])
for student in sorted_students_builtin:
    print(f"{student['name']}: Average = {student['average']:.2f}")