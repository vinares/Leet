/*
 * @lc app=leetcode id=713 lang=cpp
 *
 * [713] Subarray Product Less Than K
 */

// @lc code=start
class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int ans=0, i=0, prod=1;
        for (int j=0; j<nums.size(); j++) {
            prod *= nums[j];
            while (i<nums.size() && prod >=k){
                prod /= nums[i++];
            }
            if (prod < k) ans += j-i+1;
        }
        return ans;
    }
};
// @lc code=end

