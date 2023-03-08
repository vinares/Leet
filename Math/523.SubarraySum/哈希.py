class Solution:
    def checkSubarraySum(self, nums: list, k: int) -> bool:
        n = len(nums)
        hashmap = dict()
        cur = 0
        hashmap[0] = -1
        for i, num in enumerate(nums):
            cur += num
            if k != 0:
                if i and cur:
                    if (cur % k in hashmap and hashmap[cur % k] != i - 1) or not cur % k:
                        return True
                if cur % k not in hashmap:
                    hashmap[cur % k] = i
            else:
                if not num and i:
                    if not nums[i - 1]:
                        return True
        return False
case =  Solution()
nums = [0,0]
print(case.checkSubarraySum(nums, 0))