#
# @lc app=leetcode id=2179 lang=python3
#
# [2179] Count Good Triplets in an Array
#

# @lc code=start
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos2 = dict((nums2[i], i) for i in range(n))
        f = [pos2[nums1[i]] for i in range(n)] # index in nums2

        def add(x):
            while x<=n:
                t[x] += 1
                x += (x & (-x))

        def query(x):
            res = 0
            while x:
                res += t[x]
                x -= (x & (-x))
            return res
    
        left, right = [0] * n, [0] * n

        t = [0] * (n+1)
        for i in range(n):
            left[i] = query(f[i])
            add(f[i]+1)
            print(nums1[i], f[i], t)
            
        t = [0] * (n+1)
        for i in range(n-1, -1, -1):
            right[i] = n - 1 - i - query(f[i]+1)
            add(f[i]+1)

        res = 0
        for i in range(n):
            res += left[i] * right[i]
        return res
# @lc code=end

