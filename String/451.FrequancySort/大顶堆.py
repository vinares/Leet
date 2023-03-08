class Solution:
    def frequencySort(self, s: str) -> str:
        import collections, heapq
        hashtable = collections.defaultdict(int)
        for x in s:
            hashtable[x] += 1
        heap = []
        heapq.heapify(heap)
        for i in hashtable:
            for j in range(hashtable[i]):
                heapq.heappush(heap, (-hashtable[i], i))
        return ''.join(heapq.heappop(heap)[1] for _ in range(len(heap)))


case = Solution()
print(case.frequencySort("fuuuuckkk"))