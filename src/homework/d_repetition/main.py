import repetition

def main():
    dec = input("Homework 3 Menu\nPlease select a menu option\n1-Factorial\n2-Sum Odd Numbers\n3-Exit")
    if dec == "1":
        num = input("Please enter a number greater than 0 and less than 10")
        while int(num) < 0 or int(num) > 10:
            print("Invalid Entry")
            num = input("Please enter a number greater than 0 and less than 10")
        fact = repetition.get_factorial(int(num))
        print(fact)
        dec0 = input("Do you want to quit? Y or N")
        if dec0.lower() == "y":
            print("Thank you for running this math program")
            quit()
        else:
            main()

    elif dec == "2":
        num1 = input("Please enter a number greater than 0 and less than 100")
        while int(num1) < 0 or int(num1) > 100:
            print("Invalid Entry")
            num1 = input("Please enter a number greater than 0 and less than 100")
        odd_sum = repetition.sum_odd_numbers(int(num1))
        print(odd_sum)
        dec1 = input("Do you want to quit? Y or N")
        if dec1.lower() == "y":
            print("Thank you for running this math program")
            quit()
        else:
            main()

    elif dec == "3":
        print("Goodbye")
        quit()

main()
