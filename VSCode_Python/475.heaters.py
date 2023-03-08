#
# @lc app=leetcode id=475 lang=python3
#
# [475] Heaters
#

# @lc code=start
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        m, n = len(houses), len(heaters)
        houses.sort()
        heaters.sort()
        i, j = 0, 0
        max_radius = 0
        while i < m and j < n:
            first = heaters[j]
            second = heaters[j+1] if j+1<n else None
            if second and houses[i] > second:
                j += 1
                continue
            radius = 10 ** 9
            if houses[i] < first:
                radius = min(radius, first - houses[i])
            else:
                radius = min(radius, houses[i]-first)
                if second:
                    radius = min(radius, second-houses[i])
            max_radius = max(radius, max_radius)
            i += 1
        return max_radius

# @lc code=end

