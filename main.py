from qustion import qustions


print("welcome")

score = 0


for item in qustions:
    awnser = input(item["qustion"])

    if awnser.lower() == item["awnser"]:
        print("correct")
        score += 1
    else:
        print("wrong")

print("your score is:", score)