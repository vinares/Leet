/*
 * @lc app=leetcode id=115 lang=cpp
 *
 * [115] Distinct Subsequences
 */

// @lc code=start
#include <algorithm>
class Solution {
public:
    int numDistinct(string s, string t) {
        vector<int> memo(t.length(), 0);
        vector<int> tmp(t.length(), 0);
        int mod = 1e9+7;
        for (int i=0; i<s.length(); i++) {
            tmp = memo;
            for (int j=0; j<min((i+1), int(t.length())); j++) {
                if (s[i] == t[j]) {
                    if (j == 0) tmp[j] ++;
                    else {
                        if (memo[j-1] == 0) break;
                        tmp[j] = (tmp[j] + memo[j-1]) % mod;
                    }
                }
            }
            memo = tmp;
        }
        return memo[t.length()-1];
    }
};
// @lc code=end

