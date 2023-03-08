class Solution:
    def threeSum(self, nums: list) -> list:
        if not nums: return []
        nums.sort()
        print(nums)
        if nums[0] > 0 or nums[-1] <0: return []
        result = []
        n = len(nums)
        last = 0
        hash = dict()
        for i in range(n):
            if nums[i] > 0:
                break
            reverse = self.twoSum(nums[i + 1: n], -nums[i])
            while reverse:
                if nums[i] not in hash:
                    hash.setdefault(nums[i],[]).append(nums[reverse[1]+i])
                    element = [nums[i],nums[reverse[0]+i],nums[reverse[1]+i]]
                    result.append(element)
                else:
                    flag = 0
                    for _ in  hash[nums[i]]:
                        if _ == nums[reverse[1]+i]:
                            flag = 1

                    if not flag:
                        hash.setdefault(nums[i], []).append(nums[reverse[1] + i])
                        element = [nums[i], nums[reverse[0] + i], nums[reverse[1] + i]]
                        result.append(element)
                reverse = self.twoSum(nums[i + 1 : reverse[1] + i], -nums[i])
        return result

    def twoSum(self, numbers, target: int):
        n = len(numbers)
        left, right = 0, n - 1
        while left < right:
            mid = left + (right - left) // 2
            side = numbers[left] + numbers[right]
            if side == target:
                return [left + 1, right + 1]
            elif side < target:
                left += 1
            else:
                right -= 1
        return []


case = Solution()
nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
print(case.threeSum(nums))