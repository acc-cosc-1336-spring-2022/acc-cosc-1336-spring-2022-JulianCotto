from strings import get_dna_complement, get_hamming_distance
def main():
    decision1 = str(input("1- Hamming Distance\t(Press 1)\n2- DNA Complement\t(Press 2)\n3- Exit\t\t\t(Press 3)"))

    if decision1 == "1":
        decision_1()
        new_decision = str(input("Do you have another DNA sequence to compare? Y/N"))
        while new_decision == "N":
            main()
        while new_decision == "Y":
            decision_1()
        new_decision = str(input("Do you have another DNA sequence to compare? Y/N"))
    
    elif decision1 == "2":
        decision_2()
        decision = str(input("Do you have another DNA sequence to add? Y/N"))
        while decision == "N":
            main()
        while decision == "Y":
            decision_2()
            decision = str(input("Do you have another DNA sequence to add? Y/N"))
            while decision == "N":
                main()
    
    while decision1 == "3":
        print("Thank you for running the program!")
        quit()


def decision_1():
    ham1 = input("Please enter 1st DNA Sequence")
    ham2 = input("Please enter 2nd DNA Sequence")
    ham3 = get_hamming_distance(ham1 , ham2)
    print("The hamming distance between DNA1 & DNA 2 is", ham3)
    new_decision = str(input("Do you have another DNA sequence to compare? Y/N"))
    while new_decision == "N":
        main()
    while new_decision == "Y":
        decision_1()
        new_decision = str(input("Do you have another DNA sequence to add? Y/N"))
        while new_decision == "N":
                main()
        

def decision_2():
    dna1 = input("Please enter DNA Sequence")
    dna2 = get_dna_complement(dna1)
    print("The DNA Complement is", dna2)
    decision = str(input("Do you have another DNA sequence to add? Y/N"))
    while decision == "N":
        main()
    while decision == "Y":
        decision_2()
        decision = str(input("Do you have another DNA sequence to add? Y/N"))
        while decision == "N":
                main()

def decision_3():
    print("Thank you for running the program!")

print("Welcome to my DNA Program")
main()
