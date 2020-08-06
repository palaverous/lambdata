"""
Summation
"""

import pandas as pd

def summation():
    '''
    Calculates the sum of two user defined numbers
    Displays the variables entered as well as sum
    '''
    var1 = input('Enter First Number To Add: ')
    var2 = input('Enter Second Number To Add: ')
    sum = float(var1) + float(var2)
    print('The sum of {0} and {1} is {2}'. format(var1, var2, sum))def
