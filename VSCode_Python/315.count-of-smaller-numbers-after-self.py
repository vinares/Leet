#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#

# @lc code=start
#using fenwick tree or BIT
class FenwickTree:
    def __init__(self, n) -> None:
        self.n = n
        self.fenwick_tree = [0] * (n+1)

    def update(self, i):
        while i < self.n+1:
            self.fenwick_tree[i] += 1
            i += i & (-i)
        return
    
    def query(self, i):
        ans = 0
        while i > 0:
            ans += self.fenwick_tree[i]
            i -= i & (-i)
        return ans
        
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        bucket = {}
        n = len(nums)
        ft = FenwickTree(n)
        for num in sorted(nums):
            if num in bucket:continue
            bucket[num] = len(bucket)+1
        for i in range(n-1, -1, -1):
            ft.update(bucket[nums[i]])
            nums[i] = ft.query(bucket[nums[i]]-1)
        return nums


# @lc code=end


