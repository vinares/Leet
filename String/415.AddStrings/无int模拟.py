class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        res = ""
        carry = 0
        while i >= 0 or j >= 0:
            n1 = ord(num1[i]) if i >= 0 else 48    ##ord('0') = 48
            n2 = ord(num2[j]) if j >= 0 else 48
            temp = n1 + n2 - 2 * ord('0') + carry
            cur = temp % 10
            carry = temp // 10
            res = chr(cur + 48) + res
            i -= 1
            j -= 1
        return '1' + res if carry != 0 else res

case = Solution()
print(case.addStrings('345','12345'))
