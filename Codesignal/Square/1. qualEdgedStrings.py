def equalEdgedStrings(words):
    n = len(words)
    ans = [False] * (n - 1)
    for i in range(n-1):
        if words[i][0] == words[i+1][0] and words[i][-1] == words[i+1][-1]:
            ans[i] = True
    return ans
