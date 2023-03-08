class Solution:
    def minOperations(self, target: list, arr: list) -> int:
        infinity = 10 ** 6
        target_hash = dict()
        arr_hash = dict()
        for i, tar in enumerate(target):
            target_hash[tar] = i

        new_arr = []
        for x in arr:
            if x in target_hash.keys():
                new_arr.append(target_hash[x])

        dp = [1] * len(new_arr)
        for i in range(1, len(new_arr)):
            for j in range(i):
                if new_arr[i] > new_arr[j]:
                    dp[i] = max(dp[i], dp[j] + 1)


        return len(target) - max(dp) if dp else len(target)

target = [1,3,8]
arr = [2,6]
print(Solution().minOperations(target,arr))