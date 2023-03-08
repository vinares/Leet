'''
Given a non-empty integer array `numbers`, you may perform increment operations, each of which increases one of
the values of the array by 1. Your task is to find the minimum number of increment operations required to make all
the array elements unique.
Note: You can increment the same array element multiple times.

numbers = [5, 1, 2, 4, 5, 2], the output should be obtainUniqueSequence(numbers) = 2.
One way to make all the elements unique is to increment numbers[0] and numbers[2], after which the array will
look like numbers = [6, 1, 3, 4, 5, 2]. Because 2 increment operations were performed, the answer is 2.
'''
def obtainUniqueSequence(nums):
    min_num, max_num = min(nums), max(nums)
    bucket = [None] * (max_num - min_num + len(nums))
    left = []
    for num in nums:
        if not bucket[num - min_num]:
            bucket[num - min_num] = nums
        else:
            left.append(num)
    count = 0
    for num in left:
        i = num - min_num
        while bucket[i] != None:
            i += 1
            count += 1
        bucket[i] = num
    return count


nums = [5, 1, 2, 4, 5, 2]
print(obtainUniqueSequence(nums))


