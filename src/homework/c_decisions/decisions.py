#Get Options Ratio
def get_options_ratio(option, total):
    return option / total

def get_faculty_rating(get_options_ratio):
    if get_options_ratio >= .9 and get_options_ratio < 1:
        return "Excellent"
    elif get_options_ratio >= .8 and get_options_ratio < .9:
        return "Very Good"
    elif get_options_ratio >= .7 and get_options_ratio < .8:
        return "Good"
    elif get_options_ratio >= .6 and get_options_ratio < .7:
        return "Needs Improvement"
    else: 
        get_options_ratio >= 0 and get_options_ratio < .59
        return "Unacceptable"

    