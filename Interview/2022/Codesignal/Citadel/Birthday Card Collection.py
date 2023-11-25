#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'hackerCards' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY collection
#  2. INTEGER d
#

def hackerCards(collection, d):
    i, j = 1, 0
    ans = []
    tmp = set(collection)
    collection = []
    for elem in tmp:
        collection.append(elem)
    collection.sort()

    while i <= d and j < len(collection):
        if i < collection[j]:
            ans.append(i)
            d -= i
            i += 1

        elif i == collection[j]:
            i += 1
            j += 1
        else:
            j += 1
    while i <= d:
        ans.append(i)
        d -= i
        i+= 1

    return ans

collection = [3,1,3,4]
d = 7
print(hackerCards(collection, d))