class Solution:
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.original

    def shuffle(self):
        aux = list(self.array)
        import random
        for idx in range(len(self.array) - 1, -1, -1):
            remove_idx = random.randrange(0, idx + 1)
            self.array[idx] = aux.pop(remove_idx)
        return self.array

nums = [1, 2, 3]
obj = Solution(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()
print(param_1,param_2)
