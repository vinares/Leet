import math
import random
import numpy as np
import matplotlib.pyplot as plt

def cryp(nums, s):
    m, n = nums.shape
    p1, p2 = m // 10, n // 10
    average = ord(s)
    fill = np.random.normal(average, 0.1, p1 * p2)
    row, col = [10 * i for i in range(p1)], [10 * j for j in range(p2)]

    k = 0
    for i in row:
        for j in col:
            if fill[k] - np.floor(fill[k]) < 0.5:
                fill[k] = np.floor(fill[k])
            else:
                fill[k] = np.ceil(fill[k])
            nums[i][j] = int(fill[k])
            k += 1
    return

def decryp(nums):
    m, n = nums.shape
    p1, p2 = m // 10, n // 10
    row, col = [10 * i for i in range(p1)], [10 * j for j in range(p2)]

    fill = []
    for i in row:
        for j in col:
            fill.append(nums[i][j])
    k = sum(fill) / (p1 * p2)
    ans = sum(fill) // (p1 * p2)
    if abs(ans - k) >= 0.5:
        ans =  int(np.floor(k))
    else:
        ans =  int(np.ceil(k))
    return chr(ans)
cnt = 0
for _ in range(100):
    nums = np.random.randint(low=0, high=255, size=(120, 1024))
    s = chr(random.randint(0, 255))
    cryp(nums, s)
    #plt.imshow(nums,cmap='gray')
    #plt.show()
    t = decryp(nums)
    if s != t:
        cnt += 1
print(cnt)