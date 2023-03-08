#
# @lc app=leetcode id=321 lang=python3
#
# [321] Create Maximum Number
#

# @lc code=start
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        def merge(a, b):
            ans = []
            while a or b:
                bigger = a if a>b else b
                ans.append(bigger[0])
                bigger.pop(0)
            return ans

        def largest(nums, x):
            monotonous_stack = []
            remain = len(nums) - x
            for num in nums:
                while monotonous_stack and monotonous_stack[-1] < num and x:
                    monotonous_stack.pop()
                    x -= 1
                monotonous_stack.append(num)
            return monotonous_stack[:remain]    
        
        def evaluate(nums):
            ans = 0
            for num in nums:
                ans *= 10
                ans += num
            return ans


        m, n = len(nums1), len(nums2)
        res = 0
        cur_list = []
        k = m + n - k

        for i in range(min(m, k)+1):
            j = k-i
            if j > n:
                continue
            a_largest = largest(nums1, i)
            b_largest = largest(nums2, j)
            i_largest = merge(a_largest, b_largest)
            cur_val = evaluate(i_largest)
            if cur_val > res:
                cur_list = i_largest
                res = cur_val
        return cur_list



        


# @lc code=end

