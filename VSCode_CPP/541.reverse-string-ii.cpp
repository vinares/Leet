/*
 * @lc app=leetcode id=541 lang=cpp
 *
 * [541] Reverse String II
 */

// @lc code=start
class Solution {
public:
    string reverseStr(string s, int k) {
        string ans;
        int n = s.size();
        int cur=0, reverse_end=0, period_end=0;
        int i;
        while (cur < n) {
            reverse_end = min(cur+k-1, n-1);
            period_end = min(cur+k*2-1, n-1);
            for(i=reverse_end; i>=cur; i--) ans += s[i];
            for(i=reverse_end+1; i<= period_end; i++) ans += s[i];
            cur += 2*k;
        }
        return ans;
    }
};
// @lc code=end

