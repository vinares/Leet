#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pri = {ch: i for i, ch in enumerate(order)}
        if not words: return True
        prev = [pri[ch] for ch in words[0]]
        for i in range(1 ,len(words)):
            cur = [pri[ch] for ch in words[i]]
            if cur < prev:
                return False
            prev = cur
        return True

# @lc code=end

