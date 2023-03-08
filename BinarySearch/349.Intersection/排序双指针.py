class Solution:
    def intersection(self, nums1: list, nums2: list) -> list:
        p1, p2= 0, 0
        res = set()
        l1 = sorted(nums1)
        l2 = sorted(nums2)
        while p1 < len(l1) and p2 < len(l2):
            if l1[p1] < l2[p2]:
                p1 += 1
            elif l1[p1] == l2[p2]:
                res.add(l1[p1])
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        return list(res)
case = Solution()
print(case.intersection([1,1,1,1,2,3,4,5],[4,4,5,5,5,6,1]))