from qustion import qustions

name = input("whats your name? ")

print("welcome")

score = 0


for item in qustions:
    awnser = input(item["qustion"])

    if awnser.lower() == item["awnser"]:
        print("correct")
        score += 1
    else:
        print("wrong")

print("your score is:", score, "out of", len(qustions))

if score == len(qustions):
    print("excellent job", name)
elif score >= 2:
    print("good job", name)
else:
    print("keep praticing", name)