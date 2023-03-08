#
# @lc app=leetcode id=801 lang=python3
#
# [801] Minimum Swaps To Make Sequences Increasing
#

# @lc code=start
class Solution:
    def minSwap(self, A, B):
        n = len(A)
        prevNotSwap = 0
        prevSwap = 1
        for i in range(1, n):
            areBothSelfIncreasing = A[i - 1] < A[i] and B[i - 1] < B[i] 
            areInterchangeIncreasing = A[i - 1] < B[i] and B[i - 1] < A[i]
            if areBothSelfIncreasing and areInterchangeIncreasing:
                newPrevNotSwap = min(prevNotSwap, prevSwap)
                prevSwap = min(prevNotSwap, prevSwap) + 1
                prevNotSwap = newPrevNotSwap
            elif areBothSelfIncreasing:
                prevSwap += 1 
            else: # if areInterchangeIncreasing:
                newPrevNotSwap = prevSwap
                prevSwap = prevNotSwap + 1
                prevNotSwap = newPrevNotSwap
        return min(prevNotSwap, prevSwap)
# @lc code=end

