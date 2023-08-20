/*
 * @lc app=leetcode id=54 lang=cpp
 *
 * [54] Spiral Matrix
 */

// @lc code=start
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m=matrix.size(), n=matrix[0].size();
        vector<int> ans(m*n);
        int cnt = 0;
        int left=-1, right = n-1, top=0, down=m-1;
        while(cnt < m*n) {
            if (++left > right) break;
            for (int i=left; i<=right; i++) ans[cnt++] = matrix[top][i];
            if (++top > down) break;
            for (int i=top; i<=down; i++) ans[cnt++] = matrix[i][right];
            if (left > --right) break;
            for (int i=right; i>=left; i--) ans[cnt++] = matrix[down][i];
            if (top > --down) break;
            for (int i=down; i>=top; i--) ans[cnt++] = matrix[i][left];
        }
        return ans;
    }
};
// @lc code=end

