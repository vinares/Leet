#
# @lc app=leetcode id=825 lang=python3
#
# [825] Friends Of Appropriate Ages
#

# @lc code=start
from collections import Counter
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ans = 0
        c = Counter(ages)
        def send(x, y):
            return not (y <= (0.5*x + 7) or y > x or (y > 100 and x < 100))

        for age in c:
            for another_age in c:
                if send(age, another_age):
                    if age != another_age:
                        ans += c[age] * c[another_age]
                    else:
                        ans += c[age] * (c[age]-1)
        return ans

# @lc code=end

