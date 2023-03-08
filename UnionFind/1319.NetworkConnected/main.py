class Solution(object):
    def makeConnected(self, n: int, connections: list):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections) < n - 1:
            return -1
        edges = 0
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

        for con in connections:
            if union(con[0], con[1]):
                edges += 1
        need = len({find(i) for i in uf}) - 1
        return -1 if edges < need else need