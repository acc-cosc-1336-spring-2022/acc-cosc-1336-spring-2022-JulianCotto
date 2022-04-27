import random

class Die:

    def roll(self):
        __roll_value = random.randint(1, 6)
        return __roll_value

    def get_roll_value(self):
        return self.roll()

    def __str__(self):
        return str("The rolled value is {0}".format(self.get_roll_value()))

def main():
    decision = "n"
    die = Die()
    decision = input("Do you want to roll the Die? y or n?")
    while decision.lower() == "y":
        print(die)
        decision = input("Do you want to roll the Die again? y or n?")
    while decision.lower() == "n":
        print("Thanks for playing!!")
        quit()
    else:
        print("Invalid Input. Enter y or n")
        main()
