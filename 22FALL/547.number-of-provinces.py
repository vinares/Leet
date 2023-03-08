#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
from collections import defaultdict, deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        aj = defaultdict(list)
        n = len(isConnected)
        unvisited = set(list(range(n)))
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    aj[i].append(j)
                    aj[j].append(i)
        ccp = 0
        
        for i in range(n):
            if unvisited is None:
                break
            if i in unvisited:
                ccp += 1
                q = deque([i])
                while q:
                    cur = q.popleft()
                    if cur not in unvisited:
                        continue
                    unvisited.remove(cur)
                    for node in aj[cur]:
                        if node in unvisited:
                            q.append(node)
        return ccp
# @lc code=end

