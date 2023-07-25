/*
 * @lc app=leetcode id=58 lang=cpp
 *
 * [58] Length of Last Word
 */

// @lc code=start
class Solution
{
public:
    int lengthOfLastWord(string s)
    {
        int n = s.size() - 1;
        int cnt = 0;
        for (n; n >= 0; n--)
            if (s[n] != ' ')
            {
                n++;
                break;
            }
        for (int i = n - 1; i >= -1; i--)
            if (i < 0 || s[i] == ' ')
            {
                cnt = max(0, n - i - 1);
                break;
            }
        return cnt;
    }
};
// @lc code=end
