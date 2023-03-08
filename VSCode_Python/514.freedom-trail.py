#
# @lc app=leetcode id=514 lang=python3
#
# [514] Freedom Trail
#

# @lc code=start
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        m, n = len(ring), len(key)
        alphabet = [[] for _ in range(26)]
        for i, c in enumerate(ring):
            alphabet[ord(c)-ord('a')].append(i)
        dp = [[10 ** 9]*m for _ in range(n)]
        for position in alphabet[ord(key[0])-ord('a')]:
            dp[0][position] = min(position, m-position) + 1
        for i in range(1, n):
            for j in alphabet[ord(key[i])-ord('a')]:
                for k in alphabet[ord(key[i-1])-ord('a')]:
                    dp[i][j] = min(dp[i][j], dp[i-1][k]+min(abs(k-j), m-abs(k-j))+1)
        return min([dp[n-1][x] for x in range(m)])


# @lc code=end

