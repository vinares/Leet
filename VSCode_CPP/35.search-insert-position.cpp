/*
 * @lc app=leetcode id=35 lang=cpp
 *
 * [35] Search Insert Position
 */

// @lc code=start
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = -1, right = nums.size();
        while (left+1 < right) {
            int mid = left + (right-left)/2;
            if (nums[mid] < target) left=mid;
            else right=mid;
        }
        return right;
    }
};
// @lc code=end

