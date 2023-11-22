#
# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#

# @lc code=start
import random
from bisect import bisect_left
class Solution:
    def __init__(self, w: List[int]):
        self.acc = []
        if len(w) > 0: self.acc.append(w[0])
        for i in range(1, len(w)):
            self.acc.append(self.acc[-1] + w[i])

    def pickIndex(self) -> int:
        r = random.randint(1, self.acc[-1])
        i = bisect_left(self.acc, r)
        return i

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

