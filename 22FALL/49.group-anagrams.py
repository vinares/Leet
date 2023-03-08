#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = defaultdict(list)
        for string in strs:
            cnt = Counter(string)
            st = ''
            for key, val in sorted(cnt.items(), key=lambda x:x[0], reverse=True):
                st += key + str(val)
            ht[st].append(string)
        return ht.values()
# @lc code=end

