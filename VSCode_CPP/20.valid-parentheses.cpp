/*
 * @lc app=leetcode id=20 lang=cpp
 *
 * [20] Valid Parentheses
 */

// @lc code=start
class Solution {
public:
    bool isValid(string s) {
        unordered_map <char, char> mp = {
            {']', '['},
            {'}', '{'},
            {')', '('},
        };
        stack<char> st;
        for (auto x:s) {
            if (mp.count(x) > 0) {
                if (st.empty() || st.top() != mp[x]) return false;
                st.pop();
            } else {
                st.push(x);
            }
        }
        return st.empty();
    }
};
// @lc code=end

