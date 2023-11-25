class Solution:
    def depthSum(self, nestedList: list) -> int:
        def dfs(nestedList, depth):
            if not nestedList: return 0
            ans = 0
            for i in range(len(nestedList)):
                if type(nestedList[i]) == int:
                    ans += nestedList[i] * depth
                else:
                    ans += dfs(nestedList[i], depth + 1)
            return ans

        return dfs(nestedList, 1)

nums = [[1,1],2,[1,1]]
print(Solution().depthSum(nums))