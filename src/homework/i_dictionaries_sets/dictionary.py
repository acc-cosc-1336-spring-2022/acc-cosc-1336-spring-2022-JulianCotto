def get_p_distance(list1, list2):
    indx = 0
    diff = 0
    while indx < len(list1):
        if list1[indx] != list2[indx]:
            diff += 1
        indx += 1
    p_distance = diff / len(list1)
    return p_distance

def get_p_distance_matrix(twodlist):
    dist_matr = []
    for r_list in twodlist:
        row = []
        for c_list in twodlist:
            row.append(get_p_distance(r_list , c_list))
        dist_matr.append(row)
    return dist_matr