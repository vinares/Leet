#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word[0] < 'a':
            if len(word) == 1:
                return True
            if word[1] < 'a':
                for c in word:
                    if c >= 'a':
                        return False
            else:
                for c in word[2:]:
                    if c < 'a':
                        return False
        else:
            for c in word:
                if c < 'a':
                    return False
        return True
# @lc code=end

