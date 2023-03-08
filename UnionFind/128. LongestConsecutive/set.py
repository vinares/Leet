class Solution:
    def longestConsecutive(self, nums: list) -> int:
        n = len(nums)
        if n < 2:
            return n
        numset = set(nums)
        cnt = 1
        while numset:
            pivot = numset.pop()
            tmp = 1
            left, right = pivot - 1, pivot + 1
            while left in numset:
                numset.remove(left)
                tmp += 1
                left -= 1
            while right in numset:
                numset.remove(right)
                tmp += 1
                right += 1
            cnt = max(cnt, tmp)
        return cnt

nums = [0,3,7,2,5,8,4,6,0,1]
print(Solution().longestConsecutive(nums))