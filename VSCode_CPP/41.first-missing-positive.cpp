/*
 * @lc app=leetcode id=41 lang=cpp
 *
 * [41] First Missing Positive
 */

// @lc code=start
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int max_num = 0;
        int l = nums.size() - 1;
        int r = nums.size() - 1;
        while (r >= 0) {
            if (nums[r] <= 0) {
                swap(nums[l], nums[r]);
                l--;
            }
            if (nums[r] > max_num) {
                max_num = nums[r];
            }
            r--;
        }
        for (int i=0; i<l+1; i++) {
            if (abs(nums[i])-1 <= l && nums[abs(nums[i])-1] > 0) {
                nums[abs(nums[i])-1] = 0 - nums[abs(nums[i])-1];
            }
        }

        for (int i=0; i<l+1; i++){
            if (nums[i] > 0) return i+1;
        }
        return max_num+1;
    }
};
// @lc code=end

