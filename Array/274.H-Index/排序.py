class Solution:
    def hIndex(self, citations: list) -> int:
        H, n = 0, len(citations)
        citations.sort()
        for i in range(n - 1, -1, -1):
            if citations[i] >= n - i:
                H += 1
            else:
                return H

nums = [3,0,6,1,5]
print(Solution().hIndex(nums))