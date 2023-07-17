/*
 * @lc app=leetcode id=945 lang=cpp
 *
 * [945] Minimum Increment to Make Array Unique
 */

// @lc code=start
class Solution {
public:
    int minIncrementForUnique(vector<int>& nums) {
        int ans = 0;
        sort(nums.begin(), nums.end());
        for(int i=1; i<nums.size(); i++){
            if (nums[i]<=nums[i-1]){
                ans += nums[i-1]-nums[i]+1;
                nums[i] = nums[i-1]+1;
            }
        }
        return ans;
    }
};
// @lc code=end

