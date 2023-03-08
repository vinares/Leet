class Solution:
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
numbers = [3,24,50,79,88,150,345]
target = 200
print(case.twoSum(numbers, target))
