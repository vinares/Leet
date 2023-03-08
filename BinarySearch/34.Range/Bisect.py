class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        import bisect
        if not nums: return [-1, -1]
        if target not in set(nums): return [-1, -1]
        r = bisect.bisect_right(nums,target) - 1
        l = bisect.bisect_left(nums,target)
        return [l,r]
case = Solution()
import time
t = time.time()
print(case.searchRange([1,2,45], 3))
print(time.time()-t)