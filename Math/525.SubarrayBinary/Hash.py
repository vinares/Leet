class Solution:
    def findMaxLength(self, nums:list) -> int:
        n = len(nums)
        hashmap = dict()
        count = 0
        hashmap[0] = [0]
        for i in range(n):
            if nums[i]:
                count += 1
            else:
                count -= 1
            if count not in hashmap:
                hashmap[count] = [i + 1]
            else:
                hashmap[count].append(i + 1)
        result = 0
        print(hashmap)
        for p in hashmap:
            distance = hashmap[p][-1] - hashmap[p][0]
            if distance > result:
                result = distance
        return result






case = Solution()
nums = [0,1,0]
print(case.findMaxLength(nums))