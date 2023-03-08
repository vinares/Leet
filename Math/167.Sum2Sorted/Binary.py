class Solution:
    def twoSum(self, numbers, target: int):
        n = len(numbers)
        for i in range(n):
            tar = target - numbers[i]
            if  numbers[i] <= tar <= numbers[-1]:
                left, right = i + 1, n - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    if numbers[mid] == tar:
                        return [i+1, mid+1]
                    elif numbers[mid] > tar:
                        right = mid - 1
                    else:
                        left = mid + 1
        return []

case = Solution()
numbers = [2,7,11,15]
target = 9
print(case.twoSum(numbers, target))
