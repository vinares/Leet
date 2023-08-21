/*
 * @lc app=leetcode id=56 lang=cpp
 *
 * [56] Merge Intervals
 */

// @lc code=start
class Solution {
   public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> merged;
        sort(intervals.begin(), intervals.end());
        for (int i = 0; i < intervals.size(); i++) {
            int L = intervals[i][0], R = intervals[i][1];
            if (!merged.empty() && merged.back()[1] >= L)
                merged.back()[1] = max(R, merged.back()[1]);
            else
                merged.push_back(intervals[i]);
        }
        return merged;
    }
};
// @lc code=end
