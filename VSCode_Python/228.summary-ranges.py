#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        res = []
        flag = True
        s, e = nums[0],  nums[0]        
        
        def cat(s, e, res):
            if s != e:
                res.append(str(s) + '->' + str(e))
            else:
                res.append(str(s))
            return res 
            
        for i in range(1, len(nums)):
            num = nums[i]
            if s == num:
                flag = False
                continue
            if e == num - 1:
                e = num
                flag = False
            else:
                res = cat(s, e, res)
                s, e = num, num

        return cat(s, e, res)
# @lc code=end

