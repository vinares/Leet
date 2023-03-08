from functools import  lru_cache
@lru_cache(128)
class Solution:
    def wordBreak(self, s: str, wordDict: list) -> list:
        if s == '':
            return ['']
        n = len(s)
        dp = [[] * n]
        ans = []
        for i in range(n-1, -1, -1):
            if s[i::] in wordDict:
                subans = self.wordBreak(s[0:i], wordDict)
                for l in subans:
                    if l != '':
                        ans.append(l + ' ' + s[i::])
                    else:
                        ans.append(l + s[i::])
        return ans



s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
print(Solution().wordBreak(s, wordDict))