#
# @lc app=leetcode id=1444 lang=python3
#
# [1444] Number of Ways of Cutting a Pizza
#

# @lc code=start
from functools import lru_cache
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        prex_sum = [[0] * n for _ in range(m)]
        prex_sum[m-1][n-1] = int(pizza[m-1][n-1] == 'A')
        for i in range(m-2, -1, -1):
            prex_sum[i][n-1] = prex_sum[i+1][n-1] + int(pizza[i][n-1]=='A')
        for j in range(n-2, -1, -1):
            prex_sum[m-1][j] = prex_sum[m-1][j+1] + int(pizza[m-1][j] == 'A')
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                prex_sum[i][j] = prex_sum[i+1][j] + prex_sum[i][j+1] - prex_sum[i+1][j+1] + int(pizza[i][j] == 'A')
        mod = 10 ** 9 + 7

        @lru_cache(None)
        def dfs(i, j, k):
            if k == 1:
                return 1
            ans = 0
            for x in range(i+1, m):
                if (prex_sum[i][j] > prex_sum[x][j] and prex_sum[x][j] >= k-1):
                    ans += dfs(x, j, k-1)
            for y in range(j+1, n):
                if ( prex_sum[i][j] > prex_sum[i][y] and prex_sum[i][y] >= k-1):
                    ans += dfs(i, y, k-1)
            if ans > mod:
                ans %= mod
            return ans

        return dfs(0, 0, k)



# @lc code=end

