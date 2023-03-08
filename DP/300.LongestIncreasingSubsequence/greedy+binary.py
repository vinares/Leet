class Solution:
    def lengthOfLIS(self, nums: list) -> int:
        n = len(nums)
        length = 1
        greedy = [nums[0]]
        for i in range(1, n):
            if nums[i] > greedy[length - 1]:
                length += 1
                greedy.append(nums[i])
            else:
                j = self.search(greedy, nums[i])
                greedy[j] = nums[i]

        return len(greedy)

    def search(self, array, number):
        left, right = 0, len(array) - 1
        while left < right:
            mid = left + (right - left) // 2
            if number > array[mid]:
                left = mid + 1
            else:
                right = mid
        return right

nums =  [3,5,6,2,5,4,19,5,6,7,12]
print(Solution().lengthOfLIS(nums))