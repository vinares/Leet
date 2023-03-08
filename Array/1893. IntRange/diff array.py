class Solution:
    def isCovered(self, ranges: list, left: int, right: int) -> bool:
        diff = [0] * 52
        for l, r in ranges:
            diff[l] += 1
            diff[r + 1] -= 1
        score = 0
        print(diff)
        for i in range(52):
            score += diff[i]
            if left <= i  <= right and score <= 0:
                return False
            if i > right:
                break
        return True


ranges = [[1,10],[10,20]]
left = 21
right = 21
print(Solution().isCovered(ranges, left, right))