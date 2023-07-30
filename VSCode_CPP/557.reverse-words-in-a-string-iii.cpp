/*
 * @lc app=leetcode id=557 lang=cpp
 *
 * [557] Reverse Words in a String III
 */

// @lc code=start
class Solution {
public:
    string reverseWords(string s) {
        int left = 0, right = 0;

        while (right < s.length()) {
            if (s[right+1] == ' ' || right==s.length()-1) {
                int k = right;
                while (k > left) {
                    swap(s[k--], s[left++]);
                }
                left=++right+1 ;
            }
            right++;
        }
        return s;
    }
};
// @lc code=end

