class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        table = {0: 1}
        sum = 0
        ans = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in table:
                ans += table[sum - k]
            if sum in table:
                table[sum] += 1
            else:
                table[sum] = 1
        return ans
    def positiveO1(self, nums):
        ans = 0
        hashtable = collections.defaultdict(list)
        hashtable[0].append((-1, 0))
        modulo = 0
        keepsum = 0
        for i in range(len(nums)):
            if nums[i] > k: continue
            keepsum += nums[i]
            if keepsum >= k:
                keepsum %= k
                modulo += 1
            if keepsum in hashtable.keys():
                if hashtable[keepsum][-1][1] + 1 == modulo:
                    ans += 1
            hashtable[keepsum].append((i, modulo))
        return ans
