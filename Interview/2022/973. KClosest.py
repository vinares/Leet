import random
class Solution:
    def kClosest(self, points: list, k: int) -> list:

        def random_select(left: int, right: int, k: int):
            if left == right:return
            pivot_id = random.randint(left, right)
            pivot = points[pivot_id][0] ** 2 + points[pivot_id][1] ** 2
            points[right], points[pivot_id] = points[pivot_id], points[right]
            i = left - 1
            for j in range(left, right):
                if points[j][0] ** 2 + points[j][1] ** 2 <= pivot:
                    i += 1
                    points[i], points[j] = points[j], points[i]
            i += 1
            points[i], points[right] = points[right], points[i]
            # [left, i-1] 都小于等于 pivot, [i+1, right] 都大于 pivot
            if k < i - left + 1:
                random_select(left, i - 1, k)
            elif k > i - left + 1:
                random_select(i + 1, right, k - (i - left + 1))

        n = len(points)
        random_select(0, n - 1, k)
        return points[:k]


points = [[3,3],[5,-1],[-2,4]]
k = 2
for i in range(10):
    print(Solution().kClosest(points,k))