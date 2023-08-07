/*
 * @lc app=leetcode id=392 lang=cpp
 *
 * [392] Is Subsequence
 */

// @lc code=start
class Solution {
public:
    bool isSubsequence(string s, string t) {
        if (s.length() == 0) return true;
        int sp = 0, tp = 0;
        while (tp < t.length()) {
            if (s[sp] == t[tp++]) sp++;
            if (sp >= s.length()) return true; 
        }
        return sp == s.length();
    }
};
// @lc code=end

