#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), math.ceil(len(weights)/days) * max(weights)
        
        def not_enough(size):
            cur = 0
            cnt = 1
            for w in weights:
                cur += w
                if cur > size:
                    cur = w
                    cnt += 1
                    if cnt > days:
                        return True
            return False
        while l < r:
            m = l + (r-l) //2
            print(m)
            if not_enough(m):
                l = m+1
            else:
                r = m
        return l



# @lc code=end

