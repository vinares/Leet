class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list, k: int, t: int) -> bool:
        check = dict()
        distance = 0

        for i, num in enumerate(nums):
            if num not in check:
                check[num] = i
            else:
                if i - check[num] < t
                check[num] = i
        if not distance or distance != k: return False
        else: return True




nums = [1,0,1,1]
print(Solution().containsNearbyAlmostDuplicate(nums,1,2))