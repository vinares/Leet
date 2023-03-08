import numpy


class Solution: #floyd algo, loop in linkedList
    def findDuplicate(self, nums: list) -> int:
        n = len(nums)
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
    def zeroStart(self, nums):
        n = len(nums)
        start = 0
        while start < n:
            if nums[start] != start:
                break
            start += 1
        fast, slow = start, start
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = start
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

nums = [0,2,3,1,1]
print(Solution().zeroStart(nums))