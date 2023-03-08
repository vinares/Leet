#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
from random import randint
class Solution:
    def partition(self, left, right):
        pivot_idx = randint(left, right)
        pivot = self.nums[pivot_idx]
        self.nums[left],  self.nums[pivot_idx] = pivot, self.nums[left]
        while left < right:
            while left < right and self.nums[right] <= pivot:
                right -= 1
            self.nums[left] = self.nums[right]
            while left < right and self.nums[left] >= pivot:
                left += 1
            self.nums[right] = self.nums[left]
        self.nums[left] = pivot
        return left
    

    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.nums = nums
        n = len(nums)
        
        l, r = 0, n-1
        while True:
            index = self.partition(l, r)
            if index == k-1:
                return nums[index]
            elif index < k-1:
                l = index +1
            else:
                r = index -1
        return nums[l]
        
# @lc code=end

