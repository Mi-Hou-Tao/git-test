def show_students(students):
    for student in students:
        print (student[0],":",student[1])
def update_score(students,name,new_score):
    for student in students:
        if student[0] == name:
            student[1] = new_score

def add_student(students,student):
    students.append(student)
def sort_students(students,name):
    for student in students:
        if student[0] == name:
            students.remove(student)
            break
def sort_students(students):
    students.sort(key=lambda x:x[1],reverse=True)

students = [
    ["xiaoyang9336",55],
    ["chatgpt",96],
    ["deepseek",95],
    ["doubao",94],
    ["jidundun",36],
    ["yangmiemie",28]
]

print("initial scores:")
show_students(students)

update_score(students,"xiaoyang9336",100)

add_student(students,["xiaohuang",54])

sort_students(students)

print("\nfinal scores:")
show_students(students)

top_student = students[0]

print("\n top student:")
print(top_student[0],top_student[1])