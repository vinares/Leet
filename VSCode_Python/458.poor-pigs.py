#
# @lc app=leetcode id=458 lang=python3
#
# [458] Poor Pigs
#

# @lc code=start
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        n = minutesToTest//minutesToDie + 1
        ans = 0
        while (n) ** ans  < buckets:
            ans += 1
        return ans
            

# @lc code=end

