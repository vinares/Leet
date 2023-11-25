'''
You are given an array of strings a. Your task is to construct an array of strings of the same length,
where the ith element is equal to the first character of a[i], concatenated with the last character of a[i + 1].
If there is no a[i + 1], cycle back to the beginning of the array. In other words, for the final element,
concatenate the first character of a[a.length - 1] with the last character of a[0].
Return the resulting array of 2-character strings.

a = ["cat", "dog", "ferret", "scorpion"]
concatEdgeLetters(a) = ["cg", "dt", "fn", "st"]
'''

def concatEdgeLetters(a):
    n = len(a)
    ans = []
    for i in range(n - 1):
        ans.append(a[i][0] + a[i + 1][-1])
    ans.append(a[-1][0] + a[0][-1])
    return ans

a = ["cat", "dog", "ferret", "scorpion"]
print(concatEdgeLetters(a))