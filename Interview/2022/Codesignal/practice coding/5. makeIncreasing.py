def makeIncreasing(numbers):
    if len(numbers) <= 1:return True
    prev = -1
    numbers.append(10 ** 19)
    problemData = None

    for i in range(len(numbers) - 1):
        if prev < numbers[i] < numbers[i + 1]:
            continue
        else:
            if problemData:return False
            problemData = i

    if not problemData:return True
    dataString = str(numbers[problemData])
    for i in range(len(dataString)):
        for j in range(i, len(dataString)):
            testpoint = int(dataString[0:i] + dataString[j] + dataString[i + 1:j - 1] + dataString[i] + dataString[j+1::])
            if dataString == 0 and testpoint < numbers[1]:
                return True
            elif numbers[problemData - 1] < testpoint < numbers[problemData + 1]:
                return True
    return False
numbers =  [13, 31, 30]
print(makeIncreasing(numbers))
