def convert_miles_to_km(miles):
    km = miles * 1.6
    return km

def convert_fahrenheit_to_celcius(fah):
    cel = (fah - 32) * (5/9)
    return cel

def convert_gallons_to_liters(gallons):
    liters = gallons * 3.91
    return liters

def convert_pounds_to_kilograms(lbs):
    kg = lbs * .45
    return kg

def convert_inches_to_centimeters(ins):
    cms = ins * 2.54
    return cms

def main():
    print("Please select what operation you want to execute")
    menu_input = input("Miles - Kilometers: \tPress 1\nFahrenheit - Celcius: \tPress 2\nGallons - Liters: \tPress 3\nPounds - Kilograms: \tPress 4\nInches - Centimeters: \tPress 5")

    if menu_input == "1":
        miles1 = int(input("Please enter miles to convert to Kilometers"))
        kilometers = convert_miles_to_km(miles1)
        print(miles1, "mile/s is equal to", kilometers, "Kilometer/s")
        wh_decision = input("Do you want to run this again?")

    elif menu_input == "2":
        fah1 = int(input("Please enter temperature to convert from Fahrenheit to Celcius"))
        celcius1 = convert_fahrenheit_to_celcius(fah1)
        print(fah1, "degress fahreheit is equal to", celcius1, "degress Celcius")

    elif menu_input == "3":
        gallons1 = int(input("Please enter Gallons to convert to Liters"))
        liters1 = convert_gallons_to_liters(gallons1)
        print(gallons1, "Gallon/s is equal to", liters1, "liter/s")
    
    elif menu_input == "4":
        pounds1 = int(input("Please enter Pounds to convert to Kilograms"))
        kilograms1 = convert_pounds_to_kilograms(pounds1)
        print(pounds1, "pound/s is equal to", kilograms1, "Kilogram/s")

    elif menu_input == "5":
        inches1 = int(input("Please enter inches to convert to centimeters"))
        cms1 = convert_inches_to_centimeters(inches1)
        print(inches1, "Inche/s is equal to", cms1, "Centimter/s")

    else:
        print("Invalid Input. Valid inputs are 1, 2, 3, 4 & 5")
        main()

print("Welcome to my conversion program")   
main()