#!/bin/python3

import math
import os
import random
from re import compile
from re import match
import sys


#
# The function accepts STRING_ARRAY coordinates as parameter.
#
def isValid(coordinates):
    # matches all criteria for valid lat/long pairs except -90<=x<=90 and -180<=y<=180
    # the exception is handled below
    regularExpression = '^\((-|\+)?[1-9][0-9]*(\.[0-9][0-9]*)?, (-|\+)?[1-9][0-9]{0,2}(\.[0-9][0-9]*)?\)'
    pattern = compile(regularExpression)
    result = ['Invalid'] * len(coordinates)
    
    for i,pair in enumerate(coordinates):
        if pattern.match(pair):
            temp = (pair.strip("()")).split(",")
            # Handling for valid integer ranges
            if float(temp[0]) <= 90 and float(temp[0]) >= -90 and float(temp[1]) <= 180 and float(temp[1]) >= -180:
                result[i] = 'Valid'

    
    with open(os.environ['OUTPUT_PATH'], 'w') as fileOut:
        fileOut.write('\n'.join(result))
if __name__ == '__main__':
    coordinates_count = int(input().strip())

    coordinates = []

    for _ in range(coordinates_count):
        coordinates_item = input()
        coordinates.append(coordinates_item)

    isValid(coordinates)
