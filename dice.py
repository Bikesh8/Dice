import random

playagain=True

while playagain:
    print (random.randint(1,6))
    again=input("Do you wanna play again? (y/n) : ")
    if again.lower()=="y":
        continue
    else:
        break

print("Thank you for playing")
    