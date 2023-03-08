#
# @lc app=leetcode id=398 lang=python3
#
# [398] Random Pick Index
#

# @lc code=start
from collections import defaultdict
from random import choice
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = defaultdict(list)
        for i, num in enumerate(nums):
            self.nums[num].append(i)

    def pick(self, target: int) -> int:
        return choice(self.nums[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @lc code=end

