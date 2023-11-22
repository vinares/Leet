import math


# Add any extra import statements you may need here


# Add any helper functions you may need here

from collections import defaultdict
def numberOfWays(arr, k):
    numhash = dict()
    count = 0
    for i in range(len(arr)):
        if arr[i] not in numhash.keys():
            numhash[arr[i]] = set()
            numhash[arr[i]].add(i)
        else:
            numhash[arr[i]].add(i)

    for num in arr:
        if k - num > 0 and k - num in numhash.keys():
            x = numhash[k - num].pop()
            numhash[k - num].add(x)
            if num != arr[x]:
                count += len(numhash[k - num])
            else:
                count += (len(numhash[k - num]) - 1)
    return count // 2



# Write your code here


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
    print('[', n, ']', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printInteger(expected)
        print(' Your output: ', end='')
        printInteger(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    k_1 = 6
    arr_1 = [1, 2, 3, 4, 3]
    expected_1 = 2
    output_1 = numberOfWays(arr_1, k_1)
    check(expected_1, output_1)

    k_2 = 6
    arr_2 = [1, 5, 3, 3, 3]
    expected_2 = 4
    output_2 = numberOfWays(arr_2, k_2)
    check(expected_2, output_2)

    # Add your own test cases here
