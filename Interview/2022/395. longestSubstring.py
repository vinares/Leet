# If some character c appears less than k times in s, c becomes a spliter of s


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k: return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)


s = "ababacb"

k = 3
print(Solution().longestSubstring(s, k))