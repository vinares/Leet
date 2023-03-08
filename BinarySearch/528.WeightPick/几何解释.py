class Solution:
    def __init__(self, w: list):
        probability = [0] * len(w)
        _sum = sum(w)
        cur = 0
        for i in range(len(w)):
            cur += w[i]
            probability[i] = cur/_sum
        self.probability = probability

    def pickIndex(self) -> int:
        import bisect, random
        return(bisect.bisect_right(self.probability, random.random()))

import time
w = [1,1,2]
obj = Solution(w)
m = [0] * len(w)
t = time.time()
for i in range(100000):
    m[obj.pickIndex()] += 1
print (time.time()-t)
print(m)
