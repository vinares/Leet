#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degrees = defaultdict(int)
        graphs = defaultdict(list)
        for v, u in prerequisites:
            degrees[v] += 1
            graphs[u].append(v)
        new_frontier = []
        for i in range(numCourses):
            if i not in degrees:
                degrees[i] = 0
                new_frontier.append(i)
        ans = []
        while degrees:
            frontier = new_frontier
            new_frontier = []
            for node in frontier:
                ans.append(node)
                degrees.pop(node)
                edges = graphs[node]
                graphs.pop(node)
                for v in edges:
                    degrees[v] -= 1
                    if degrees[v] == 0:
                        new_frontier.append(v)
            if degrees and not new_frontier: return []
        return ans
                    
            
# @lc code=end

