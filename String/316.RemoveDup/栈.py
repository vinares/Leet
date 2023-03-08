class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        from collections import Counter
        hashtable = Counter(s)
        stack = []
        seen = set()

        for x in s:
            if x not in seen:
                while stack and x < stack[-1] and hashtable[x]:
                    seen.discard(stack.pop())
                stack.append(x)
                seen.add(x)
            hashtable[x] -= 1
        return ''.join(x for x in stack)

print(Solution().removeDuplicateLetters(s = "bcaabac"))