
class Solution:
    def wordBreak(self, s: str, wordDict: list) -> list:
        if s == '':
            return '' in wordDict
        n = len(s)
        dp = [[[] * n for _ in range(n)]] * n

        for i in range(n):
            if s[0:i+1] in wordDict:
                dp[0][i].append(''.join(s[0:i+1]))
        for j in range(1, n):
            for i in range(0, j+1):
                for k in range(0, i):
                    if dp[k][i-1] != [] and s[i:j+1] in wordDict:
                        for x in dp[k][i-1]:
                            dp[i][j].append(''.join(x + ' ' + s[i:j+1]))

        ans = set()
        for i in range(n):
            if dp[i][n-1]:
                for x in dp[i][n-1]:
                    ans.add(x)
        return  list(ans)


s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
print(Solution().wordBreak(s, wordDict))