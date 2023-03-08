class Solution:
    def findLength(self, A: list, B: list) -> int:
        a, b = len(A), len(B)
        if not a or not b:
            return 0
        base, mod = 113, 10 ** 9 + 9

        def hashFind(length: int) -> bool:
            hashA = 0
            for i in range(length):
                hashA = (hashA * base + A[i]) % mod
            bucketA = {hashA}
            mult = pow(base, length - 1, mod)
            for i in range(length, len(A)):
                hashA = ((hashA - A[i - length] * mult) * base + A[i]) % mod
                bucketA.add(hashA)
            hashB = 0
            print(bucketA)
            for i in range(length):
                hashB = (hashB * base + B[i]) % mod
            if hashB in bucketA:
                return True
            for i in range(length, b):
                hashB = ((hashB - B[i - length] * mult) * base + B[i]) % mod
                if hashB in bucketA:
                    return True

            return False

        left, ans, right = 0, 0, min(a, b)
        while left <= right:
            mid = left + (right - left) // 2
            if hashFind(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans



print(Solution().findLength(A=[0,0,0,0,1], B=[1,0,0,0,0]))