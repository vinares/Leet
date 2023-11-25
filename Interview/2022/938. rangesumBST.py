import random
class Solution:
    def __init__(self, nums:list):
        nums = [(nums[i], i) for i in range(len(nums))]
        self.nums = sorted(nums)

    def pick(self, target: int) -> int:

        left, right = 0, len(self.nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if self.nums[mid][0] == target:
                break
            elif self.nums[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1

        l, r = mid, mid
        flag = True
        while flag:
            flag = False
            if l >= 0 and self.nums[l][0] == target:
                flag = True
                l -= 1
            if r < len(self.nums) and self.nums[r][0] == target:
                flag = True
                r += 1
        index = random.choice(range(l+1,r,1))
        return self.nums[index][1]


nums = [1, 2, 3]
pick = 3
print(Solution(nums).pick(pick))