class Solution:
    def lexi_order_n(self, n):
        self.ans = []

        def dfs(x):
            if x > n:
                return
            self.ans.append(x)
            for i in range(0, 10):
                dfs(x*10+i)
            return
        for i in range(1, 10):
            dfs(i)
        return self.ans
            
print(Solution().lexi_order_n(16))