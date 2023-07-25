/*
 * @lc app=leetcode id=14 lang=cpp
 *
 * [14] Longest Common Prefix
 */

// @lc code=start
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string ans = "";
        if (strs.size() == 0) return ans;
        sort(strs.begin(), strs.end());
        string *first = &strs[0];
        string *last = &strs[strs.size()-1];
        for (int i=0; i<min((*first).size(), (*last).size()); i++) {
            if ((*first)[i] != (*last)[i]) break;
            ans += (*first)[i];
        }
        return ans;

    }
};
// @lc code=end

