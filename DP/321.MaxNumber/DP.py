class Solution:
    def maxNumber(self, nums1: list, nums2: list, k: int) -> list:
        m, n = len(nums1), len(nums2)
        N = m + n
        if N < k: return 0

        def maxsequence(nums: list, x: int) -> list:
            length_of_nums = len(nums)
            if not x: return []
            if x == length_of_nums: return nums
            max_sequence = []
            for i in range(length_of_nums):
                while max_sequence and nums[i] > max_sequence[-1] and x - len(max_sequence) < length_of_nums - i:
                    max_sequence.pop()
                if x - len(max_sequence) == length_of_nums - i:
                    max_sequence += nums[i::]
                    break
                if x > len(max_sequence):
                    max_sequence.append(nums[i])
            return max_sequence

        def greater(num1: list, i: int, num2: list, j: int) -> bool:
            m, n = len(num1), len(num2)
            if not num2:
                return True
            elif not num1:
                return False
            while i != m and j != n and num1[i] == num2[j]:
                i += 1
                j += 1
            return j == n or (i < m and num1[i] > num2[j])

        def merge(num1:list, num2: list):
            x, y = len(num1), len(num2)
            if not x: return num2
            if not y: return num1
            ans = []
            id1, id2 = 0, 0
            for _ in range(x + y):
                if greater(num1,id1, num2,id2):
                    ans.append(num1[id1])
                    id1 += 1
                else:
                    ans.append(num2[id2])
                    id2 += 1
            return ans

        start, end = max(0, k - n), min(k, m)
        ans = []
        for index in range(start, end + 1):
            num1 = maxsequence(nums1, index)
            num2 = maxsequence(nums2, k - index)
            ans.append(merge(num1, num2))
        return max(ans)

print(Solution().maxNumber(nums1=[6,6,8], nums2= [5,0,9], k=3))