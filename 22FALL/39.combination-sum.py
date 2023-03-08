#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def backtrack(i, tmp, cur):
            if cur == target:
                ans.append(tmp)
                return
            for j in range(i, len(candidates)):
                if candidates[j] > target-cur:
                    break
                backtrack(j, tmp+[candidates[j]], cur+candidates[j])
            return
        backtrack(0, [], 0)
        return ans

# @lc code=end

