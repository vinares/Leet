class Solution:
    def canJump(self, nums: list) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, nums[i] + i)
                if rightmost >= n - 1:
                    return True
        return False

nums =[3,2,1,0,5]
print(Solution().canJump(nums))