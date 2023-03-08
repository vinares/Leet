#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        First, Second, Third = None, None, None
        for num in nums:
            if First is None:
                First = num
            elif num > First:
                First, Second, Third = num, First, Second
            else:
                if Second is None:
                    Second = num
                elif num > Second:
                    Second, Third = num, Second
                else:
                    if Third is None or Third < num:
                        Third = num
        return Third if Third is not None else First

# @lc code=end

