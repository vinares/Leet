/*
 * @lc app=leetcode id=974 lang=cpp
 *
 * [974] Subarray Sums Divisible by K
 */

// @lc code=start
class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        int prefix_sum = 0, ans = 0;
        unordered_map<int,int> m;
        m[0]++;
        int residual;
        for (int x:nums) {
            prefix_sum += x;
            residual = (prefix_sum % k + k) % k;
            if (m.find(residual) != m.end()) ans += m[residual];
            m[residual]++;
        }
        return ans;
    }
};
// @lc code=end

