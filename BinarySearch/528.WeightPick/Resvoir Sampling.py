class Solution:
    def __init__(self, w: list):
        self.w = w

    def pickIndex(self) -> int:
        import random
        _i, _v = 0,  float('-inf')
        for i, w in enumerate(self.w):
            v = random.random()**(1/w)
            if v > _v:
                _i, _v = i, v
        return _i

import time
w = [1,1,2]
obj = Solution(w)
m = [0] * len(w)
t = time.time()
for i in range(100000):
    m[obj.pickIndex()] += 1
print (time.time()-t)
print(m)
