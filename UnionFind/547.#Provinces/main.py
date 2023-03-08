class Solution:
    def findCircleNum(self, isConnected: list) -> int:
        n = len(isConnected)
        uf = {i: i for i in range(n)}

        def find(a):
            if a != uf[a]:
                uf[a] = find(uf[a])
            return uf[a]

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return True
            uf[ra] = rb
            return False

        for i in range( n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    union(i, j)
        return len({find(x) for x in uf})

nums = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
print(Solution().findCircleNum(nums))