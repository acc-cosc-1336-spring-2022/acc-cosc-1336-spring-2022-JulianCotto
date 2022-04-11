grade_list = []
total = 0
decision1 = "y"
while decision1 == "y" or decision1 == "Y":
    st_grade = int(input("Please enter student grade"))
    grade_list.append(st_grade)
    if st_grade >= 90 and st_grade <= 100:
        print("Student number", len(grade_list), ":", "You got an A!! Why dont you teach the next class!!")
    elif st_grade >= 80 and st_grade < 90:
        print("Student number", len(grade_list), ":", "You got an B!! There is a Little More Practice Required!!")
    elif st_grade >= 70 and st_grade < 80:
        print("Student number", len(grade_list), ":", "You got an C!! Practice your fundamentals more!!")
    elif st_grade >= 60 and st_grade < 70:
        print("Student number", len(grade_list), ":", "You got an D!! Are you even trying?!")
    elif st_grade < 60 and st_grade >= 0:
        print("Student number", len(grade_list), ":", "You got an F!! This is an expensive class to retake!!")
    else: 
        print("Invalid Input")
    decision1 = input("Do you want to check another grade? y/n")
for value in grade_list:
    total += int(value)
    average = total / len(grade_list)
print("The number of grades you entered is:", len(grade_list))
print("The average grade of the class is:", average)








    

