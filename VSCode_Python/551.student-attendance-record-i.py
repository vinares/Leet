#
# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        cnt = 0
        for c in s:
            if c=='A': 
                cnt +=1
            if cnt > 1:
                return False 
        return 'LLL' not in s
# @lc code=end

