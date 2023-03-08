class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        n = len(s)
        dp = [-1]

        for i in range(n):
            for j in range(len(dp) - 1, -1, -1):
                if s[dp[j] + 1:i + 1] in wordDict:
                    dp.append(i)
                    break
        return dp[-1] == n - 1

print(Solution().wordBreak(s = "aaaaaaa", wordDict=["aaaa","aaa"]))