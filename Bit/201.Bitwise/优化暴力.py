class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m <= n / 2:
            return 0
        ans = [bin(m)[i] for i in  range(2, len(bin(m)))]
        one = set()
        for i in range(len(ans)):
            if ans[i] == '1':
                one.add(i - len(ans))
        if not one:
            return 0

        for x in one:
            for i in range(m + 1, n + 1):
                tmp = bin(i)
                if tmp[x] == '0':
                    ans[x] ='0'
                    break
        ret = '0b'
        for i in range(len(ans)):
            ret += ans[i]
        return int(ret, 2)



print(Solution().rangeBitwiseAnd(600000000, 2147483645))