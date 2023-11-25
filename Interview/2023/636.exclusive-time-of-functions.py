#
# @lc app=leetcode id=636 lang=python3
#
# [636] Exclusive Time of Functions
#

# @lc code=start
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0 for _ in range(n)]
        stack = []
        start_time = 0
        for log in logs:
            fid, action, ts = log.split(':')
            fid, ts = int(fid), int(ts)
            if action == 'start':
                if stack:
                    prev_fid = stack[-1]
                    res[prev_fid] += ts - start_time
                stack.append(fid)
                start_time = ts
            else:
                stack.pop()
                res[fid] += ts - start_time + 1
                start_time = ts + 1
                    
        return res


# @lc code=end

