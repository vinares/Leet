/*
 * @lc app=leetcode id=11 lang=cpp
 *
 * [11] Container With Most Water
 */

// @lc code=start
class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0, right = height.size()-1;
        int dummy = (right-left) * min(height[left], height[right]);
        while (left < right) {
            if (height[left] < height[right] ) {
                left += 1;
            } else {
                right -= 1;
            }
            int cur_prod = (right-left) * min(height[left], height[right]);
            if (cur_prod > dummy)
                dummy = cur_prod;
        }
        return dummy;
    }
};
// @lc code=end

