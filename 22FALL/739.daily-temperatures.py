#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        monotonous_stack = []
        for i in range(n-1, -1, -1):
            while monotonous_stack and monotonous_stack[-1][0] <= temperatures[i]:
                monotonous_stack.pop()
            if monotonous_stack:
                answer[i] = monotonous_stack[-1][1] - i
            monotonous_stack.append((temperatures[i], i))
        return answer
# @lc code=end

