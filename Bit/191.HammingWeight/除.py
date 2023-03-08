class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            if n % 2:
                count += 1
            n //= 2
        return count

print(Solution().hammingWeight(n=0b00000000000000000000000010000000))