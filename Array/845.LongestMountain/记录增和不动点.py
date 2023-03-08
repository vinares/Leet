class Solution:
    def longestMountain(self, arr: list) -> int:
        n = len(arr)
        record = []
        for i in range(n - 1):
            if arr[i] <= arr[i + 1]:
                if i == 0 or arr[i - 1] >= arr[i]:
                    record.append(i)
            if arr[i] == arr[i + 1]:
                record.append(n)
        if  arr[n - 1] < arr[n - 2]:
            record.append(n - 1)
        longest = 0
        for i in range(len(record) - 1):
            cur = 0
            if record[i] < n and record[i + 1] < n:
                cur = record[i + 1] - record[i] + 1
            if cur > longest:
                longest = cur
        if longest < 3: return 0
        return longest


arr = [1,1,0,0,1,0]
print(Solution().longestMountain(arr))