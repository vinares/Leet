import collections
import math


# Add any extra import statements you may need here


# Add any helper functions you may need here


def minOperations(arr):
    goal = ''.join(str(i + 1) for i in range(len(arr)))
    start = ''.join(str(arr[i]) for i in range(len(arr)))
    q = collections.deque([start])
    level = 0
    visited = set([start])

    while q:
        for _ in range(len(q)):
            cur_permutation =  q.popleft()

            if cur_permutation == goal:
                return level
            for i in range(len(cur_permutation)):
                for j in range(i, len(cur_permutation)):
                    tmp = [c for c in cur_permutation]
                    tmp[i:j+1] = tmp[i:j+1][::-1]
                    cur = ''.join(tmp)
                    if cur not in visited:
                        visited.add(cur)
                        q.append(cur)

        level += 1

    return -1

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
    n_1 = 5
    arr_1 = [1, 2, 5, 4, 3]
    expected_1 = 1
    output_1 = minOperations(arr_1)
    check(expected_1, output_1)

    n_2 = 3
    arr_2 = [3, 1, 2]
    expected_2 = 2
    output_2 = minOperations(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
    n_2 = 8
    arr_2 = [1,1,1,1,1,1,1,1]
    expected_2 = -1
    output_2 = minOperations(arr_2)
    check(expected_2, output_2)