#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#

# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        x = 1
        missing = 0
        i = 0
        while i < len(arr) and k > 0:
            if x == arr[i]:
                i += 1
                x += 1
            else:
                missing = x
                k -= 1
                x += 1
        if k == 0: return missing
        while k > 0:
            if arr and missing < arr[-1]:
                missing = arr[-1] + 1
                k -= 1
            else:
                missing += k
                k = 0
        return missing

# @lc code=end

