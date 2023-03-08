class NumArray:
    def __init__(self, nums: list):
        self.n = len(nums)
        self.segement = [0] * (2 * self.n)
        for i in range(self.n, 2 * self.n):
            self.segement[i] = nums[i - self.n]
        for i in range(self.n - 1, 0, -1):
            self.segement[i] = self.segement[i * 2] + self.segement[i * 2 + 1]

    def update(self, i: int, val: int) -> None:
        diff = val - self.segement[i + self.n]
        k = i + self.n
        while  k > 0:
            self.segement[k] += diff
            k //= 2

    def sumRange(self, i: int, j: int) -> int:
        ans = 0
        i += self.n
        j += self.n
        while i <= j:
            if i % 2 == 1:
                ans += self.segement[i]
                i += 1
            if j % 2 == 0:
                ans += self.segement[j]
                j -= 1
            i //= 2
            j //= 2
        return ans




nums = [1, 3, 5]
NumArray(nums)
obj = NumArray(nums)
param_1 = obj.sumRange(0,2)
obj.update(1,2)
param_2 = obj.sumRange(0,2)

print(param_1, param_2)