#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    coords = [[0,0], [1, 0], [2, 0], [1, 1], [0, 2], [1, 2], [2, 2]]

    curMax = 0
    for i in range(4):
        for j in range(4):
            coords_trans = [[coords[x][1]+i, coords[x][0]+j] for x in range(len(coords))]
            curSum = 0
            for x in range(len(coords_trans)):
                curSum += arr[coords_trans[x][0]][coords_trans[x][1]]
            
            if curSum > curMax:
                curMax = curSum
    
    return curMax


    

if __name__ == '__main__':
    fptr = open('out.txt', 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
