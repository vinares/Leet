class Solution:
    def fourSum(self, nums: list, target: int) -> int:
        nums.sort()
        print(nums)
        result = []
        n = len(nums)
        if n < 4: return result

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[j] + nums[j + 1] + nums[j + 2] + nums[i] > target:
                    break
                if nums[j] + nums[i] + nums[n - 2] + nums[n - 1] < target:
                    continue
                sum = target - nums[i] - nums[j]
                left, right = j + 1, n - 1
                while left < right:
                    if nums[left] + nums[right] == sum:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        second = nums[left]
                        third = nums[right]
                        while nums[left] == second and nums[right] == third and left < right:
                            left += 1
                            right -= 1
                    elif nums[left] + nums[right] < sum:
                        if nums[right - 1] + nums[right] < sum:
                            break
                        else:
                            left += 1
                    else:
                        if nums[left] + nums[left + 1] > sum:
                            break
                        else:
                            right -= 1
        return result


case = Solution()
nums =  [-2,-1,-1,1,1,2,2]
print(case.fourSum(nums, 0))