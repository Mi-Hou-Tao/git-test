import time
import random

stars = ["·", "✦", "⋆", "·", "✧"]

for i in range(20):
    line = ""

    for j in range(40):
        line += random.choice(stars)

    print(line)
    time.sleep(0.2)