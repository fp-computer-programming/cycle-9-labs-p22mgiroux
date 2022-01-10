# Author: MOG 1/10/22

from typing import List


def double_stuff(lst):
    for i, val in enumerate(lst):
            lst[i] *= 2
    return lst

list1 = [1,2,3,4,2.5,5.5,"a","v"]
print(double_stuff(list1))

list2 = [10,2,3,6]
print(double_stuff(list2))

list3 = [3.3,31,6.9]
print(double_stuff(list3))
