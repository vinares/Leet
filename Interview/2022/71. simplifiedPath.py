class Solution:
    def simplifyPath(self, path: str) -> str:
        words = path.split('/')
        ans = ''
        back, i = 0, len(words) - 1
        while words:
            word = words.pop()
            if word == '' or word == '.':
                continue
            elif word == '..':
                back += 1
            else:
                if back > 0:
                    back -= 1
                else:
                    ans += word[::-1]
                    ans += '/'
        if not ans: return '/'
        else: return ans[::-1]


path = "/a/./b/../../c/"
print(Solution().simplifyPath(path))