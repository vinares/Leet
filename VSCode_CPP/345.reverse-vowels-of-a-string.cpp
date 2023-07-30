/*
 * @lc app=leetcode id=345 lang=cpp
 *
 * [345] Reverse Vowels of a String
 */

// @lc code=start
class Solution {
public:
    string reverseVowels(string s) {
        string vowels = "aeiouAEIOU";
        string ans = s;
        int start = 0, end = s.size()-1;
        while (start < end)
        {
            while (start < end && vowels.find(s[start]) == -1)
                start++;
            while (start < end && vowels.find(s[end]) == -1)
                end--;
            swap(ans[start], ans[end]);
            start++;
            end--;
        }
        return ans;
        

    }
};
// @lc code=end

