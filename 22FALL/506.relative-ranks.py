#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        cool_dict = {n-1:"Gold Medal", n-2:"Silver Medal", n-3: "Bronze Medal"}
        sortedscore = [sorted(score).index(s) for s in score]
        answer = []
        
        for s in sortedscore:
            answer.append(cool_dict.get(s, str(n-s)))
        return answer
# @lc code=end

