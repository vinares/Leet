import collections
import copy


class Solution:
    def depthSum(self, nestedList: list) -> int:
        ans = 0
        thislevel = nestedList
        while thislevel:
            thislevelsum = 0
            flag = False
            nextlevel = []
            for i in range(len(thislevel)):
                if type(thislevel[i]) == int:
                    thislevelsum += thislevel[i]

                else:
                    nextlevel.extend(thislevel[i])
            ans += thislevelsum
            if not nextlevel: break
            thislevel = nextlevel + [thislevelsum]
        return ans


nums = [[1,1],2,[1,1]]
print(Solution().depthSum(nums))