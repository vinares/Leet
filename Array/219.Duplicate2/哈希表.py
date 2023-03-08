class Solution:
    def containsNearbyDuplicate(self, nums: list, k: int) -> bool:
        check = dict()
        distance = 0

        for i, num in enumerate(nums):
            if num not in check:
                check[num] = i
            else:
                distance = max(distance, i - check[num])
                check[num] = i
        if not distance or distance != k: return False
        else: return True




nums = [1,0,1,1]
print(Solution().containsNearbyDuplicate(nums,1))