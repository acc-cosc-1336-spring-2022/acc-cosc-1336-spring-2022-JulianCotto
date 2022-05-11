import decisions


def main():
    run_again = "y"
    while run_again.lower() == "y":
        total = input("Please enter the amount of points available on your assignment")
        options = input("Please enter how many points you earned on your assignment")
        if int(options) < 0 or int(options) > int(total):
            print("Invalid Entry. You cannot have a grade less than 0 or more than the total available points")
            main()
        print("Now calculating your grade")
        grade = decisions.get_options_ratio(int(options), int(total))
        fac_grade = decisions.get_faculty_rating(grade)
        if grade >= .6 and grade < .7:
            print("You got a grade of", grade*100, "% which", fac_grade)
            run_again = input("Would you like to enter more grades? Y or N")
        else:
            print("You got a grade of", grade*100, "% which is", fac_grade)
            run_again = input("Would you like to enter more grades? Y or N")
    else:
        print("Thank you for running this grading program")
        quit()

main()






    

