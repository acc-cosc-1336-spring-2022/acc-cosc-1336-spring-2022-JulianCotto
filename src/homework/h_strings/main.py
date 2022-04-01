from strings import get_dna_complement, get_hamming_distance
def main(): #main menu function that displays the 3 routes to my defined menu option functions
    decision1 = str(input("1- Hamming Distance\t(Press 1)\n2- DNA Complement\t(Press 2)\n3- Exit\t\t\t(Press 3)")) #menu display with proper spacing and tabs

    if decision1 == "1": #if statement that will route user to the hamming distance function
        decision_1() #decision1 function defined below
        
    elif decision1 == "2": #if statement that will route the user to dna complement function
        decision_2() #decision2 function defined below
        
    elif decision1 == "3": #if statement that will run decision3 function defined below
        decision_3() #user will be routed to decision3 function



def decision_1(): #decision1 function that takes user input and enters into the get_hamming_distance function
    ham1 = input("Please enter 1st DNA Sequence") #Asking user to fill in parameter ham1
    ham2 = input("Please enter 2nd DNA Sequence") #Asking user to fill in parameter ham2
    ham3 = get_hamming_distance(ham1 , ham2) #setting hamming distance, when user created parameters (ham1, ham2) are parsed through it, equal to ham3
    print("The hamming distance between DNA1 & DNA 2 is", ham3) #print statement calling ham3 and displaying it to the user
    new_decision = str(input("Do you have another DNA sequence to compare? Y/N")) #asking the user if the want to run decision1 function again
    while new_decision.lower() == "n": #while the user doesnt want to run the decision1 function again
        main() #user will be routed back to the main menu
    while new_decision.lower() == "y": #while the user does want to run the decision1 function again
        decision_1() #user will be routed back to the decision1 function
        new_decision = str(input("Do you have another DNA sequence to compare? Y/N")) #asking the user if the want to run decision1 function again to complete the loop
        
        

def decision_2(): #decision2 function that takes user input and enters into the get_dna_complement function
    dna1 = input("Please enter DNA Sequence") #Asking user to fill in parameter DNA1
    dna2 = get_dna_complement(dna1) #setting dna_complement, when user created parameter (dna1) are parsed through it, equal to dna2
    print("The DNA Complement is", dna2) #print statement calling dna2 and displaying it to the user
    decision = str(input("Do you have another DNA sequence to add? Y/N")) #asking the user if they want to run decision2 function again
    while decision.lower() == "n": #while the user doesnt want to run the decision2 function again
        main() #user will be routed back to the main menu
    while decision.lower() == "y": #while the user does want to run the decision2 function again
        decision_2() #user will be routed back to the decision2 function
        decision = str(input("Do you have another DNA sequence to add? Y/N")) #asking the user if the want to run decision2 function again to complete the loop
    

def decision_3(): #decision3 function that will thank the user and terminate the program
    print("Thank you for running the program!") #thanking the user for running the program
    quit() #built-in python function to terminate a program

print("Welcome to my DNA Program") #The first thing the program displays, welcoming the user to the program
main() #calling main menu function that will run all other parts of the program
