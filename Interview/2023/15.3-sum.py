#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        Z, p, n = [], [], []
        for num in nums:
            if num == 0:
                Z.append(num)
            elif num < 0:
                n.append(num)
            else:
                p.append(num)
        res = set()
        P = set(p)
        N = set(n)

        if len(Z) >= 3:
            res.add((0, 0, 0))
        if Z:
            for num in P:
                if -num in N:
                    res.add((-num, 0, num))
        nn = len(n)
        for i in range(nn):
            for j in range(i+1, nn):
                N_sum = n[i] + n[j]
                if -N_sum in P:
                    res.add(tuple(sorted([n[i], n[j], -N_sum])))
        pp = len(p)
        for i in range(pp):
            for j in range(i+1, pp):
                P_sum = p[i] + p[j]
                if -P_sum in N:
                    res.add(tuple(sorted([-P_sum, p[i], p[j]])))
        return res

# @lc code=end

