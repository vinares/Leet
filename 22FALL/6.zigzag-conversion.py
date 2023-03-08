#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = [[] for _ in range(numRows)]
        i = 0
        j = numRows
        while i < len(s):
            if j == numRows:
                for k in range(numRows):
                    ans[k].append(s[i])
                    i += 1
                    if i >= len(s): break
            else:
                ans[j-1].append(s[i])
                i += 1
            j -= 1
            if j <= 1:
                j = numRows
        print(ans)

        return ''.join(''.join(x) for x in ans)
# @lc code=end

