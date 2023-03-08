import bisect
class Solution:
    def minOperations(self, target: list, arr: list) -> int:
        order = []
        target_dict = dict({tar:i for i, tar in enumerate(target)})
        for x in arr:
            if x in target_dict:
                index = target_dict[x]
                i = bisect.bisect_left(order, index)
                if len(order) == i:
                    order.append(0)
                order[i] = index

        return len(target) - len(order)

target = [16,7,20,11,15,13,10,14,6,8]
arr = [11,14,15,7,5,5,6,10,11,6]
print(Solution().minOperations(target,arr))