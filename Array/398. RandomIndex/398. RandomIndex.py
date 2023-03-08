from collections import defaultdict
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = defaultdict(list)
        for i in range(len(nums)):
            self.nums[nums[i]].append(i)
        
    def pick(self, target: int) -> int:
        return random.choice(self.nums[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)