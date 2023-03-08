class Solution:
    def findDuplicates(self, nums: list) -> list:
        n = len(nums)
        if not nums:
            return []
        def swap(nums:list, ind1:int, ind2: int):
            if ind1 == ind2:return
            tmp = nums[ind1]
            nums[ind1] = nums[ind2]
            nums[ind2] = tmp
            return

        result = []
        for i, num in enumerate(nums):
            while nums[i] != i + 1:
                swap(nums, i, nums[i] - 1)
                if nums[i] == nums[nums[i] - 1]:
                    break
        for i, num in enumerate(nums):
            if i != num - 1:
                result.append(num)
        return result
case = Solution()
nums = [4,3,2,7,8,2,3,1]
print(case.findDuplicates(nums))