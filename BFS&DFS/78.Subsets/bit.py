class Solution:
    def subsets(self, nums: list) -> list:
        n = len(nums)
        res = []
        for i in range(1 << n):
            tmp = []
            for j in range(n):
                if i >> j & 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res


nums = [1,2,3]
a = Solution().subsets(nums)
print(a)
print(len(a) == 2 ** (len(nums)))
