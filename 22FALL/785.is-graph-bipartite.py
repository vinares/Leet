#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        UNVISITED, ONE, TWO = 0, 1, -1
        state = [ UNVISITED for _ in range(n)]
        for i in range(n):
            if state[i] == UNVISITED:
                q = deque([(i, ONE)])
                while q:
                    node, node_state = q.popleft()
                    state[node] = node_state
                    for new_node in graph[node]:
                        if state[new_node] == node_state:
                            return False
                        elif state[new_node] == -1 * node_state:
                            continue
                        q.append((new_node, -1*node_state))
        return True

# @lc code=end

