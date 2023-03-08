#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left, right = 1, len(height)-2
        lb, rb = height[0], height[len(height)-1]
        while left <= right:
            if height[left-1] < height[right+1]:
                lb = max(lb, height[left])
                min_b = lb
                if min_b > height[left]:
                    ans += min_b - height[left]
                left += 1
            else:
                rb = max(rb, height[right])
                min_b = rb
                if min_b > height[right]:
                    ans += min_b - height[right]
                right -= 1
        return ans

        

# @lc code=end
