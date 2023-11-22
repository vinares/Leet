import collections


class Solution:
    def criticalConnections(self, n: int, connections:list) -> list:
        visited = [False for _ in range(n)]
        rank = [-1 for _ in range(n)]
        whenVisited = [-1 for _ in range(n)]
        table = collections.defaultdict(list)
        parent = [-1 for _ in range(n)]
        ans = []

        for inv,outv in connections:
            table[inv].append(outv)
            table[outv].append(inv)

        def backtrack(table, timestamp, rank, visited, whenVisited, index, ans, parent ):
            timestamp += 1
            visited[index] = True
            rank[index] = whenVisited[index] = timestamp

            for outv in table[index]:
                if parent[index] == outv:continue
                elif visited[outv]:
                    rank[index] = min(whenVisited[index], rank[outv])
                else:
                    parent[outv] = index
                    backtrack(table,timestamp,rank,visited,whenVisited,outv, ans, parent)
                    rank[index] = min(rank[index], rank[outv])
                if rank[outv] > whenVisited[index]:
                    ans.append([index, outv])

        backtrack(table,0,rank, visited,whenVisited,0,ans,parent)
        return ans





n = 4
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
print(Solution().criticalConnections(n, connections))