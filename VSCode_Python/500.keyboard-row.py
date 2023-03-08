#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#

# @lc code=start
#

class Solution:
    def __init__(self) -> None:
        self.row = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm",
        ]

    def findWords(self, words: List[str]) -> List[str]:
        ans = []

        for word in words:
            if len(word) < 2:
                ans.append(word)
                continue
            a = word[0].lower()
            for r in self.row:
                if a in r:
                    des = r
                    break
            for i in range(1, len(word)):
                if word[i].lower() not in des:
                    break
                if i == len(word) - 1:
                    ans.append(word)
        return ans
            
# @lc code=end

