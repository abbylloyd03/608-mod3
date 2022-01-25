#Abby Lloyd, built-in-min-max.py

def max_min(list):
    """Print maximum and minimum values from a list"""
    max_value = -1000000
    min_value = 1000000
    for number in list:
        if number > max_value:
            max_value = number
        if number < min_value:
            min_value = number
    return print(list, "Maximum:", max_value, "Minimum:", min_value)

list1 = [12, 27, 36]
list2 = [12.3, 45.6, 9.7]
         
max_min(list1)
max_min(list2)
