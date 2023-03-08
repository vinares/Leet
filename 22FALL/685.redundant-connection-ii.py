#
# @lc app=leetcode id=685 lang=python3
#
# [685] Redundant Connection II
#

# @lc code=start
class Solution:
    def __init__(self):
        self.parent = list(0 for i in range(1001))

    def find(self, x: int):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        if self.find(x) != self.find(y):
            self.parent[self.find(y)] = self.parent[x]

    def check(self, edges: List[List[int]], remove: List[int]) -> bool:
        self.parent = list(range(1001))
        for e in edges:
            if e[0] == remove[0] and e[1] == remove[1]:
                continue
            if self.find(e[0]) == self.find(e[1]):
                return False
            else:
                self.union(e[0], e[1])
        return True

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        inn, res = list(0 for i in range(1001)), {}
        for e in edges:
            inn[e[1]] += 1
            if inn[e[1]] == 2:
                res = e
        if len(res) > 0:
            if self.check(edges, res):
                return res
            else:
                for e in edges:
                    if e[1] == res[1]:
                        return e
        self.parent = list(range(1001))
        for e in edges:
            if self.find(e[0]) == self.find(e[1]):
                return e
            else:
                self.union(e[0], e[1])
        return res



# @lc code=end

