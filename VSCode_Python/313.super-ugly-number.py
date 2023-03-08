#
# @lc app=leetcode id=313 lang=python3
#
# [313] Super Ugly Number
#

# @lc code=start
from heapq import heapify, heappop, heappush
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        q = [1]
        heapify(q)
        while n:
            cur = heappop(q)
            while q and cur == q[0]:
                cur = heappop(q)
            for p in primes:
                heappush(q, p * cur)
            n -= 1
        return cur

# @lc code=end

