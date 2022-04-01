def get_hamming_distance(dna1 , dna2): #Compares 2 DNA strings for non-matching characters
    list_dna1 = list(dna1) #Covert dna1 into a list
    list_dna2 = list(dna2) #Covert dna2 into a list
    counter = 0 #counter at 0 as there are no non-matching characters before comparison
    for i in range(len(list_dna1)): #allow the entry of a DNA string of any length
        if list_dna1[i] != list_dna2[i]: #The code that recognizes non matching characters
            counter += 1 #Counter increments each time a non-matching characters is identified
    return counter

def reverse_string(string): #Code that reverse an inputted string
    rstr1 = "" #string of any value
    indx = len(string) #string of any length = index
    while indx > 0: #while index is larger than string
        rstr1 += string[ indx - 1 ] #code that reverses the string
        indx = indx - 1 #index decremented by 1
    return rstr1 #return rstr1 value that is now the string reversed

def listToString(s):   #function to turn list into string
    str1 = "" #string of any value
    for letter in s: #for letters in list
        str1 += letter #list converted to string
    return str1 #return string

def get_dna_complement(dna): #function to return dna complement
    reverse = reverse_string(dna) #pass dna parameter through reverse string function
    new_reverse = list(reverse) #convert reveresed dna parameter into a list
    for i in range(len(new_reverse)): #for positions in a list of any size
        if new_reverse[i].lower() == "t": #if position i is == "t" or "T"
            new_reverse[i] = "A" #position i is equal to "A"
        elif new_reverse[i].lower() == "a": #if position i is == "a" or "A"
            new_reverse[i] = "T" #position i is equal to "T"
        elif new_reverse[i].lower() == "g": #if position i is == "g" or "G"
            new_reverse[i] = "C" #position i is equal to "C"
        elif new_reverse[i].lower() == "c": #if position i is == "c" or "C"
            new_reverse[i] = "G" #position i is equal to "G"
            i += 1 #position incremented by one and for loop ran until length of list has been reached

    new_reverse1 = listToString(new_reverse) #pass list through listtostring function so output will pass test cases
    return new_reverse1 #return reversed and value replaced string
    
    



    
    