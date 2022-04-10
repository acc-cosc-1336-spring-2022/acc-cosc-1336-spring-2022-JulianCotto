import dictionary

def main(): #main menu function that displays the 2 routes to my defined menu option functions
    decision1 = str(input("1- Get P Matrix\t(Press 1)\n2- Exit\t\t(Press 2)")) #menu display with proper spacing and tabs

    if decision1 == "1": #if statement that will route user to the get_p_distance_matrix
        decision_1() #decision1 function defined below
    
    if decision1 == "2": #if statement that will route user to the exit function
        decision_2() #decision2 function defined below

    else:
        print("Invalid Input, Please select 1, 2") #informs user that their entry is invalid
        main() #sends user back to main menu function


def decision_1(): #decision1 function that takes user input and enters into the get_p_distance_matrix
    print("Prepare to enter 4 DNA strings of 10 character lengths") #prompts user to enter dna a 10 digit dna string
    dna1 = input("Please enter your first 10 character DNA string") #prompts user to enter dna a 10 digit dna string
    dna2 = input("Please enter your second 10 character DNA string") #prompts user to enter dna a 10 digit dna string
    dna3 = input("Please enter your third 10 character DNA string") #prompts user to enter dna a 10 digit dna string
    dna4 = input("Please enter your fourth 10 character DNA string") #prompts user to enter dna a 10 digit dna string
    listdna1 = list(dna1) #converts first user entry into list and assigns to listdna1
    listdna2 = list(dna2) #converts second user entry into list and assigns to listdna2
    listdna3 = list(dna3) #converts third user entry into list and assigns to listdna3
    listdna4 = list(dna4) #converts fourth user entry into list and assigns to listdna4
    twodlist = [listdna1, listdna2, listdna3, listdna4] #converts listdna1-4 into a 2-d list assigned to twodlist
    matrix = dictionary.get_p_distance_matrix(twodlist) #parses twodlist through g_p_distance_function and assigns to matrix
    print(matrix) #prints matrix
    new_decision = str(input("Do you have another DNA matrix to create? Y/N")) #asking the user if the want to run decision1 function again
    while new_decision.lower() == "n": #while the user doesnt want to run the decision1 function again
        main() #user will be routed back to the main menu
    while new_decision.lower() == "y": #while the user does want to run the decision1 function again
        decision_1() #user will be routed back to the decision1 function
        new_decision = str(input("Do you have another DNA matrix to create? Y/N")) #asking the user if the want to run decision1 function again to complete the loop
    

def decision_2(): #decision3 function that will thank the user and terminate the program
    print("Thank you for running the program!") #thanking the user for running the program
    quit() #built-in python function to terminate a program

print("Welcome to my DNA Program") #The first thing the program displays, welcoming the user to the program
main() #calling main menu function that will run all other parts of the program


