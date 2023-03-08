#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

# @lc code=start
from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = [set() for _ in range(n)]
        for u,v in edges: tree[u].add(v), tree[v].add(u)
        q, nq = [i for i in range(n) if len(tree[i])<2], []
        while True:
            for u in q:
                for v in tree[u]:
                    tree[v].remove(u)
                    if len(tree[v]) == 1:
                        nq.append(v)
            if not nq:
                break
            q, nq = nq, []
        return q

# @lc code=end

