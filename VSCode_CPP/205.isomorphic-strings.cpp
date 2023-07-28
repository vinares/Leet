/*
 * @lc app=leetcode id=205 lang=cpp
 *
 * [205] Isomorphic Strings
 */

// @lc code=start
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        int n = s.size();
        int s_char, t_char;
        if (n!=t.size()) return false;
        vector<int> s2t(128, -1);
        vector<int> t2s(128, -1);
        for (int i=0; i<n; i++) {
            s_char = int(s[i]);
            t_char = int(t[i]);
            if (s2t[s_char] == -1 && t2s[t_char] == -1) {
                s2t[s_char] = t_char;
                t2s[t_char] = s_char;
                continue;
            } else if (s2t[s_char] == t_char && t2s[t_char] == s_char) continue;
            else return false;
        }
        
        return true;

    }
};
// @lc code=end

