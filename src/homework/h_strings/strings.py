def get_hamming_distance(dna1 , dna2):
    list_dna1 = list(dna1)
    list_dna2 = list(dna2)
    counter = 0
    for i in range(len(list_dna1)):
        if list_dna1[i] != list_dna2[i]:
            counter += 1
    return counter

def reverse_string(string):
    rstr1 = ""
    indx = len(string)
    while indx > 0:
        rstr1 += string[ indx - 1 ]
        indx = indx - 1
    return rstr1

def listToString(s):   
    str1 = ""
    for letter in s: 
        str1 += letter 
    return str1 

def get_dna_complement(dna):
    reverse = reverse_string(dna)
    new_reverse = list(reverse)
    for i in range(len(new_reverse)):
        if new_reverse[i] == "T" or new_reverse[i] == "t":
            new_reverse[i] = "A"
        elif new_reverse[i] == "A" or new_reverse[i] == "a":
            new_reverse[i] = "T"
        elif new_reverse[i] == "G" or new_reverse[i] == "g":
            new_reverse[i] = "C"
        elif new_reverse[i] == "C" or new_reverse[i] == "c":
            new_reverse[i] = "G"
            i += 1

    new_reverse1 = listToString(new_reverse)
    return new_reverse1
    
    



    
    