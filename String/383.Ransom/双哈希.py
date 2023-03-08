class Solution:
    def canConstruct(self, ransom:str,megazine:str) -> bool:
        Hash_ran, Hash_meg = {},{}
        for i in ransom:
            Hash_ran[i] = Hash_ran.get(i, 0) + 1
        for j in megazine:
            Hash_meg[j] = Hash_meg.get(j, 0) + 1
        for key in Hash_ran.keys():
            if Hash_meg[key] < Hash_ran[key]:
                return False
            else:
                return True

case = Solution()
print(case.canConstruct('lordvoldemort', 'tommarvoloriddle'))
