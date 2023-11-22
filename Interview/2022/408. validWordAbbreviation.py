class Solution:
    def validWordAbbreviation(self, s, abbr):
        i = 0
        j = 0
        l = 0
        while j < len(abbr) and i < len(s):
            if s[i] == abbr[j]:
                i += 1
                j += 1
                continue
            else:
                if not '0' < abbr[j] <= '9': return False
                else:
                    while j < len(abbr) and '0' <= abbr[j] <= '9':
                        l = l * 10 + int(abbr[j])
                        j += 1
                i += l
        return i == len(s) and j == len(abbr)

s = "aaa"
abbr = "a2"
print(Solution().validWordAbbreviation(s, abbr))