class Solution:
    def nextGreaterElement(self, n: int) -> int:
        bits = []
        tmp = n
        while tmp:
            bits.append(tmp % 10)
            tmp //= 10
        for i in range(len(bits) - 1):
            if bits[i] > bits[i + 1]:
                break
        for j in range(i):
            if bits[j] > bits[i + 1]:
                bits[j], bits[i] = bits[i], bits[j]
                break

        
print(Solution().nextGreaterElement(21))