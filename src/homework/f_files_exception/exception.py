def add_inventory(dictionary, widget_name, quantity):
    if widget_name not in dictionary:
        dictionary[widget_name] = quantity
        widget_file = open("widgets.txt", "w")
        widget_file.write(str(dictionary))
        widget_file.close()
    else:
        dictionary[widget_name] += quantity
        widget_file = open("widgets.txt", "w")
        widget_file.write(str(dictionary))
        widget_file.close()
    return dictionary
    
def display_items(widget_file):
    widget_file = open("widgets.txt", "r")
    file_contents = widget_file.read()
    return file_contents
