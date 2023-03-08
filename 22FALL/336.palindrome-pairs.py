#
# @lc app=leetcode id=336 lang=python3
#
# [336] Palindrome Pairs
#

# @lc code=start
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans, n = [], len(words)
        wordmap = {words[i]: i for i in range(n)}
        for i in range(n):
            w = words[i]
            l = len(w)
            if w=='':
                for j in range(n):
                    if j!=i and words[j]==words[j][::-1]:
                        ans.append([i, j])
                        ans.append([j, i])
            if w[::-1] in wordmap and wordmap[w[::-1]] > i:
                ans.append([wordmap[w[::-1]], i])
                ans.append([i, wordmap[w[::-1]]])
            for j in range(l-1):
                if w[:j+1]==w[:j+1][::-1] and w[j+1:][::-1] in wordmap:
                    ans.append([wordmap[w[j+1:][::-1]], i])
            for j in range(1, l):
                if w[j:]==w[j:][::-1] and w[:j][::-1] in wordmap:
                    ans.append([i, wordmap[w[:j][::-1]]])
        return ans

# @lc code=end

