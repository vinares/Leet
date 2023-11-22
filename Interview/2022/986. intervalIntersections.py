class Solution:
    def intervalIntersection(self, firstList: list, secondList: list) ->list:
        if not firstList or not secondList : return []
        ans = []
        i, j = 0, 0
        start, end = 0, 0
        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            if start <= end:
                ans.append([start, end])
            if end == firstList[i][1]: i += 1
            elif end == secondList[j][1]: j+= 1
        return ans
    def cover(self, firstList: list, secondList: list) -> bool:
        if not firstList and secondList : return False
        if not secondList: return True

        i, j = 0, 0
        start, end, mid = 0, 0, 0
        while i < len(firstList) and j < len(secondList):
            start, end = max(secondList[j][0], start), secondList[j][1]

            if start > firstList[i][1]: i += 1
            elif end > firstList[i][1]:
                start = firstList[i][1] + 1
                i += 1
            elif end < firstList[i][0]: return False
            else:
                j += 1
        if j < len(secondList): return False
        return True
    def merge(self, firstList, secondList):
        if not firstList: return secondList
        if not secondList: return firstList

        ans = []
        i,j = 0, 0
        while i < len(firstList) and j < len(secondList):
            if i < len(firstList) and j < len(secondList):
                start = min(firstList[i][0], secondList[j][0])
                end = max(firstList[i][1], secondList[j][1])
            elif i < len(firstList):
                start = firstList[i][0]
                end = firstList[i][1]
            else:
                start = secondList[j][0]
                end = secondList[j][1]
            i += 1
            j += 1
            if not ans:
                ans.append([start, end])
            else:
                if ans[-1][1] < start - 1:
                    ans.append([start, end])
                else:
                    ans[-1][1] = max(ans[-1][1], end)
        return ans


firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
print(Solution().intervalIntersection(firstList, secondList))

firstList = [[1, 5], [8, 12], [15, 24], [25, 26]]
secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
print(Solution().cover(firstList, secondList))

firstList = [[1,5],[10,14],[16,18]]
secondList = [[2,6],[8,10],[11,20]]
print(Solution().merge(firstList, secondList))