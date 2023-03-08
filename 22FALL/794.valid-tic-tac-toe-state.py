#
# @lc app=leetcode id=794 lang=python3
#
# [794] Valid Tic-Tac-Toe State
#

# @lc code=start
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        x, o = 0, 0
        rows, columns, diagnals = [0] * 3, [0] * 3, [0] * 2
        for i in range(3):
            for j in range(3):
                c = board[i][j]
                if c=='X':
                    rows[i] += 1
                    columns[j] += 1
                    if i==j:
                        diagnals[0] += 1
                    if i==2-j:
                        diagnals[1] += 1
                    x+=1
                elif c=='O':
                    o+=1
                    rows[i] -= 1
                    columns[j] -= 1
                    if i==j:
                        diagnals[0] -= 1
                    if i==2-j:
                        diagnals[1] -= 1
        if x < o or x > o+1:
            return False
        p, q = False, False
        for n in rows + columns + diagnals:
            if n == 3:
                p = True
            if n == -3:
                q = True
            
        if p and q:
            return False
        if p and x<=o:
            return False
        if q and x!=o:
            return False
        return True

# @lc code=end

