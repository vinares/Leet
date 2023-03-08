#
# @lc app=leetcode id=331 lang=python3
#
# [331] Verify Preorder Serialization of a Binary Tree
#

# @lc code=start
class Solution(object):
    def isValidSerialization(self, preorder):
        degree = 1
        i = 0
        while i<len(preorder):
            if preorder[i] == ',':
                i += 1
                continue
            degree -= 1
            if degree < 0:
                return False
            if preorder[i] == '#':
                i += 1
                continue
            while i < len(preorder) and preorder[i] not in ',#':
                i += 1
            degree += 2
        return degree == 0

# @lc code=end

