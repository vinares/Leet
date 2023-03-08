class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        string = bin(n)
        for i in range(2, len(string)):
            if string[i] == '1':
                count += 1
        return count

print(Solution().hammingWeight(n=0b00000000000000000000000010000000))