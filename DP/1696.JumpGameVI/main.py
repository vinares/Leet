from heapq import *
class Solution:
    def maxResult(self, nums, k: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        ans = nums[0]
        past = [(-nums[0],0)]
        heapify(past)
        for i in range(1, n):
            best = heappop(past)
            while best[1] < i - k:
                best = heappop(past)
            ans = nums[i] - best[0]
            heappush(past, best)
            heappush(past, (-ans, i))
        return ans

nums = [1,-1,-2,4,-7,3]
k = 2

print(Solution().maxResult(nums, k))

