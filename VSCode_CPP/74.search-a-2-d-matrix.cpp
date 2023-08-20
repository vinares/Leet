/*
 * @lc app=leetcode id=74 lang=cpp
 *
 * [74] Search a 2D Matrix
 */

// @lc code=start
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m=matrix.size(), n=matrix[0].size();
        int i=0, j=0;
        while(i<m && j<n) {
            if (matrix[i][j]>target) return false;
            else if (matrix[i][j] == target) return true;
            else if (i+1<m && matrix[i+1][j]<=target) i++;
            else j++;
        }
        return false;
    }
};
// @lc code=end

