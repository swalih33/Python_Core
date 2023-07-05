import random

fruits = ["apple","orange","banana"]
print("List=",fruits)

selection = str(input("enter your selection"))

comp_guess = random.randrange(0,2)
guess = fruits[comp_guess]

if selection==guess:
    print("you won")  

else:
    print("you lost")
print("coputer guess=",guess)
print("your selection=",selection)


