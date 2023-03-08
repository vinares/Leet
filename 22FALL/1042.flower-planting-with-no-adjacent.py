#
# @lc app=leetcode id=1042 lang=python3
#
# [1042] Flower Planting With No Adjacent
#

# @lc code=start
from collections import defaultdict
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
    
        graph = defaultdict(list)
        for u, v in paths:
            graph[u].append(v)
            graph[v].append(u)
        color = [0 for i in range(n)]
        for u in range(1, n+1):
            choices = set(range(1,5)) - set(color[v-1] for v in graph[u])
            color[u-1] = choices.pop()
        return color
        


# @lc code=end

