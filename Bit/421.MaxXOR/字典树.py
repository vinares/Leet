class Solution:
    def findMaximumXOR(self, nums: list) -> int:
        L = len(bin(max(nums))) - 2
        nums = [[(x >> i) & 1 for i in range(L)[:: -1]]for x in nums]
        maxor = 0
        trie = {}

        for num in nums:
            cur = 0
            cur_node = trie
            node = trie
            curxor = 0
            for bit in num:
                if bit not in node:
                    node[bit] = {}
                node = node[bit]

                toggled = 1 - bit
                if toggled in cur_node:
                    cur_node = cur_node[toggled]
                    curxor = curxor << 1 | 1
                else:
                    curxor = curxor << 1
                    cur_node = cur_node[bit]
            maxor = max(maxor, curxor)
        return  maxor


print(Solution().findMaximumXOR(nums=[3,10,5,25,2,8]))