class Solution:
    def canCompleteCircuit(self, gas: list, cost: list) -> int:
        n = len(gas)
        for i in range(n):
            gas[i] -= cost[i]
        print(gas)
        if not n: return -1
        if n == 1 and gas[0] >= 0: return 0

        start = 0
        while start < n:
            count, p = 0, 0
            for i in range(start, start + n):
                cur = i % n
                count += gas[cur]
                if cur == (start - 1 + n) % n and count >= 0: return start
                if count <= 0: break
            start = i + 1
        return -1


gas  = [1,2,3,4,3,2,4,1,5,3,2,4]
cost = [1,1,1,3,2,4,3,6,7,4,3,1]
print(Solution().canCompleteCircuit(gas, cost))