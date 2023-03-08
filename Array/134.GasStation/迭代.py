class Solution:
    def canCompleteCircuit(self, gas: list, cost: list) -> int:
        n = len(gas)
        for idx, num in enumerate(gas):
            car = num
            car -= cost[idx]
            if car <= 0: continue
            for i in range(idx + 1, idx + n + 1):
                cur = i % n
                car += gas[cur]
                car -= cost[cur]
                if car < 0: break
                if cur == (idx - 1 + n) % n: return idx
        return -1
gas  = [4,5,3,1,4]
cost = [5,4,3,4,2]
print(Solution().canCompleteCircuit(gas, cost))