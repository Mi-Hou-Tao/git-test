import datetime
import json
import os

FILE = "Birthday_capsule.json"
today = datetime.date.today()
def create_capsule():
    print("生日时间胶囊\n")

    answers = {}
    questions = [
        "现在最想实现的一件事？",
        "现在最喜欢什么？",
        "现在最担心什么？",
        "一年后的你，希望自己变成什么样？",
        "想对一年后的自己说什么？"
    ]
    for question in questions:
        answers[question] = input(question + '\n>')

    capsule = {
        "date": str(today),
        "answer":answers
    }

    with open(FILE,'w',encoding='utf-8') as f:
        json.dump(capsule,f,ensure_ascii=False,indent=4)

    print('\n已封存,请一年后打开它')

def open_capsule():
    with open(FILE,'r',encoding='utf-8') as f:
        capsule = json.load(f)
    print('\n时间胶囊')
    print(f'封存日期：{capsule["date"]}\n')

    for question,answer in capsule['answers'].items():
        print(question)
        print('->',answer)
        print()

if os.path.exists(FILE):
    open_capsule()
else:
    create_capsule()