class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s: return []
        res = []
        longest = 0
        for word in wordDict:
            if len(word) > longest:
                longest = len(word)

        def backtrack(tmp, i, j):
            if i == j and i == len(s):
                res.append(tmp[1::])
                return

            if j - i + 1 > longest:
                return
            if s[i:j + 1] in wordDict:
                backtrack(tmp + ' ' + s[i:j + 1], j + 1, j + 1)
            backtrack(tmp, i, j + 1)
            return

        backtrack('', 0, 0)

        return res