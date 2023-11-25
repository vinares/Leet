from collections import Counter
class Solution:
    def leastInterval(self, tasks: list, n: int) -> int:
        counter = Counter(tasks)
        counter = sorted(counter.items(), key=lambda x:x[1],reverse=False)
        freq = counter[0][1] - 1
        idle = freq * n

        for i in range(1, len(counter)):
            idle -= min(freq, counter[i][1])
        return max(len(tasks), len(tasks) + idle)

tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
print(Solution().leastInterval(tasks,n))