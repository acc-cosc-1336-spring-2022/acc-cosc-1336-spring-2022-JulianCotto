def get_options_ratio(option, total):
    value = option/total
    return value

def get_faculty_rating(value):
    if value == 1:
        rating = "Perfect!!"
    elif value >= .9 and value < 1:
        rating = "Excellent"
    elif value >= .8 and value < .9:
        rating = "Very Good"  
    elif value >= .7 and value < .8:
        rating = "Good" 
    elif value >= .6 and value < .7:
        rating = "Needs Improvement" 
    elif value >= 0 and value <= .59:
        rating = "Unacceptable"
    else:
        print("Invalid Entry!")
    return rating

 

    
