/*
 * @lc app=leetcode id=451 lang=cpp
 *
 * [451] Sort Characters By Frequency
 */

// @lc code=start
class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> mp;
        for (auto x:s) {
            mp[x]++;
        }
        s = "";
        vector<pair<char,int>>vec(mp.begin(), mp.end());
        sort(vec.begin(),vec.end(), [](const pair<char,int> &a, const pair<char,int> &b) {
            return a.second > b.second;
        });
        for (auto x:vec) {
            int cnt = 0;
            while (cnt < x.second) {
                s += x.first;
                cnt++;
            }
        }
        return s;
    }
};
// @lc code=end

