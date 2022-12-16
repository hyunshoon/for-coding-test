#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
import copy
#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    # Write your code here
    kinds = []    
    answer = 0
    for sample in s:
        if sample not in kinds:
            kinds.append(sample)
    if len(kinds)<2:
        return 0
    delete_li = list(combinations(kinds, len(kinds) - 2))
    for delete in delete_li:
        temp = copy.deepcopy(s)
        for d in delete:
            temp = temp.replace(d, '')
        is_pass = True
        for i in range(len(temp)-1):
            if temp[i] == temp[i+1]: #not alternative false
                is_pass = False
                break
        if is_pass:
            answer = max(answer, len(temp))                
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
