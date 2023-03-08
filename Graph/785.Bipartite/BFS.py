class Solution:
    def isBipartite(self, graph: list) -> bool:
        UNCOLORED, RED, GREEN = 0, 1, 2
        n = len(graph)
        color = [UNCOLORED] * n
        Bip = True

        def BFS(node, flag):
            nonlocal Bip
            color[node] = flag
            flag_neighbor = RED if flag == GREEN else GREEN
            for neighbor in graph[node]:
                if color[neighbor] == UNCOLORED:
                    color[neighbor] = flag_neighbor
                elif color[neighbor] != flag_neighbor:
                    Bip = False
                    return
                else:
                    continue
            for neighbor in graph[node]:
                if neighbor > node:
                    BFS(neighbor, flag_neighbor)
        for i in range(n):
            if color[i] == UNCOLORED and Bip:
                BFS(i, RED)
            if not Bip:
                return False
        return Bip



graph = [[],[2],[1],[],[],[7,8],[7,8,9],[5,6],[5,6],[6],[12,13,14],[12],[10,11],[10],[10],[18],[17,18],[16],[15,16],[],[22,23,24],[22,23,24],[20,21],[20,21],[20,21],[27,28,29],[27,28,29],[25,26],[25,26],[25,26],[32,33,34],[33],[30],[30,31],[30],[37,39],[38],[35],[36],[35],[44],[43,44],[],[41],[40,41],[47,48,49],[47,48,49],[45,46],[45,46],[45,46]]
print(Solution().isBipartite(graph))

