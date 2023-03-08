class Solution:
    def numRollsToTarget(self, n: int, f: int, target: int) -> int:
        mem = {}
        def dp(n, target):
            if n == 0:
                return 0 if target > 0 else 1
            if (n, target) in mem:
                return mem[(n, target)]
            total = 0
            for k in range(max(0, target - f), target):
                total += dp(n - 1, k)
            mem[(n, target)] = total
            return total

        return dp(n, target) % (10 ** 9 + 7)





print(Solution().numRollsToTarget(30,30,500))