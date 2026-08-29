import random
replies = [
    "I'm here to offer you.",
    "Good forture wherever you go.",
    "May your day be full of good things.",
    "No worries.",
    "Just vibes.",
    "Good things loading...",
    "Good food,good mood.",
    "Good time,good person.",
    "All is well.",
    "Stay healthy.",
    "Safy trip.",
    "Have fun.",
    "So happy for you.",
    "Praying for you.",
    "Take a break.",
    "You are not interchangeable."

]

print("my_machine:Can you hear me?")
print("\n\ntype 'off' to end")

while True:
    user_input = input("user:")

    if user_input =="off":
        print("my_machine:see you next time.")
        break

    response = random.choice(replies)
    print("my_machine:",response)
