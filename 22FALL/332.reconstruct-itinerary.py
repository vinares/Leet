#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
from collections import defaultdict
from heapq import heapify, heappop
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        aj = defaultdict(list)
        stack = []
        for depart, arrive in tickets:
            aj[depart].append(arrive)
        for key in aj:
            heapify(aj[key])

        def dfs(cur):
            while aj[cur]:
                dfs(heappop(aj[cur]))
            stack.append(cur)
        dfs('JFK')
        return stack[::-1]
# @lc code=end

