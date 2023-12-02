#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        def find_first(first=True):
            left, right = 0, n-1
            ans = -1
            while left <= right:
                m = left+(right-left)//2
                if nums[m] == target:
                    ans = m
                    if first:
                        right = m-1
                    else:
                        left = m+1
                elif nums[m] > target:
                    right = m-1
                else:
                    left = m+1
            return ans

        first = find_first()
        last = find_first(first=False)
        return [first, last]
# @lc code=end

