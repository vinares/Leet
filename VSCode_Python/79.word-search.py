#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        moves = [0, 1, 0, -1, 0]
        
        def dfs(i, j, c_i):            
            if c_i == len(word):
                return True
            if i >= m or j >=n or i < 0 or j<0 or board[i][j] != word[c_i]:
                return False
            tmp = board[i][j]
            board[i][j] = '0'
            for k in range(4):
                dx, dy = i + moves[k], j + moves[k+1]
                if dfs(dx, dy, c_i+1):
                    return True
            board[i][j] = tmp
            return False
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False

# @lc code=end

