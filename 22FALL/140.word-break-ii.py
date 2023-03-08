#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [[] for _ in range(len(s)+1)]
        dp[0].append('')
        sofar = [0]
        sight = max(len(x) for x in wordDict)
        for i in range(1, len(s)+1):
            for j in sofar:
                if i - j > sight:
                    continue
                if s[j:i] in wordDict:
                    for an_str in dp[j]:
                        dp[i].append(an_str + ' ' + s[j:i])
                    sofar.append(i)
        
        ans = set([x[1:] for x in dp[-1]])  
        return list(ans)


# @lc code=end

