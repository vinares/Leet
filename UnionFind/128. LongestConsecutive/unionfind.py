from collections import Counter
class Solution:
    def __init__(self):
        self.uf = dict()

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            root = min(ra, rb)
            self.uf[a] = root
            self.uf[b] = root

    def find(self, a):
        if self.uf[a] != a:
            self.uf[a] = self.find(self.uf[a])
        return self.uf[a]

    def longestConsecutive(self, nums: list) -> int:
        n = len(nums)
        if n < 2:
            return n
        for num in nums:
            self.uf[num] = num
        for num in nums:
            if num + 1 in self.uf:
                self.uf[num + 1] = num
                self.union(num, num + 1)
            if num - 1 in self.uf:
                self.uf[num] = num - 1
                self.union(num, num -1)
        for num in nums:
            self.find(num)
        cnt = Counter(self.uf.values())
        return max(cnt.values())

nums = [0,3,7,2,5,8,4,6,0,1]
print(Solution().longestConsecutive(nums))