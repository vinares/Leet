

from heapq import heapify, heappop, heappushpop, heappush


class ComplementaryPairs:
    def cp(self, stringData):
        hm = {}
        ans = 0
        for str in stringData:
            mask = 0
            for c in str:
                mask ^= 1 << ord(c)-ord('a')
            if mask not in hm:
                hm[mask] = 1
            else:
                ans += hm[mask]
                hm[mask] += 1
        for mask in hm:
            mask = bin(mask)[2:]
            for i in range(len(mask)):
                tmp = int(mask[:i] + '0' + mask[i+1:], 2)
                if mask[i] == '1' and tmp in hm:
                    ans += hm[tmp]
        return ans


stringData = ['ball', 'all', 'call', 'bal']
print(ComplementaryPairs().cp(stringData))


class BinaryGame:
    def goodString(self, min_length, max_length, one_group, zero_group):
        dp = [0 for _ in range(max_length+1)]
        start = min(zero_group, one_group)
        dp[0] = 1
        for i in range(max_length+1):
            if i-one_group >= 0:
                dp[i] += dp[i-one_group]
            if i-zero_group >= 0:
                dp[i] += dp[i-zero_group]
        return sum(dp[min_length:max_length+1])


print(BinaryGame().goodString(1, 3, 2, 1))


class ArrayGenerator:
    def findSmallestArray(self, arr, l, r):
        diff = 0
        brr = []
        for a in arr:
            b = a + diff
            while b < l or b < a or (brr and b < brr[-1]):
                diff += 1
                b = a + diff
            if b > r:
                return [-1]
            brr.append(b)
            diff += 1
        return brr


print(ArrayGenerator().findSmallestArray([1, 2, 1, 2], 1, 10))


class MaxScore:
    def maxScore(self, n, arr, k):
        h = []
        heapify(h)
        for i in range(n):
            if len(h) == k:
                heappushpop(h, arr[i])
            else:
                heappush(h, arr[i])
        return sum(h)


print(MaxScore().maxScore(6, [4, 6, -10, -1, 10, -20], 4))


class BankTransaction:
    def maxtxn(self, txns):
        n = len(txns)
        dp = [0 for _ in range(n+1)]
        balance, ans = 0, 0
        while balance >= 0:
            new_dp = [float('-inf') for i in range(n+1)]
            balance = float('-inf')
            for i in range(ans, n+1):
                for j in range(ans, i):
                    new_dp[i] = max(new_dp[i], dp[j]+txns[i-1])
                balance = max(balance, new_dp[i])
            if balance >= 0:
                ans += 1
            dp = new_dp
        return ans


print(BankTransaction().maxtxn([3, 2, -5, -6, -1, 4]))


class FindingIntegers:
    def find(self, n, k, arr):
        heap = []
        for i in range(k):
            heappush(heap, arr[i])
        ans = [heap[0]]
        for i in range(k, n):
            heappushpop(heap, arr[i])
            ans.append(heap[0])
        return ans


print(FindingIntegers().find(4, 2, [4, 2, 1, 3]))


class MinHealth:
    def minHealth(self, initial_players, new_players, rank):
        self.heap = []
        ans = 0
        for player in initial_players:
            self.push(self.heap, player, rank)
        ans += self.heap[0]
        for player in new_players:
            self.push(self.heap, player, rank)
            ans += self.heap[0]
        return ans

    def push(self, heap, player, rank):
        if len(self.heap) == rank:
            heappushpop(self.heap, player)
        else:
            heappush(self.heap, player)
        return


print(MinHealth().minHealth([1, 2], [3, 4], 2))


class EvenTag:
    def evenTag(self, arr):
        min_odd, ans = 0, 0
        for num in arr:
            if num > 0:
                if num % 2:
                    min_odd = min(min_odd, num)
                ans += num
        if ans % 2:
            ans -= num
        return ans


print(EvenTag().evenTag([2, 3, 6, -5, 10, 1, 1]))

class DataUpdate:
    def data(self, data, updates):
        n = len(data)
        counter = [0 for _ in range(n+1)]
        for l, r in updates:
            counter[l-1] += 1
            counter[r] -= 1
        cur = 0
        for i in range(n):
            cur += counter[i]
            data[i] *= (-1) ** cur
        return data

print(DataUpdate().data([1,-4,-5,2], [[2,4], [1,2]]))

class EfficientTeam:
    def et(self, skill):
        n = len(skill)
        total = sum(skill)
        if n%2 or total % (n//2):
            return -1
        group_sum = total // (n//2)
        return sum([x*(group_sum-x) for x in skill]) // 2

skill = [1,2,3,2,2,3,2,3,1,1]
print(EfficientTeam().et(skill))