import time
tic = time.time()
class Solution:
    def findMinDifference(self, timePoints: list) -> int:
        ans, n = 720, len(timePoints)
        time = []
        for x in timePoints:
            time.append(self.minute(x))
        time.sort()
        while ans:
            for i in range(len(time) - 1):
                ans = min(ans, time[i + 1] - time[i])
            break
        ans = min(ans, 1440 - time[-1] + time[0])
        return ans

    def minute(self, point: str):
        h, m = int(point[0:2]), int(point[3:5])
        return h * 60 + m

timePoints = ["23:59","00:00"]
print(Solution().findMinDifference(timePoints))

toc = time.time()
print(toc - tic)