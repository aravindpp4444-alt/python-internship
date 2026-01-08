students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    score = int(input(f"Enter score of {name}: "))

    students.append({"name": name, "score": score})

# Average score
total = sum(student["score"] for student in students)
average = total / n

# Highest and lowest
highest = max(students, key=lambda x: x["score"])
lowest = min(students, key=lambda x: x["score"])

# Passed students
passed_students = [s["name"] for s in students if s["score"] >= 40]

print("\n--- Results ---")
print("Average Score:", average)
print("Highest Score:", highest["score"], "-", highest["name"])
print("Lowest Score:", lowest["score"], "-", lowest["name"])
print("Passed Students:", passed_students)

print("\n--- Grades ---")
for student in students:
    score = student["score"]

    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 40:
        grade = "D"
    else:
        grade = "F"

    print(student["name"], ":", grade)
