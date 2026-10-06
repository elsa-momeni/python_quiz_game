import os
from  dotenv import load_dotenv
from qustion import qustions


load_dotenv()

admin_password = os.getenv("QUIZ_ADMIN_PASWORD")

open_admin = input("do u want to open amin mode? yes/no: ")

if open_admin.lower() == "yes":
    entered_password = input("enter admin password: ")

    if entered_password == admin_password:
        print("admin! hi....")
    else:
        print("wrong password")



name = input("whats your name? ")

print("welcome")

score = 0


for item in qustions:
    awnser = input(item["print"])

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
with open("results.txt", "a") as file:
    file.write(f"{name} - {score}/{len(qustions)}\n") #3/4