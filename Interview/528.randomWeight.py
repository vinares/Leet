import random

class Solution:
    def __init__(self, w: list):
        self.w = []
        self.sum = sum(w)
        for i in range(len(w)):
            prob = w[i] * 10000 // self.sum
            self.w.extend([i] * prob)

    def pickIndex(self) -> int:
        return random.choice(self.w)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
w = [3,14,1,7]
ans = []
for i in range(100):
    ans.append(Solution(w).pickIndex())
print(ans)
