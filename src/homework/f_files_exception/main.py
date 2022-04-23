import exception

main_decision = "y"
decision = "y"
widgets = {}

try:
    main_decision = input("1-Add or Update Item:\tPress 1\n2-Display Item\t\tPress 2\n3-Exit:\t\t\tPress 3")
    while main_decision == "1":
        try:
            widget_name = input("Please enter the name of the widget you want to add or update")
            quantity = int(input("Please enter the quantity being added"))
            print(quantity, "x", widget_name, "will be added and if it already exists", widget_name,"will be incremented by x", quantity)
            widgets = exception.add_inventory(widgets, widget_name, quantity)
            print(widgets)
            decision = input("Do you have another widget to add?")
            while decision.lower() == "y":
                widget_name = input("Please enter the name of the widget you want to add or update")
                print(widget_name, "will be added and if it already exists", widget_name,"will be incremented")
                quantity = int(input("Please enter the quantity being added"))
                print(quantity, "x", widget_name, "will be added and if it already exists", widget_name,"will be incremented by x", quantity)
                widgets = exception.add_inventory(widgets, widget_name, quantity)
                print(widgets)
                decision = input("Do you have another widget to add?")
            main_decision = input("1-Add or Update Item:\tPress 1\n2-Delete Item\t\tPress 2\n3-Exit:\t\t\tPress 3")
        except ValueError:
            print("Try Again")

    while main_decision == "2":
        try:
            widget_file = input("Preparing Widget File Contents")
            exception.display_items(widget_file)
            print(widgets)
            main_decision = input("1-Add or Update Item:\tPress 1\n2-Delete Item\t\tPress 2\n3-Exit:\t\t\tPress 3")
        except ValueError:
            print("Try Again")

    while main_decision ==  "3":
        print("Thank you for running the program!")
        quit()

except ValueError:
    print("Invalid selection. 1, 2, or 3")
    main_decision = input("1-Add or Update Item:\tPress 1\n2-Delete Item\t\tPress 2\n3-Exit:\t\t\tPress 3")
    
