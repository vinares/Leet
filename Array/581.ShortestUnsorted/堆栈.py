class Solution:
    def findUnsortedSubarray(self, nums: list) -> int:
        n = len(nums)
        stack = []
        left, right = n - 1, 0
        stack.append(0)
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                stack.append(i)
            else:
                while stack and nums[i] < nums[stack[-1]]:
                    left = min(left, stack.pop())

        stack.clear()
        stack.append(n - 1)
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                stack.append(i)
            else:

                while stack and nums[i] > nums[stack[-1]]:
                    right = max(right, stack.pop())
        return right - left + 1 if right > left else 0

case = Solution()
nums =  [2,1]
print(case.findUnsortedSubarray(nums))