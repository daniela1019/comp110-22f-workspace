from random import randint
# elif is the same as else-if, just shortened; first like is the if statement,
# everything else is the else statement 

question: str = input("What is your yes/no question? ")
response: int = randint(0,3)

if response == 0:
    print("Yes, def")
elif response == 1:
    print("Ask again later")
elif response == 2:
    print("Yes ofc")
else:
    print("My sources say no")
