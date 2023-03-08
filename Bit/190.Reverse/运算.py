class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(31):
            ans *= 2
            ans += n % 2
            n //= 2
        ans *= 2
        return ans




print(Solution().reverseBits(n=0b00000010100101000001111010011100))