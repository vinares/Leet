class Solution:
    def findLength(self, A: list, B: list) -> int:
        def in_window(length: int, aindex: int, bindex: int) -> int:
            ret, k = 0, 0
            for i in range(length):
                if A[i + aindex] == B[i + bindex]:
                    k += 1
                    ret = max(ret, k)
                elif length - i < ret:
                    break
                else:
                    k = 0
            return ret
        a, b = len(A), len(B)
        ans = 0
        for i in range(a):
            length = min(b, a - i)
            ans = max(ans, in_window(length, i, 0))
        for i in range(b):
            length = min(a, b - i)
            ans = max(ans, in_window(length, 0, i))
        return ans


print(Solution().findLength(A=[1,2,3,2,1], B=[3,2,1,4,7]))