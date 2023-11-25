import random
class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        
        def Qselect(nums, left, right, k):
            n = right - left + 1
            if n < 2:
                return nums[left]
            pivot = random.randint(left, right)
            i, j = left + 1, left + 1
            nums[left], nums[pivot] = nums[pivot], nums[left]

            while j <= right:
                while j <= right and nums[j] < nums[left] and i == j:
                    i += 1
                    j += 1
                if j > right: break
                if nums[j] < nums[left]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
                else:
                    j += 1

            nums[i - 1], nums[left] = nums[left], nums[i - 1]
            if i - 1 == len(nums) - k:
                return nums[i - 1]
            elif i - 1 < len(nums) - k:
                return Qselect(nums, i, right, k)
            else:
                return Qselect(nums, left, i - 1, k)

        return Qselect(nums, 0, len(nums) - 1, k)

nums = [3,2,1,5,6,4]
k = 2
print(Solution().findKthLargest(nums,k))