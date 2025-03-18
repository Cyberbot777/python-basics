student = {"name": "Richard", "age": 25, "grades": [85, 90, 95]}
student["grades"].append(88)
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
