import numpy as np
def QSort(nums, left, right):
    n = right - left + 1
    if n < 2:
        return
    pivot = np.random.randint(left,right)
    i, j = left + 1, left + 1
    nums[left], nums[pivot] = nums[pivot], nums[left]

    while j <= right:
        while j <= right and i == j and nums[i] < nums[left]:
            i += 1
            j += 1
        if j >= right:
            break
        if nums[j] < nums[left]:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        else:
            j += 1

    pivot = i - 1
    nums[left], nums[pivot] = nums[pivot], nums[left]
    QSort(nums, left, pivot - 1)
    QSort(nums, pivot + 1, right)
    return

x = [1,45,2,5,7,23,2,3,57,37,4,8]
z = QSort(x, 0, len(x) - 1)
print(x)