class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        Hash = {}
        for i in range(len(s)):
            if s[i] in Hash:
                if Hash[s[i]] != t[i]:
                    return False
            else:
                if t[i] in Hash.values():
                    return False
                Hash[s[i]] = t[i]
        return True

case = Solution()
print(case.isIsomorphic('b00k','l00t'))