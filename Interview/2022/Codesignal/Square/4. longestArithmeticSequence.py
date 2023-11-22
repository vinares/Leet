from collections import defaultdict
def longestArithmeticSequence(numbers):
    ans = defaultdict(int)
    n = len(numbers)
    numbers.sort()
    for i in range(1, n):
        for j in range(i):
            diff = numbers[j] - numbers[i]
            ans[(i,diff)] = ans.get((j,diff), 1) + 1
    return max(ans.values())


numbers = [1, 4, 2, 5, 6, 8]
print(longestArithmeticSequence(numbers))