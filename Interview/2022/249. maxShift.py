class Solution:
    def groupStrings(self, strings: list) -> list:
        #TC: O(len(strings)*M) M: maximum length of elements in strings
        #SC: Maximum (O(len(strings)*len(strings)*M))
        #Use tuple to represent string pattern
        #Same string with the same pattern in the Dict
        Dict = {}
        for ele in strings:
            pattern = ()
            for i in range(len(ele)-1):
                diff = (ord(ele[i]) - ord(ele[i+1])) % 26
                pattern = pattern + (diff, )

            if pattern not in Dict:
                Dict[pattern] = [ele]
            else:
                Dict[pattern].append(ele)

        res = []
        for key in Dict:
            res.append(Dict[key])

        return res

print(Solution().groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))