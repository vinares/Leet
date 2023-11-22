#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        names = path.split('/')
        for name in names:
            if name == '..' and stack:
                stack.pop()
            elif name not in '..':
                stack.append(name)
        return '/' + '/'.join(stack)


# @lc code=end

