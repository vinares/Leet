class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        last_occurance = {c:i for i, c in enumerate(s)}
        seen = set()
        for i, let in enumerate(s):
            if let not in seen:
                while stack and let < stack[-1] and i < last_occurance[stack[-1]]:
                    seen.discard(stack.pop())

                stack.append(let)
                seen.add(let)

        return ''.join(stack)



case = Solution()
s = 'cbacdcbc'
print(case.removeDuplicateLetters(s))