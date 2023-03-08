#
# @lc app=leetcode id=318 lang=python3
#
# [318] Maximum Product of Word Lengths
#

# @lc code=start
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        n = len(words)
        codes = []
        for word in words:
            binary = ['0' for _ in range(26)]
            for x in word:
                binary[ord(x) - ord('a')] = '1'
                if '0' not in binary:
                    break
            codes.append(int(''.join(binary), 2))
        for i in range(n):
            for j in range(i):
                if codes[i] & codes[j] == 0:
                    ans = max(ans, len(words[i])*len(words[j]))
        return ans
# @lc code=end

