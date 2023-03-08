class Solution:
    def frequencySort(self, s: str) -> str:
        # 桶排序
        import collections
        hashtable = collections.defaultdict(int)
        for x in s:
            hashtable[x] += 1

        buckets = [[] for _ in range(len(s))]
        for ch in hashtable:
            buckets[hashtable[ch]].extend( ch * hashtable[ch])
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            if buckets[i]:
                res.extend(buckets[i])
        return ''.join(res)



case = Solution()
print(case.frequencySort("fuuuuckkk"))