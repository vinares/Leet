#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        s, stack, left, right = str(num), [], None, None
        for i, c in enumerate(s):
            while stack and s[stack[-1]] < c:
                index = stack.pop()
                if left is None or index < left:
                    left = index
                    right = i
                if index == right:
                    right = i
            if right and s[right] == c: right = i
            stack.append(i)
        return int(s[:left]+s[right]+s[left+1:right]+s[left]+s[right+1:]) if left is not None else num      
            
# @lc code=end

