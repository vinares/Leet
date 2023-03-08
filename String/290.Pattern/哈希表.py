class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        t = s.split()
        Hash = {}
        for i in range(len(pattern)):
            if pattern[i] in Hash:
                if Hash[pattern[i]] != t[i]:
                    return False
            else:
                if t[i] in Hash.values():
                    return False
                Hash[pattern[i]] = t[i]
        return True
case = Solution()
print(case.wordPattern('abba','dog cat cat fish'))