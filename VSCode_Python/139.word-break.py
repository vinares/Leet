#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        sofar = [0]
        for i in range(1, len(s) + 1):
            for j in sofar[::-1]:
                dp[i] = s[j:i] in wordDict
                if dp[i]:
                    sofar.append(i)
                    break
        return dp[-1]
# @lc code=end