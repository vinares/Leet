class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        if n == 0: return 1
        ans = 1

        if n > 0:
            cal = x
        else:
            cal = 1 / x
            n = - n

        cals = [cal]
        n_bit = bin(n)
        for i in range(1, len(n_bit)- 2):
            cals.append(cals[-1] * cals[-1])
        for i in range(2, len(n_bit)):
            if n_bit[i] == '1':
                ans *= cals[len(cals) - i + 1]
            elif n_bit[i] == '0':
                continue

        return ans


x = 10
n = -5
print(Solution().myPow(x, n))