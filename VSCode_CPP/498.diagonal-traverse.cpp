/*
 * @lc app=leetcode id=498 lang=cpp
 *
 * [498] Diagonal Traverse
 */

// @lc code=start
class Solution {
   public:
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        vector<int> res;
        if (mat.empty() || mat[0].empty()) return res;
        int m = mat.size(), n = mat[0].size();
        for (int dia = 0; dia < m + n - 1; dia++) {
            if (dia % 2 == 0) {
                for (int x = min(dia, m - 1); x >= 0 && dia - x < n; x--)
                    res.push_back(mat[x][dia - x]);
            } else {
                for (int x = max(0, dia - n + 1); dia - x >= 0 && x < m; x++)
                    res.push_back(mat[x][dia - x]);
            }
        }
        return res;
    }
};
// @lc code=end
