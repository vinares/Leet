#
# @lc app=leetcode id=939 lang=python3
#
# [939] Minimum Area Rectangle
#

# @lc code=start
from collections import defaultdict

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        rows = defaultdict(set)
        for x, y in points:
            rows[x].add(y)
        ans = float('inf')
        def min_ans(row1, row2, common_cols, ans):
            if len(common_cols) < 2:
                return ans
            h = abs(row1-row2)
            common_cols.sort()
            w = common_cols[1] - common_cols[0]
            for i in range(len(common_cols)-1):
                w = min(w, common_cols[i+1]-common_cols[i])
            return min(ans, w*h)



        for row in rows:
            for another in rows:
                if row != another:
                    common_cols = []
                    for col in rows[row]:
                        if col in rows[another]:
                            common_cols.append(col)
                    ans = min_ans(row, another, common_cols, ans)
        return 0 if ans == float('inf') else ans

# @lc code=end

