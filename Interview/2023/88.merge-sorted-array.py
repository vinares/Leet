#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m-1, -1, -1):
            nums1[i+n] = nums1[i]
        i, j = n, 0
        head = 0
        while i < m+n or j < n:
            if j == n or (i < m+n and nums1[i] < nums2[j]):
                nums1[head] = nums1[i]
                i += 1
            else:
                nums1[head] = nums2[j]
                j += 1
            head += 1
        return 
# @lc code=end

