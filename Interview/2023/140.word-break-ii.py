#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
class Trie:
    def __init__(self) -> None:
        self.map = {}

    def insert(self, word):
        t = self.map
        for ch in word:
            if ch not in t:
                t[ch] = Trie().map
            t = t[ch]
        t["#"] = True

    def get(self, s, start):
        t = self.map
        ans = []
        for i in range(start, len(s)):
            if s[i] not in t:
                break
            t = t[s[i]]
            if '#' in t:
                ans.append(i+1)
        return ans

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        
        ans = []
        
        def backtrack(i, tmp):
            nonlocal ans
            if i == len(s):
                ans.append(tmp[:-1])
                return
            ends = trie.get(s, i)
            for end in ends:
                backtrack(end, tmp + s[i:end] + ' ')
            return
        backtrack(0, '')
        return ans

# @lc code=end

