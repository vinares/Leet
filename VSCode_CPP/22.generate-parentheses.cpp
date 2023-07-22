/*
 * @lc app=leetcode id=22 lang=cpp
 *
 * [22] Generate Parentheses
 */

// @lc code=start
class Solution {
public:
    void bt(string &s, int left, int right, vector<string> &ans) {
        if (left == right && left == 0) {
            ans.push_back(s);
            return;
        }
        if (left > 0) {
            s.push_back('(');
            bt(s, left-1, right, ans);
            s.pop_back();
        }
        if (right > left) {
            s.push_back(')');
            bt(s, left, right-1, ans);
            s.pop_back();
        }
    }
    vector<string> generateParenthesis(int n) {
        string s;
        vector<string> ans;
        bt(s, n, n, ans);
        return ans;
    }
};
// @lc code=end

