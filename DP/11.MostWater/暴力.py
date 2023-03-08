class Solution:
    def maxArea(self, height: list) -> int:
        ans = min(height[0], height[1])
        for i in range(len(height)):
            for j in range(i):
                if height[j] >= height[i]:
                    ans = max(ans, (height[i] * (i - j)))
                    break
            for j in range(len(height) - 1, i, -1):
                if height[j] >= height[i]:
                    ans = max(ans, (height[i] * (j - i)))
                    break
        return ans

print(Solution().maxArea(height=[1,0,0,0,0,0,0,2,2]))