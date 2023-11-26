#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#

# @lc code=start
from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = {}
        n = len(accounts)
        for i in range(n):
            uf[i] = i
        
        def find(x):
            px = uf[x]
            while px != uf[px]:
                px = find(px)
            return px
    
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                uf[px] = py
            
        email_to_index = {}
        for i in range(n):
            for email in accounts[i][1:]:
                if email in email_to_index:
                    union(i, uf[email_to_index[email]])
                email_to_index[email] = i
        
        root_to_emails = defaultdict(list)
        for i in range(n):
            root_to_emails[find(i)].append(i)
        
        ans = []
        for root, subs in root_to_emails.items():
            name = accounts[root][0]
            emails = set()
            for sub in subs:
                emails.update(accounts[sub][1:])
            ans.append([name] + sorted(emails))
        return ans
            


# @lc code=end

