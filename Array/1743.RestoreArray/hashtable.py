from collections import defaultdict
class Solution:
    def restoreArray(self, adjacentPairs: list) -> list:
        hashtable = defaultdict(list)
        for adjacent in adjacentPairs:
            hashtable[adjacent[0]].append(adjacent[1])
            hashtable[adjacent[1]].append(adjacent[0])
        start = None
        for node, adjacent in hashtable.items():
            if len(adjacent) == 1:
                start = node
                break

        cur = hashtable[start][0]
        res = [start, cur]
        pre = start
        while 1:
            if hashtable[cur][0] == pre:
                res.append(hashtable[cur][1])
                pre = cur
                cur = hashtable[cur][1]
            else:
                res.append(hashtable[cur][0])
                pre = cur
                cur = hashtable[cur][0]

            if len(hashtable[cur]) == 1:
                break
        return res



adjacentPairs = [[4,-2],[1,4],[-3,1]]
print(Solution().restoreArray(adjacentPairs))