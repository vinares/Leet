/*
 * @lc app=leetcode id=290 lang=cpp
 *
 * [290] Word Pattern
 */

// @lc code=start
class Solution {
public:
    bool wordPattern(string pattern, string s) {
        unordered_map<char, string> p2s;
        unordered_map<string, char> s2p;
        int pattern_length = pattern.size();
        int string_pointer = 0;
        for (int i=0; i<pattern_length; i++) {
            if (string_pointer >= s.size()) return false;
            int right = string_pointer;
            do{
                right ++;
            }  while (right < s.size() && s[right] != ' ');
            const string &tmp = s.substr(string_pointer, right-string_pointer);
            if (p2s.count(pattern[i]) && p2s[pattern[i]] != tmp)
                return false;
            if (s2p.count(tmp) && s2p[tmp] != pattern[i]) 
                return false;
            s2p[tmp] = pattern[i];
            p2s[pattern[i]] = tmp;
            string_pointer = right+1;
        }
        return string_pointer >= s.size();
    }
};
// @lc code=end

