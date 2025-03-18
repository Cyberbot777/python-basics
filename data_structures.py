student = {"name": "Richard", "age": 25, "grades": [85, 90, 95]}
student2 = {"name": "Alice", "age": 22, "grades": [90, 85, 92]}
student3 = {"name": "Mike", "age": 29, "grades": [99, 86, 90]}
student["grades"].append(88)
student2["grades"].append(84)
average = sum(student["grades"]) / len(student["grades"])
print(f"Student: {student}")
print(f"Average grade: {average}")

for grade in student["grades"]:
    if grade >=90:
        print(f"{grade} is an A!")
    else:
        print(f"{grade} is a B or lower.")

student["major"] = "Computer Science"
print(f"Student with major: {student}")

students = [student, student2, student3]
for s in students:
    avg = sum(s["grades"]) / len(s["grades"])
    print(f"{s['name']}'s average: {avg}")