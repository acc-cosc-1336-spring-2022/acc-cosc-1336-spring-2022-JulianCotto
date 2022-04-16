# def get_p_distance(list1, list2):
#     indx = 0
#     diff = 0
#     while indx < len(list1):
#         if list1[indx] != list2[indx]:
#             diff += 1
#         indx += 1
#     p_distance = diff / len(list1)
#     return p_distance

# def get_p_distance_matrix(twodlist):
#     dist_matr = []
#     for r_list in twodlist:
#         row = []
#         for c_list in twodlist:
#             row.append(get_p_distance(r_list , c_list))
#         dist_matr.append(row)
#     return dist_matr

def add_inventory(dictionary, widget_name, quantity):
    if widget_name not in dictionary:
        dictionary[widget_name] = quantity
    else:
        dictionary[widget_name] += quantity
    return dictionary
    
def remove_inventory(dictionary, widget_name):
    if widget_name in dictionary:
        del dictionary[widget_name]
        print("Record Deleted")
    else:
        print("Item Not Found")
            
