class Solution:
    def canJump(self, nums: list) -> bool:
        zero = dict()
        zero[-1] = 1
        if nums[0] == 0 and len(nums) > 1: return False
        for i in range(1, len(nums)):
            if nums[i]:
                continue
            if nums[i - 1] != 0:
                p = i
                zero[p] = 1
            else:
                zero[p] += 1
        for o in zero:
            if o == -1:
                continue
            cur = o - 1
            while cur >= 0:
                if nums[cur] + cur >= len(nums) - 1:
                    return True
                if nums[cur] > zero[o]:
                    break
                zero[o] += 1
                cur -= 1

            if cur in zero:
                return False

        return True

nums = [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]
print(Solution().canJump(nums))