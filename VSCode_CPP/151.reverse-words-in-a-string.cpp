/*
 * @lc app=leetcode id=151 lang=cpp
 *
 * [151] Reverse Words in a String
 */

// @lc code=start
class Solution {
public:
    string reverseWords(string s) {
        int begin=0, end=0;
        string ans;
        while (begin<s.length()) {
            while(s[begin] == ' ') begin++;
            if (begin>=s.length()) break;
            end = begin;
            while(end+1<s.length() && s[end+1] != ' ') end++;
            for(int i=end; i>=begin; i--) ans.push_back(s[i]);
            ans.push_back(' ');
            begin = end+1;
        }
        ans.pop_back();
        for (int i=0; i<ans.length()/2; i++) {
            swap(ans[i], ans[ans.length()-1-i]);
        }
        return ans;
    }
};
// @lc code=end

