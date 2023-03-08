class Solution:
    def canConstruct(self, ransom:str,megazine:str) -> bool:
        for i in ransom:
            if i in megazine:
                megazine.replace(i,'')
            else:
                return False
        return True

case = Solution()
print(case.canConstruct('lordvoldemort', 'tommarvoloriddle'))
