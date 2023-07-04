/*
 * @lc app=leetcode id=448 lang=cpp
 *
 * [448] Find All Numbers Disappeared in an Array
 */

// @lc code=start
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> ans;
        for (int i=0; i<nums.size(); i++){
            int a = abs(nums[i]) - 1;
            if (nums[a] < 0) continue;
            nums[a] = -1 * nums[a];
        }
        for (int i=0; i<nums.size(); i++){
            if (nums[i] > 0) {
                ans.push_back(i+1);
            }
        }
        return ans;
    }
};
// @lc code=end

