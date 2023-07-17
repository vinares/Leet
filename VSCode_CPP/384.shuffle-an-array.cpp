/*
 * @lc app=leetcode id=384 lang=cpp
 *
 * [384] Shuffle an Array
 */

// @lc code=start
class Solution {
    int n;
    vector<int> original;
public:
    Solution(vector<int>& nums) {
        original = nums;
        n = nums.size();
    }
    
    vector<int> reset() {
        return original;
    }
    
    vector<int> shuffle() {
        vector<int> ans = original;
        for (int i=n-1; i>0; i--) {
            int random_index = rand() % (i+1);
            swap(ans[random_index], ans[i]);
        }
        return ans;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */
// @lc code=end

