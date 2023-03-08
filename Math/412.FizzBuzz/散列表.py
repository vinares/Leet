class Solution:
    def fizzBuzz(self, n: int) ->list:
        result = []
        hashmap = {3: 'Fizz', 5: 'Buzz'}
        for i in range(1,n + 1):
            ans_str = ''
            for key in hashmap:
                if not i % key:
                    ans_str += hashmap[key]
            if not ans_str:
                ans_str = str(i)
            result.append(ans_str)
        return result

case = Solution()
print(case.fizzBuzz(15))
