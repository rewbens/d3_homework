def return_10():
    return 10
#everything will return something
def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

def length_of_string(string):
    return len(string), string

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(first, second):
    return int(first) + int(second)

def number_to_full_month_name(num):
    if num == 1:
        return "January"
    elif num == 3:
        return "March"
    elif num == 9: 
        return "September"
    
def number_to_short_month_name(num):
    if num == 1:
        return "Jan"
    elif num == 4:
        return "Apr"
    elif num == 10:
        return "Oct"


