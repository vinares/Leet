/*
 * @lc app=leetcode id=200 lang=cpp
 *
 * [200] Number of Islands
 */

// @lc code=start
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        int ans = 0;
        for (int row=0; row<m; row++) {
            for (int col=0; col<n; col++) {
                if (grid[row][col] == '1') {
                    dfs(row, col, grid, m, n);
                    ans++;
                }
            }
        }
        return ans;
    }

    void dfs(int row, int col, vector<vector<char>>& grid, int m, int n) {
        grid[row][col] = '0';
        int dir[] = {-1, 0, 1, 0, -1};

        for(int i=0; i<4; i++) {
            int r = row + dir[i];
            int c = col + dir[i+1];
            if (0 <= r && r<m && 0 <= c && c < n && grid[r][c] == '1') 
                dfs(r, c, grid, m, n);
        }
    }
};
// @lc code=end

