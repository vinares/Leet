/*
 * @lc app=leetcode id=695 lang=cpp
 *
 * [695] Max Area of Island
 */

// @lc code=start
class Solution {
   public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        m = grid.size();
        n = grid[0].size();
        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    ans = max(ans, mark(grid, i, j, 0));
                }
            }
        }
        return ans;
    }

   private:
    int m, n;
    int mark(vector<vector<int>>& grid, int i, int j, int area) {
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] != 1) return 0;
        grid[i][j] = 0;
        area += 1;
        area += mark(grid, i + 1, j, 0);
        area += mark(grid, i - 1, j, 0);
        area += mark(grid, i, j + 1, 0);
        area += mark(grid, i, j - 1, 0);
        return area;
    }
};
// @lc code=end
