class Solution:
    def maxArea(self, height: list) -> int:
        left, right = 0, len(height) - 1
        lb, rb = left, right
        ans = (right - left) * min(height[left], height[right])
        while left < right:
            if height[left] < height[right]:
                left += 1
                if height[left] <= height[lb]:
                    continue
            else:
                right -= 1
                if height[right] <= height[rb]:
                    continue
            if (right - left) * min(height[left], height[right]) > ans:
                lb, rb = left, right
                ans = (right - left) * min(height[left], height[right])
        return ans




print(Solution().maxArea(height=[2,3,4,5,18,17,6]))