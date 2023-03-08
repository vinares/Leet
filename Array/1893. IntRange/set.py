class Solution:
    def isCovered(self, ranges: list, left: int, right: int) -> bool:
        buckets = set()
        for i in ranges:
            for j in range(i[0], i[1] + 1):
                buckets.add(j)
        for i in range(left, right + 1):
            if i not in buckets:
                return False
        return True

ranges = [[50,50]]
left = 1
right = 50
print(Solution().isCovered(ranges, left, right))