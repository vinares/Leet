#
# @lc app=leetcode id=1944 lang=python3
#
# [1944] Number of Visible People in a Queue
#

# @lc code=start
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0 for _ in range(n)]
        ms = []
        for i in range(n-1, -1, -1):
            while ms and ms[-1] < heights[i]:
                ms.pop()
                ans[i] += 1
            ans[i] += len(ms)>0
            ms.append(heights[i])
        return ans

# @lc code=end

