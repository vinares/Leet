#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
from heapq import heapify, heappush, heappushpop, heappop
class MedianFinder:
    def __init__(self):
        self.up, self.down = [], [] 
        heapify(self.up)
        heapify(self.down)

    def addNum(self, num: int) -> None:
        if len(self.up) == len(self.down):
            heappush(self.up, num)
        else:
            heappush(self.down, -num)
        while self.down and self.up[0] < -self.down[0]:
            small = heappop(self.up)
            big = heappushpop(self.down, -small)
            heappush(self.up, -big)

    def findMedian(self) -> float:
        if len(self.up) == len(self.down):
            return (self.up[0] - self.down[0])/2
        else:
            return self.up[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

