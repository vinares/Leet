import numpy as np
def judge(nums):
    x, y = dict(), dict()
    for i in range(len(nums)):
        x[nums[i]], y[nums[i]] = [], []
        for j in range(i):
            if nums[j][0] == nums[i][0]:
                x[nums[j]].append(nums[i])
                x[nums[i]].append(nums[j])
            if nums[j][1] == nums[i][1]:
                y[nums[j]].append(nums[i])
                y[nums[i]].append(nums[j])


    for first, seconds in x.items():
        if len(seconds) < 1: continue
        for second in seconds:
            if y[first] and y[second]:
                for third in y[first]:
                    for forth in y[second]:
                        if third[0] == forth[0]: return [first, second, third, forth]
    return []


    return
np.random.seed(7)
x = np.random.randint(-100, 100, size=100)
y = np.random.randint(-100, 100, size=100)
x[0], x[25], x[75], x[90] = -15, -15, 15, 15
y[0], y[25], y[75], y[90] = -10, 10, -10, 10

nums = [(x[i], y[i]) for i in range(100)]
print(judge(nums))