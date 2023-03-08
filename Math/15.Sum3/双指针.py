class Solution:
    def threeSum(self, nums: list) -> list:
        if not nums: return []
        nums.sort()
        print(nums)
        if nums[0] > 0 or nums[-1] <0: return []
        result = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            sum = - nums[i]
            left, right = i + 1, n - 1
            while left < right:
                if nums[left] + nums[right] == sum:
                    result.append([nums[i], nums[left], nums[right]])
                    second = nums[left]
                    third = nums[right]
                    while nums[left] == second and nums[right] == third and left < right:
                        left += 1
                        right -= 1
                elif nums[left] + nums[right] < sum:
                    left += 1
                else:
                    right -= 1
        return result


case = Solution()
nums = [0,0,0]
print(case.threeSum(nums))