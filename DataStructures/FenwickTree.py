class FenwickTree:
    def __init__(self, nums) -> None:
        self.n = len(nums)
        self.nums = nums
        self.fenwick_tree = [0 for _ in range(self.n+1)]
        self._build()

    def _build(self):
        for i in range(1, self.n+1):
            self.update(i, self.nums[i-1])

    def update(self, i, num):
        self.nums[i-1] = num
        while i < self.n+1:
            self.fenwick_tree[i] += num
            i += i & (-i)
        return
    
    def query(self, i):
        ans = 0
        while i > 0:
            ans += self.fenwick_tree[i]
            i -= i & (-i)
        return ans


nums = [5,2,6,1]
ft = FenwickTree(nums)
print(ft.fenwick_tree)