#
# @lc app=leetcode id=481 lang=python3
#
# [481] Magical String
#

# @lc code=start
class Solution:
    def magicalString(self, n: int) -> int:
        self.ans = [1]
        one = False
        counter = 1
        index = 1

        while counter < n:
            new_element = 1 if self.ans[-1] == 2 else 2
            index += 1
            if one:
                counter += 1
                self.ans.append(new_element)
            else:
                counter += 2
                self.ans.append(new_element)
                self.ans.append(new_element)

            if self.ans[index] == 1:
                one = True
            else:
                one = False
        answer = 0
        for i in range(n):
            if self.ans[i] == 1:
                answer += 1
        return answer

# @lc code=end

