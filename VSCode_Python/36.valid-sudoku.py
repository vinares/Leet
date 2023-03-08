#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col= [set() for _ in range(9)], [set() for _ in range(9)]
        nut = [[set() for i in range(3)] for _ in range(3)]
        for c in range(9):
            for r in range(9):
                ch = board[c][r]
                if ch == '.':
                    continue
                if ch in row[r] or ch in col[c] or ch in nut[c//3][r//3]:
                    return False
                row[r].add(ch)
                col[c].add(ch)
                nut[c//3][r//3].add(ch)
                
        return True

# @lc code=end

