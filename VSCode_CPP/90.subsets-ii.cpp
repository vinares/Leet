/*
 * @lc app=leetcode id=90 lang=cpp
 *
 * [90] Subsets II
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> ans;
    vector<int> tmp;

    void dfs(vector<int>& nums, int p) {
        ans.push_back(tmp);
        for(int i = p; i<nums.size(); i++) {
            if (i>p && nums[i] == nums[i-1]) continue;
            tmp.push_back(nums[i]);
            dfs(nums, i+1);
            tmp.pop_back();
        }
    }

    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        dfs(nums, 0);
        return ans;
    }
};
// @lc code=end
