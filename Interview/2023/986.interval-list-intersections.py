#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#

# @lc code=start
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        s, e = 0, 1
        ans = []
        while i < len(firstList) and j<len(secondList):
            a = firstList[i]
            b = secondList[j]
            # a
            # b
            # not (a[start] > b[end] or a[end] < b[start])
            # a[start] <= b[end] and a[end] >= b[start]
            if a[s] <= b[e] and a[e] >= b[s]:
                ans.append([max(a[s], b[s]), min(a[e], b[e])])
            if a[e] <= b[e]:
                i += 1
            else:
                j += 1
        return ans
# @lc code=end

