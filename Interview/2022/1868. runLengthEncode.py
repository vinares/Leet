class Solution:
    def product(self, encode1, encode2):
        n = 0
        for i in range(len(encode1)):
            n += encode1[i][1]
        ans = []
        i, j = 0, 0
        while i < len(encode1) and j < len(encode2):
            cur, cnt = 0, 0
            if encode1[i][1] < encode2[j][1]:
                cur, cnt = encode1[i][0] * encode2[j][0], encode1[i][1]
                i += 1
                encode2[j][1] -= cnt

            elif encode1[i][1] == encode2[j][1]:
                cur, cnt = encode1[i][0] * encode2[j][0], encode1[i][1]
                i += 1
                j += 1
            else:
                cur, cnt = encode2[j][0] * encode1[i][0], encode2[j][1]
                j += 1
                encode1[i][1] -= cnt
            if ans and ans[-1][0] == cur:
                ans[-1][1] += cnt
            else:
                ans.append([cur, cnt])
        return ans

print(Solution().product(encode1 =[[1,3],[2,3]], encode2 = [[6,3],[3,3]]))