class UF:

    def __init__(self, nums) -> None:    
        self.uf = dict()
        self.size = dict()
        for num in nums:
            self.uf[num] = num
            self.size[num] = 1
    
    def find(self, a):
        if self.uf[a] != a:
            self.uf[a] = self.find(self.uf[a])
        return self.uf[a]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b: return
        self.uf[root_a] = root_b
        self.size[root_b] += self.size[root_a]

    def getMaxConnectSize(self):
        max_size = 0
        for u in self.uf:
            if self.uf[u] == u:
                max_size = max(max_size, self.size[u])
        return max_size