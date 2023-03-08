from math import ceil, log2
class SegmentTree:
    def __init__(self, nums) -> None:
        self.arr = nums
        self.N = len(self.arr)
        self.n = 2 ** (ceil(log2(self.N))+1) - 1
        self.segment_tree = [None for _ in range(self.n)]
        self._build(0, self.N-1, 0)

    def _build(self, start, end, i):
        if start == end:
            self.segment_tree[i] = self.arr[start]
            return self.arr[start]
        mid = start + (end-start)//2
        left, right = self._build(start, mid, i*2+1), self._build(mid+1, end, i*2+2)
        self.segment_tree[i] = left+right
        return self.segment_tree[i]
    
    def query(self, start, end):
        return self._query(start, end, 0, 0, self.N-1)

    def _query(self, start, end, tree_index, left, right):
        if start > end:
            return 0
        if start==left and end==right:
            return self.segment_tree[tree_index]
        mid = left + (right-left)//2
        if mid < start:
            return self._query(start, end, tree_index*2+2, mid+1, right)
        elif mid >= end:
            return self._query(start, end, tree_index*2+1, left, mid)
        else:
            l = self._query(start, mid, tree_index*2+1, left, mid)
            r = self._query(mid+1, end, tree_index*2+2, mid+1, right)
            return l+r
    
    def update(self, i, num):
        difference = num - self.arr[i]
        if difference == 0:
            return        
        self.arr[i] = num
        self._update(difference, i, 0, 0, self.N-1)
    
    def _update(self, difference, i, tree_index, left, right):
        self.segment_tree[tree_index] += difference
        mid = left + (right-left)//2
        if left==right:
            return
        elif i<=mid:
            self._update(difference, i, tree_index*2+1, left, mid)
        elif i>mid:
            self._update(difference, i, tree_index*2+2, mid+1, right)
        return

nums = [5,2,6,1]
st = SegmentTree(nums)
print(st.segment_tree)
st.update(1, 3)
print(st.segment_tree)