#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#

# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = list(range(n+1))

        def find(node):
            if uf[node] != node:
                uf[node] = find(uf[node])
            return uf[node]

        def union(u, v):
            uf[find(u)] = find(v)
        
        for edge in edges:
            u, v = edge
            if find(u) != find(v):
                union(u, v)
            else:
                return edge
# @lc code=end

