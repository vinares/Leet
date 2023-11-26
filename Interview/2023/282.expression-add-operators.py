#
# @lc app=leetcode id=282 lang=python3
#
# [282] Expression Add Operators
#

# @lc code=start
from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []

        def bt(unprocessed, expression, prev_term, val):
            if not unprocessed and val == target:
                ans.append(expression)
            
            for i in range(1, len(unprocessed)+1):
                cur_number = unprocessed[:i]
                next_unprocessed = unprocessed[i:]
                if len(cur_number) > 1 and cur_number[0] == '0':
                    break
                if len(expression) == 0:
                    bt(next_unprocessed, cur_number, int(cur_number), int(cur_number))
                    continue
                bt(next_unprocessed, expression + '+' + cur_number, int(cur_number), val+int(cur_number))
                bt(next_unprocessed, expression + '-' + cur_number, -int(cur_number), val-int(cur_number))
                bt(next_unprocessed, expression + '*' + cur_number, prev_term * int(cur_number), val - prev_term + (prev_term * int(cur_number)))

        bt(num, '', 0, 0)
        return ans
# @lc code=end

