class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        string = hex(n)
        one = {'1', '2', '4', '8'}
        two = {'3', '5', '6', '9', 'a', 'c'}
        three = {'7', 'b', 'd', 'e'}
        for i in range(2, len(string)):
            if string[i] in two:
                count += 2
            elif string[i] in one:
                count += 1
            elif string[i] in three:
                count += 3
            elif string[i] == 'f':
                count += 4
            else:
                continue
        return count

print(Solution().hammingWeight(n=0b00000000000000000000000000001011))