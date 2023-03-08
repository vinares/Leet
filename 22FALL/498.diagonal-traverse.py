#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#

# @lc code=start
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])

        res = []
        left_to_right = True

        for ij_sum in range(0, m+n-1):
            if left_to_right:
                i = min(ij_sum, m-1)
                j = ij_sum-i
            else:
                j = min(ij_sum, n-1)
                i = ij_sum-j

            while 0 <= i <= min(m-1, ij_sum) and (0 <= j <= min(n-1, ij_sum)):
                res.append(mat[i][j])
                if left_to_right:
                    i -= 1
                    j += 1
                else:
                    i += 1
                    j -= 1
            left_to_right = not left_to_right
        
        return res

                

# @lc code=end

