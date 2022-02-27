def test_config():
    return True

def multiplication_table_for(row, col):
    for i in range(1, col):
        for j in range(1, col):
            print(str(i*j).rjust(3, " "), end= " ")

def multiplication_table_while(row, col):
    i = 0
    while i < row:
        j = 0
        while j< col:
            product = (i+1)*(j+1)
            print(str(product).rjust(3, " "), end= " ")
            j += 1
        i += 1
        print(' ')

def display_menu():
    print("1-Option 1")
    print("2-Option 2")
    print("3- Exit")

def run_menu():
    option = -1
    while option != 3:
        display_menu()
        option = int(input("Select Menu Option"))
        option = handle_option(option)

def handle_option(option):

    if option == 1:
        print("Selected 1")
    elif option == 2:
        print("Selected 2")
    else:
        choice = input("Are you sure enter y or n")
        if (choice == 'n'):
            option = -1
        print(option)

        print("Exit")