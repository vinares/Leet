class Solution:
    def isCovered(self, ranges: list, left: int, right: int) -> bool:
        buckets = []
        for erange in ranges:

            while erange[1] > len(buckets):
                buckets.append(False)
            for x in range(erange[0] - 1, erange[1]):
                buckets[x] = True
        if len(buckets) < right:
            return False
        for y in range(left - 1, right):
            if buckets[y] == False:
                return False
        return True

ranges = [[50,50]]
left = 1
right = 50
print(Solution().isCovered(ranges, left, right))