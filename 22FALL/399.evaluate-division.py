#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        aj = defaultdict(list)
        n = len(equations)
        for i in range(n):
            top, bottom, val = equations[i][0], equations[i][1], values[i]
            aj[top].append((bottom, val))
            if top != 0:
                aj[bottom].append((top, 1/val))
        ans = []
        for top, bottom in queries:
            print(top, bottom)
            if (top not in aj) or (bottom not in aj):
                ans.append(-1.)
                continue

            if top == bottom:
                ans.append(1.)
                continue

            q, visited = deque([(top, 1)]), set()
            visited.add(top)
            quotient = -1
            while q:
                cur, quo = q.popleft()
                for node, weight in aj[cur]:
                    if node in visited:
                        continue
                    if node == bottom:
                        quotient = quo * weight
                        break
                    visited.add(node)
                    q.append((node, quo * weight))
                if quotient != -1:
                    break

            quotient = round(quotient, 5)
            ans.append(quotient)
        return ans

# @lc code=end

