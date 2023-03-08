class Solution:
    def twoCitySchedCost(self, costs: list) -> int:
        ans = 0
        costs = sorted(costs, key=lambda x: abs(x[0] - x[1]), reverse=True)
        l = r = len(costs) //2
        i = 0
        while i < len(costs) and l > 0 and r > 0:
            if costs[i][0] >= costs[i][1]:
                r -= 1
                ans += costs[i][1]
                i += 1
            else:
                l -= 1
                ans += costs[i][0]
                i += 1
        if l > 0:
            for j in range(i, len(costs)):
                ans += costs[j][0]
        else:
            for j in range(i ,len(costs)):
                ans += costs[j][1]
        return ans




costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
print(Solution().twoCitySchedCost(costs))