class Solution:
    def reverseBits(self, n: int) -> int:
        nums = [0] * 32
        i = 31
        while n:
            nums[i] = n % 2
            i -= 1
            n //= 2
        for i in range(16):
            nums[i], nums[31 - i] = nums[31 - i], nums[i]
        ans = 0
        for i in range(32):
            ans = ans * 2 + nums[i]
        return ans






print(Solution().reverseBits(n=0b00000010100101000001111010011100))