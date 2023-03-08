class Solution:
    def longestMountain(self, arr: list) -> int:
        n = len(arr)
        left = [0] * n
        for i in range(1, n - 1):
            if arr[i] > arr[i - 1]:
                left[i] = left[i - 1] + 1

        right = [0] * n
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                right[i] = right[i + 1] + 1

        longest = 0
        for i in range(n):
            if left[i] and right[i]:
                longest = max(longest, left[i] + right[i] + 1)
        if longest < 3: return 0
        return longest


arr = [2,1,4,7,3,2,5]
print(Solution().longestMountain(arr))