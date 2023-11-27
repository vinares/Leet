from bisect import bisect_right
def find_next(arr, i):
    l, r = i, len(arr)-1
    next_i = -1
    while l <= r:
        m = l + (r-l)//2
        if arr[m] == arr[i]:
            next_i = m
            l = m + 1
        elif arr[m] > arr[i]:
            r = m - 1
    return next_i + 1

def unique(arr, N):
    if not arr: return 0
    i = 0
    ans = 0
    while i < N:
        next_i = find_next(arr, i)
        ans += 1
        i = next_i
    return ans

# Driver Code
arr = [1, 1, 1, 1, 1, 1, 2, 2, 2,
       2, 3, 5, 5, 7, 7, 8, 8, 9,
       9, 10, 11, 12]
arr = [1, 2, 3, 4, 5, 6, 100, 100]
N = len(arr)
print(unique(arr, N))