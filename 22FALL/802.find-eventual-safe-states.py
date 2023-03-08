#
# @lc app=leetcode id=802 lang=python3
#
# [802] Find Eventual Safe States
#

# @lc code=start
from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        graph_rev = [[] for _ in graph]
        for x, ys in enumerate(graph):
            for y in ys:
                graph_rev[y].append(x)
        in_degree = [len(x) for x in graph]
        
        q = deque([i for i, d in enumerate(in_degree) if d == 0])

        while q:
            for node in graph_rev[q.popleft()]:
                in_degree[node] -= 1
                if in_degree[node] == 0:
                    q.append(node)
        return [i for i, d in enumerate(in_degree) if d == 0]


# @lc code=end

