#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ht = set(nums[0:k]) if k <= len(nums) else set(nums)
        i = k
        while i < len(nums):
            if len(ht) < k:
                return True
            ht.add(nums[i])
            ht.remove(nums[i-k])
            i += 1
        return len(ht) < min(len(nums), k)
# @lc code=end

