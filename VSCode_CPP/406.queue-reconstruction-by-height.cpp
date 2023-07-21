/*
 * @lc app=leetcode id=406 lang=cpp
 *
 * [406] Queue Reconstruction by Height
 */

// @lc code=start
class Solution {
public:
    static bool comparator(const vector<int>& a, const vector<int>& b) {
        if (a[0]==b[0]) {
            return a[1]<b[1];
        }
        return a[0] > b[0];
    }

    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end(), comparator);
        vector<vector<int>> queue;
        for(auto person:people) {
            queue.insert(queue.begin()+person[1], person);
        }
        return queue;

    }
};
// @lc code=end

