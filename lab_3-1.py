# Author: MOG 1/11/22

def add_foods(lst):
    sixth_letter = []
    short_foods = []
    not_foods = []

    for i in lst:
        try:
            sixth_letter.append(i[5])
        except IndexError:
            short_foods.append(i)
        except TypeError:
            not_foods.append(i)
        
    print("Sixth Letters: {}. \nShort Foods: {}. \nNot Foods: {}.".format(sixth_letter,short_foods,not_foods))

add_foods(["banana","apples","grape",True,"pear",7])
