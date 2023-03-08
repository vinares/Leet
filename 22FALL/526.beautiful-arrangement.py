#
# @lc app=leetcode id=526 lang=python3
#
# [526] Beautiful Arrangement
#

# @lc code=start
class Solution:
    def countArrangement(self, n: int) -> int:
        self.ans = 0
        available = set(range(1,n+1))

        def backtrack(pos, availables):
            if pos > n:
                self.ans += 1
                return
            for num in list(availables):
                if pos % num == 0 or num % pos == 0:
                    availables.remove(num)
                    backtrack(pos+1, availables)
                    availables.add(num)
                
        backtrack(1, available)
        return self.ans
        
# @lc code=end

