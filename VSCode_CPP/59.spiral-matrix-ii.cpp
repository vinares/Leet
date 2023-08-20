/*
 * @lc app=leetcode id=59 lang=cpp
 *
 * [59] Spiral Matrix II
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> matrix(n, vector<int> (n));
        int cnt = 0;
        int left=-1, right=n-1, top=0, down=n-1;
        while(cnt < n*n) { 
            for(int i=++left; i<=right; i++) matrix[top][i] = ++cnt;
            for(int i=++top; i<=down; i++) matrix[i][right] = ++cnt;
            for(int i=--right; i>=left; i--) matrix[down][i] = ++cnt;
            for(int i=--down; i>=top; i--) matrix[i][left] = ++cnt;
        }
        return matrix;
    }
};
// @lc code=end

