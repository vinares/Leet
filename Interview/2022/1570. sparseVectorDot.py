
class SparseVector:
    def __init__(self, nums: list[int]):
        self.dic = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.dic[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        if len(self.dic) > len(vec.dic):
            for j, n in vec.dic.items():
                if j in self.dic:
                    res += self.dic[j]* n
        else:
            for i, n in self.dic.items():
                if i in vec.dic:
                    res += n*vec.dic[i]
        return res

nums1 = [1,0,0,2,3]
nums2 = [0,3,0,4,0]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
print(v1.dotProduct(v2))