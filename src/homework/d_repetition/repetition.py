#Homework 3

def get_factorial(num):
    factorial = 1
    for index in range(1, num):
        factorial = factorial * (index + 1)
    return factorial
        
def sum_odd_numbers(num):
    sum = 0
    index = 0
    while index <= num:
        if index % 2 != 0:
            sum = sum + index
        index = index + 1
    return sum