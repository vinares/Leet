/*
 * @lc app=leetcode id=11 lang=cpp
 *
 * [11] Container With Most Water
 */

// @lc code=start
class Solution {
   public:
    int maxArea(vector<int>& height) {
        int left = 0, right = height.size() - 1;
        int ans = (right - left) * min(height[left], height[right]);
        while (left < right) {
            if (height[left] < height[right]) left++;
            else right--;
            int water = (right - left) * min(height[left], height[right]);
            ans = max(ans, water);
        }
        return ans;
    }
};
// @lc code=end
