class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        if not nums: return None
        nums.sort()
        print(nums)
        n = len(nums)
        result = nums[0] + nums[1] + nums[2]
        tmp = result
        def update(cur):
            nonlocal result
            if abs(result - target) > abs(cur - target):
                result = cur

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                cur = nums[i] + nums[j] + nums[k]
                print(i,j,k)
                if cur == target:
                    return target
                update(cur)
                if cur < target:
                    if nums[i] + nums[n - 2] + nums[n - 1] < target:
                        update(nums[i] + nums[n - 2] + nums[n - 1])
                        break
                    j0 = j + 1
                    while nums[j0] == nums[j] and j0 < k:
                        j = j0
                        j0 += 1
                    j = j0
                else:
                    if nums[i] + nums[i + 1] + nums[i + 2] > target:
                        update(nums[i] + nums[i + 1] + nums[i + 2])
                        break
                    k0 = k - 1
                    while nums[k0] == nums[k] and j < k0:
                        k = k0
                        k0 -= 1
                    k = k0
        return result


case = Solution()
nums =  [0,1,0,3,12]
print(case.threeSumClosest(nums, 5))