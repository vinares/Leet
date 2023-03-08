class Solution:
    def compress(self, chars: list) -> int:
        chars.append('0')
        char = chars[0]
        cur = chars[1]
        i = 1
        count = 1
        while cur != '0':
            if cur == char:
                count += 1
            else:
                chars.append(char)
                chars.append(int(count))
                char = cur

            chars.pop(0)
            i += 1
        print(chars)
        return


print(Solution().compress(chars = ["a","a","b","b","c","c","c"]))