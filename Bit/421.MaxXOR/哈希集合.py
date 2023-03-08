class Solution:
    def findMaximumXOR(self, nums: list) -> int:
        L = len(bin(max(nums))) - 2
        maxor = 0
        for i in range(L)[::-1]:
            maxor <<= 1
            cur = maxor | 1
            prefix = {num >> i for num in nums}
            maxor |= any(cur ^ p in prefix for p in prefix)
            if maxor != cur:
                print(any(cur ^ p in prefix for p in prefix))
        return maxor


print(Solution().findMaximumXOR(nums=[3,10,5,25,2,8]))