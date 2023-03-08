#
# @lc app=leetcode id=811 lang=python3
#
# [811] Subdomain Visit Count
#

# @lc code=start
from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mem = defaultdict(int)
        for string in cpdomains:
            cnt, domain = string.split()
            fracs = domain.split('.')
            cur = ''
            for i in range(len(fracs)-1, -1, -1):
                if not cur:
                    cur += fracs[i]
                else:
                    cur = fracs[i] + '.' + cur
                mem[cur] += int(cnt)
        return [str(v) + ' ' + k for k,v in mem.items()]
            

# @lc code=end

