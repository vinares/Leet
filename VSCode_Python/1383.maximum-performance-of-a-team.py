#
# @lc app=leetcode id=1383 lang=python3
#
# [1383] Maximum Performance of a Team
#

# @lc code=start
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        cur_sum, ans = 0, 0
        speed_heap = []
        for i, j in sorted(zip(efficiency, speed), reverse=True):
            while len(speed_heap) > k-1:
                cur_sum -= heappop(speed_heap)
            heappush(speed_heap, j)
            cur_sum += j
            ans = max(ans, cur_sum * i)
        return ans % (10 ** 9 + 7)

# @lc code=end

