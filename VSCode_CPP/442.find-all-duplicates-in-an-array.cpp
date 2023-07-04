/*
 * @lc app=leetcode id=442 lang=cpp
 *
 * [442] Find All Duplicates in an Array
 */

// @lc code=start
class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> ans;
        for(int i=0; i< nums.size(); i++){
            int a = abs(nums[i]) - 1;
            nums[a] = -1 * nums[a];
            if (nums[a] > 0) {
                ans.push_back(a+1);
            } 
        }
        return ans;
    }
};
// @lc code=end

