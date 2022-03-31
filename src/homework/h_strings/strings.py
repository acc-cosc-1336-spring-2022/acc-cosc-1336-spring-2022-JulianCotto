
def reverse_string(string):
    rstr1 = ""
    indx = len(string)
    while indx > 0:
        rstr1 += string[ indx - 1 ]
        indx = indx - 1
    return rstr1

def listToString(s):   
    str1 = ""
    for ele in s: 
        str1 += ele 
    return str1 

def get_hamming_distance(dna1 , dna2):
    list_dna1 = list(dna1)
    list_dna2 = list(dna2)
    counter = 0
    if list_dna1[0] != list_dna2[0]:
        counter += 1
    if list_dna1[1] != list_dna2[1]:
        counter += 1
    if list_dna1[2] != list_dna2[2]:
        counter += 1
    if list_dna1[3] != list_dna2[3]:
        counter += 1
    if list_dna1[4] != list_dna2[4]:
        counter += 1
    if list_dna1[5] != list_dna2[5]:
        counter += 1
    if list_dna1[6] != list_dna2[6]:
        counter += 1
    if list_dna1[7] != list_dna2[7]:
        counter += 1
    if list_dna1[8] != list_dna2[8]:
        counter += 1
    if list_dna1[9] != list_dna2[9]:
        counter += 1
    if list_dna1[10] != list_dna2[10]:
        counter += 1
    if list_dna1[11] != list_dna2[11]:
        counter += 1
    if list_dna1[12] != list_dna2[12]:
        counter += 1
    if list_dna1[13] != list_dna2[13]:
        counter += 1
    if list_dna1[14] != list_dna2[14]:
        counter += 1
    if list_dna1[15] != list_dna2[15]:
        counter += 1
    if list_dna1[16] != list_dna2[16]:
        counter += 1
    return counter


def get_dna_complement(dna):
    reverse = reverse_string(dna)
    new_reverse = list(reverse)
    if new_reverse[0] == "T":
        new_reverse[0] = "A"
    elif new_reverse[0] == "A":
        new_reverse[0] = "T"
    elif new_reverse[0] == "G":
        new_reverse[0] = "C"
    elif new_reverse[0] == "C":
        new_reverse[0] = "G"
    if new_reverse[1] == "T":
        new_reverse[1] = "A"
    elif new_reverse[1] == "A":
        new_reverse[1] = "T"
    elif new_reverse[1] == "G":
        new_reverse[1] = "C"
    elif new_reverse[1] == "C":
        new_reverse[1] = "G"
    if new_reverse[2] == "T":
        new_reverse[2] = "A"
    elif new_reverse[2] == "A":
        new_reverse[2] = "T"
    elif new_reverse[2] == "G":
        new_reverse[2] = "C"
    elif new_reverse[2] == "C":
        new_reverse[2] = "G"
    if new_reverse[3] == "T":
        new_reverse[3] = "A"
    elif new_reverse[3] == "A":
        new_reverse[3] = "T"
    elif new_reverse[3] == "G":
        new_reverse[3] = "C"
    elif new_reverse[3] == "C":
        new_reverse[3] = "G"    
    if new_reverse[4] == "T":
        new_reverse[4] = "A"
    elif new_reverse[4] == "A":
        new_reverse[4] = "T"
    elif new_reverse[4] == "G":
        new_reverse[4] = "C"
    elif new_reverse[4] == "C":
        new_reverse[4] = "G" 
    if new_reverse[5] == "T":
        new_reverse[5] = "A"
    elif new_reverse[5] == "A":
        new_reverse[5] = "T"
    elif new_reverse[5] == "G":
        new_reverse[5] = "C"
    elif new_reverse[5] == "C":
        new_reverse[5] = "G"
    if new_reverse[6] == "T":
        new_reverse[6] = "A"
    elif new_reverse[6] == "A":
        new_reverse[6] = "T"
    elif new_reverse[6] == "G":
        new_reverse[6] = "C"
    elif new_reverse[6] == "C":
        new_reverse[6] = "G"
    if new_reverse[7] == "T":
        new_reverse[7] = "A"
    elif new_reverse[7] == "A":
        new_reverse[7] = "T"
    elif new_reverse[7] == "G":
        new_reverse[7] = "C"
    elif new_reverse[7] == "C":
        new_reverse[7] = "G"
    if new_reverse[8] == "T":
        new_reverse[8] = "A"
    elif new_reverse[8] == "A":
        new_reverse[8] = "T"
    elif new_reverse[8] == "G":
        new_reverse[8] = "C"
    elif new_reverse[8] == "C":
        new_reverse[8] = "G"
    if new_reverse[9] == "T":
        new_reverse[9] = "A"
    elif new_reverse[9] == "A":
        new_reverse[9] = "T"
    elif new_reverse[9] == "G":
        new_reverse[9] = "C"
    elif new_reverse[9] == "C":
        new_reverse[9] = "G"
    new_reverse1 = listToString(new_reverse)
    
    return new_reverse1
    
    



    
    