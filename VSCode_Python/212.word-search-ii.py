#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class Solution:
    def findWords(self, board, words):
            if not board or not words: return []
            trie, ans = {}, set()
            m, n = len(board), len(board[0])
            moves = [(1, 0), (0, -1), (-1, 0), (0, 1)]
            for word in words:
                root = trie
                for c in word:
                    if c not in root:
                        root[c] = {}
                    root = root[c]
                root['#'] = None
                
            def dfs(board, i, j, trie, w, ans):
                c = board[i][j]
                trie = trie[c]
                _w = w+c
                if '#' in trie:
                    ans.add(_w)
                    if len(trie) == 1:
                        return
                board[i][j] = '.'
                for dx, dy in moves:
                    nx, ny = i+dx, j+dy
                    if 0<=nx<m and 0<=ny<n and board[nx][ny]!='.' and board[nx][ny] in trie:
                        dfs(board, nx, ny, trie, _w, ans)
                board[i][j] = c
                return

            for i in range(m):
                for j in range(n):
                    if board[i][j] in trie:
                        dfs(board, i, j, trie, '', ans)
            return list(ans)
            


# @lc code=end

