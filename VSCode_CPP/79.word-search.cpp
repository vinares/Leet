/*
 * @lc app=leetcode id=79 lang=cpp
 *
 * [79] Word Search
 */

// @lc code=start
class Solution {
   public:
    bool exist(vector<vector<char>>& board, string word) {
        m = board.size(), n = board[0].size();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dfs(board, word, i, j, 0)) return true;
            }
        }
        return false;
    }

   private:
    int m, n;
    bool dfs(vector<vector<char>>& board, string word, int i, int j, int k) {
        if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] != word[k])
            return false;
        if (k == word.size() - 1) return true;
        board[i][j] = '\0';
        bool dfs_rs = dfs(board, word, i + 1, j, k + 1) ||
                      dfs(board, word, i - 1, j, k + 1) ||
                      dfs(board, word, i, j + 1, k + 1) ||
                      dfs(board, word, i, j - 1, k + 1);
        board[i][j] = word[k];
        return dfs_rs;
    }
};
// @lc code=end
