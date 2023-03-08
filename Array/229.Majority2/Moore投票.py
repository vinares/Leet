class Solution:
    def majorityElement(self, nums: list) -> int:
        ans = []
        if not nums: return ans
        cnt1, cnt2 = 0, 0
        A, B = nums[0], nums[0]
        for i, num in enumerate(nums):
            if num == A:
                cnt1 += 1
                continue
            if num == B:
                cnt2 += 1
                continue
            if cnt1 == 0:
                A = num
                cnt1 += 1
                continue
            if cnt2 == 0:
                B = num
                cnt2 += 1
                continue

            cnt1 -= 1
            cnt2 -= 1
        cnt1, cnt2 = 0, 0
        for i, num in enumerate(nums):
            if num == A: cnt1 += 1
            elif num == B: cnt2 += 1
        if cnt1 > len(nums) / 3: ans.append(A)
        if cnt2 > len(nums) / 3: ans.append(B)

        return ans


nums = [1,2]
print(Solution().majorityElement(nums))
