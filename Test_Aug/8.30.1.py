import random
recommendations = {
    "travel":["China","Japan","New Zealand","The U.S.A","Mexico","Iceland","Antarctica"],
    "food":["Meat","Vegetables","Carbs","Fruits","Water"],
    "study":["Math","Programming","Mechanical Engineering"],
    "exercise":["running","playing badminton","swimming","riding","playing soccer"]
}

print("What do you want to do?\ntype 'off' to end\n")

while True:
    choice = input("\ntravel or food or study or exercise?\n")
    if choice == "off":
        print("Byebye")
        break
    
    if choice in recommendations:
        result = random.choice(recommendations[choice])
        print("recommended for you:",result)