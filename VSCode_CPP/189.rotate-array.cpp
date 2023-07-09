/*
 * @lc app=leetcode id=189 lang=cpp
 *
 * [189] Rotate Array
 */

// @lc code=start
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k = k % nums.size();
        reverse(nums.begin(), nums.begin()+nums.size()-k);
        reverse(nums.begin()+nums.size()-k, nums.end());
        reverse(nums.begin(), nums.end());
    }
};
// @lc code=end

