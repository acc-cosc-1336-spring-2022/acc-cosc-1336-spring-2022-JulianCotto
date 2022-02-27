from tkinter.messagebox import YES
import repetition


print("Homework 3 Menu\nPlease select a menu option\n1-Factorial\n2-Sum Odd Numbers\n3-exit")



if
    num = int(input("Please enter a number between 1 and 10"))
    if num > 0 and num < 10:
        factorial = repetition.get_factorial(num)
        print(factorial)
    else:   
        print("Invalid Entry")
        num = int(input("Please enter a number between 1 and 10"))
    print(repetition.get_factorial(num))

elif choice == 2:
    num = int(input("Please enter a number  greater than 0 and less than 100"))
    if num > 0 and num < 100:
        sums = repetition.sum_odd_numbers(num)
        print(sums)
    else: 
        print("Invalid Entry")
        num = int(input("Please enter a number  greater than 0 and less than 100"))
    print(repetition.sum_odd_numbers(num))
    


