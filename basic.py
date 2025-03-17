name = "Alex"
age = 25
height = 5.9
is_student = True
hobbies = ["reading", "gaming", "coding"]
hobbies.append("painting")
name = "Mike"

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is a student?", is_student)
print("Hobbies:", hobbies)

age = 10

if age >= 18:
    print("You are an adult!")
elif age < 13:
    print("You are a child.")
else:
    print("You are a minor.")

print("Counting from 1 to 10:")
for e in range(1, 11):
    if e % 2 == 0:
        print(e)

print("Counting down from 5:")
count = 5
while count > 0:
    print (count)
    count -= 1

def greet(name):
    return f"Hello {name}! How are you today?"

print(greet("Alex"))

def add_numbers(a, b):
    return a + b

print("Sum of 3 and 5:", add_numbers(3, 5))

def multiply_numbers(a, b):
    return a * b

print("Multiplied by 3 and 5:", multiply_numbers(3, 5))









