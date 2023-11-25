#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k >= len(points): return points
        def get_tuple(point):
            x, y = point
            return -(x**2+y**2), point

        ans = [get_tuple(point) for point in points[:k]]
        heapq.heapify(ans)
        for i in range(k, len(points)):
            _ = heapq.heappushpop(ans, get_tuple(points[i]))
        return [x for _, x in ans]


# @lc code=end

