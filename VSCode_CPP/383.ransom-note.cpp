/*
 * @lc app=leetcode id=383 lang=cpp
 *
 * [383] Ransom Note
 */

// @lc code=start
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        vector<int> memo(26, 0);
        for (auto x:magazine) {
            memo[x - 'a'] ++;
        }
        for (auto x:ransomNote) {
            if (memo[x - 'a'] == 0) return false;
            memo[x - 'a'] --;
        }
        return true;
    }
};
// @lc code=end

