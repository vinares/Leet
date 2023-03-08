class Solution:
    def countAndSay(self, n: int) -> str:
        ans = str(1)
        def Count(num: str) :
            ret = ''
            cur, cnt = num[0], 0
            for x in num:
                if x == cur:
                    cnt += 1
                else:
                    ret += (str(cnt) + cur)
                    cur = x
                    cnt = 1
            ret += (str(cnt) + cur)
            return ret

        for i in range(1, n):
            ans = Count(ans)
        return ans

for i in range(1, 21):
    print(i, '     ', Solution().countAndSay(i))