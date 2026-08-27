students = [
    {
        "name": "Alice",
        "score": 85
    },
    {
        "name": "Bob",
        "score": 92
    },
    {
        "name": "Tom",
        "score": 76
    }
]


for student in students:
    print(student["name"], student["score"])

target = "Bob"

for student in students:
    if student["name"] == target:
        print(target, "的成绩是", student["score"])


for student in students:
    if student["name"] == "Tom":
        student["score"] = 88


new_student = {
    "name": "Lucy",
    "score": 95
}

students.append(new_student)



for student in students:
    if student["name"] == "Alice":
        students.remove(student)
        break


total = 0

for student in students:
    total += student["score"]

average = total / len(students)

print("平均分:", average)