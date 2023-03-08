class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        sj=0
        for j in J:
            sj|=1<<(ord(j)-65)
        print(bin(sj))
        for s in S:
            print(bin(1 << ord(s) - 65))
        return  sum(((1<<(ord(s)-65))&sj)!=0 for s in  S)

print(Solution().numJewelsInStones(J= "aAz", S = "aAAbbbbz"))