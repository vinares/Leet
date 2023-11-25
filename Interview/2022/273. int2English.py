class Solution:
    def numberToWords(self, num: int) -> str:
        vocab1 = ['O','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
        vocab2 = ['Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
        vocab3 = ['Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninty']
        vocab4 = 'hundred'

        a = num // 100
        ans = ''
        if a:
            ans += vocab1[a] + ' ' + vocab4
        b = num - a * 100
        if 10 < b < 20:
            ans += + ' And ' + vocab2[b%10 - 1]
        elif b > 10 and not b % 10:
            ans += ' And ' + vocab3[b // 10 - 1]
        elif b > 20:
            ans +=  ' And ' + vocab3[b // 10 - 1] + '-' + vocab1[b % 10]
        else:
            ans += ' ' + vocab1[0] + ' ' + vocab1[b]

        return ans


num = 903
print(Solution().numberToWords(num))