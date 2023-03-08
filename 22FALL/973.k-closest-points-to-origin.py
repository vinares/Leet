#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        heapq.heapify(pq)
        for x, y in points:
            dis = x**2+y**2
            if len(pq) >= k:
                if pq[0][0] < -dis:
                    heapq.heappushpop(pq, (-dis, x, y))
            else:
                heapq.heappush(pq,  (-dis, x, y))
        return [[x, y] for _, x, y in pq]

# @lc code=end

