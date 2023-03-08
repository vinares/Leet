#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        characters = Counter(s)
        monotonous_stack = []
        for c in s:
            characters[c] -= 1
            if c not in monotonous_stack:
                while monotonous_stack and monotonous_stack[-1] > c and characters[monotonous_stack[-1]] > 0:
                    remove = monotonous_stack.pop()
                monotonous_stack.append(c)
        return ''.join(monotonous_stack)

# @lc code=end

