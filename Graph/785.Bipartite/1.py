class Solution:
    def isBipartite(self, graph: list) -> bool:
        UNCOLORED, RED, GREEN = 0, 1, 2
        n = len(graph)
        color = [UNCOLORED] * n
        Bip = True

        def dfs(node, flag):
            nonlocal Bip
            color[node] = flag
            flag_neighbor = RED if flag == GREEN else GREEN
            for neighbor in graph[node]:
                if color[neighbor] == UNCOLORED:
                    dfs(neighbor,flag_neighbor)
                elif color[neighbor] != flag_neighbor:
                    Bip = False
                    break
                else:
                    continue
        for i in range(n):
            if color[i] == UNCOLORED:
                dfs(i, RED)
                if not Bip:
                    return False
        return Bip



graph = [[1,3],[0,2],[1,3],[0,2]]
print(Solution().isBipartite(graph))

