#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#

# @lc code=start
import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points, height_pq, ans = [], [0], []
        for l, r, h in buildings:
            points.append((l, h))
            points.append((r, -h))
        points.sort(key=lambda x: (x[0], -x[1]))
        for x, y in points:
            if y > 0:
                if y > -height_pq[0]:
                    ans.append([x, y])
                heapq.heappush(height_pq, -y)
            else:
                height_pq.remove(y)
                heapq.heapify(height_pq)
                if -height_pq[0] < -y:
                    ans.append([x, -height_pq[0]])
        return ans

# @lc code=end

