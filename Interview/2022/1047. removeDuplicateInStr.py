class Solution:
    def removeDuplicates(self, s: str) -> str:
        index = []
        for i in range(len(s)):
            if index and index[-1] == s[i]:
                index.pop()
            else:
                index.append(s[i])
        return ''.join(index)

s = "aababaab"
print(Solution().removeDuplicates(s))