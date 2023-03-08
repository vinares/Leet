class NumArray:
    def __init__(self, nums: list):
        self.array = list(nums)

    def update(self, i: int, val: int) -> None:
        self.array[i] = val

    def sumRange(self, i: int, j: int) -> int:
        sum = 0
        for k in range(i, j + 1):
            sum += self.array[k]
        return sum

nums = [1, 3, 5]
obj = NumArray(nums)
param_1 = obj.sumRange(0,2)
obj.update(1,2)
param_2 = obj.sumRange(0,2)

print(param_1, param_2)