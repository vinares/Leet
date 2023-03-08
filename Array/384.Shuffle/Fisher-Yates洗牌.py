class Solution:
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.original

    def shuffle(self):
        import random
        for i in range(len(self.array)):
            swap = random.randrange(i,len(self.array))
            self.array[i], self.array[swap] = self.array[swap], self.array[i]
        return self.array

nums = [1, 2, 3]
obj = Solution(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()
print(param_1,param_2)
