/*
 * @lc app=leetcode id=240 lang=cpp
 *
 * [240] Search a 2D Matrix II
 */

// @lc code=start
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m=matrix.size(), n=matrix[0].size();
        int i=0, j=n-1;
        while(i<m && j>-1) {
            if(matrix[i][j]==target) return true;
            else if(matrix[i][j]>target) {
                if (j==0) return false;
                j--;
            } else if (matrix[i][j]<target) {
                if (i==m-1) return false;
                i++;
            }
        }
        return false;
    }
};
// @lc code=end

