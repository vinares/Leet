class Solution:
    def hIndex(self, citations: list) -> int:
        H, n = 0, len(citations)
        for i in range(n - 1, -1, -1):
            if citations[i] >= n - i:
                H += 1
            else:
                return H
        return H

nums = [0,1,3,5,6]
print(Solution().hIndex(nums))