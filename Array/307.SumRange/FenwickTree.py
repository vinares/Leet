class NumArray:
    def __init__(self, nums: list):
        self.fenwick = [0 for _ in range(len(nums) + 1)]
        for k in range(1, len(nums) + 1):
            self.fenwick[k] = sum(nums[k - (k & -k) : k])

    def update(self, i: int, val: int) -> None:
        diff = val - self.sumRange(i,i)
        k = i + 1
        while  k < len(self.fenwick):
            self.fenwick[k] += diff
            k += k & -k

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.sum1k(j + 1)
        else:
            return self.sum1k(j + 1) - self.sum1k(i)

    def sum1k(self, k: int):
        ans = 0
        while k >= 1:
            ans += self.fenwick[k]
            k -= k & -k
        return ans

nums = [1, 3, 5]
NumArray(nums)
obj = NumArray(nums)
param_1 = obj.sumRange(0,2)
obj.update(1,2)
param_2 = obj.sumRange(0,2)

print(param_1, param_2)