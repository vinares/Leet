class Solution:
    def frequencySort(self, s: str) -> str:
        import collections
        print(collections.Counter(s).most_common(1))
        return ''.join(i * j for i,j in collections.Counter(s).most_common())

case = Solution()
print(case.frequencySort('aaaAAb23Aa'))