

student1 = {"name": "Richard", "age": 25, "grades": [85, 90, 95]}
student2 = {"name": "Alice", "age": 22, "grades": [90, 85, 92]}
student3 = {"name": "Mike", "age": 29, "grades": [99, 86, 90]}

student1["grades"].append(88)
student2["grades"].append(84)

student1["major"] = "Computer Science"

average1 = sum(student1["grades"]) / len(student1["grades"])
print(f"Richard's updated info: {student1}")
print(f"Richard's average : {average1}")

students = [student1, student2, student3]

print("\nCalculating averages for all students:")
for student in students:
    avg = sum(student["grades"]) / len(student["grades"])
    print(f"{student['name']}'s : {avg}")

print("\nClassifying grades:")
for student in students:
    print(f"\nGrades for {student['name']}")
    for grade in student["grades"]:
        if grade >= 90:
            print(f"{grade} is an A!")
        else:
            print(f"{grade} is a B or lower.")