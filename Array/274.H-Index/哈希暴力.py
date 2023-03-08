class Solution:
    def hIndex(self, citations: list) -> int:
        H, n = 0, len(citations)
        from collections import Counter
        dict = Counter(citations)
        for i in range(1, n + 1):
            count = 0
            for cite, times in dict.items():
                if cite >= i:
                    count += times
                if count >= i and i > H:
                    H = i
            if count == i: return i
        return H

nums = [3,0,6,1,5]
print(Solution().hIndex(nums))