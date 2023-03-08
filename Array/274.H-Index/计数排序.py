class Solution:
    def hIndex(self, citations: list) -> int:
        n = len(citations)
        count = [0] * (n + 1)
        for cite in citations:
            if cite > n:
                cite = n
            count[cite] += 1
        total = 0
        for time in count:
            total += time
        for idx, time in enumerate(count):
            total -= time
            if total <= idx:
                return idx

        return total


nums = [3,0,6,1,5]
print(Solution().hIndex(nums))