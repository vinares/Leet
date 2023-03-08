#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = sorted([nums1, nums2], key=len)
        m, n = len(a), len(b)
        midpoint = (m + n - 1) // 2
        i = bisect_left(range(m), True, key= lambda i: midpoint - i - 1 < 0 or a[i] >= b[midpoint -i - 1])
        newnums = sorted(a[i:i+2] + b[midpoint-i:midpoint-i+2])
        return (newnums[0] +newnums[1 - (m+n)%2])/2
# @lc code=end

