class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jeweldict = set(jewels)
        return sum(s in jeweldict for s in stones)



print(Solution().numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))