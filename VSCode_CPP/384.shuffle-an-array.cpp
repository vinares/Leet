/*
 * @lc app=leetcode id=384 lang=cpp
 *
 * [384] Shuffle an Array
 */

// @lc code=start
class Solution {
    int n;
    vector<int> original_nums;
public:
    Solution(vector<int>& nums) {
        original_nums = nums;
        n = original_nums.size();
    }
    
    vector<int> reset() {
        return original_nums;
    }
    
    vector<int> shuffle() {
        vector<int> arr = original_nums;
        int sz = n;
        for(int i=n-1;i>-1;i--)
        {
            int ind = rand()%sz--;
            swap(arr[ind],arr[i]);
        }
        return arr;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */
// @lc code=end

