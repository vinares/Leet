"""
def get_five_score(number):
    score = 0
    
    # Consecutive 5s
    for idx in range(len(number) - 1):
        if number[idx] == '5' and number[idx + 1] == '5':
            score += 3

    return score

def get_sequence_score(number):
    orig_number = number
    score = 0
    digits = []
    sequence = []

    number = int(number[::-1])
    while number > 0:
        digits.append(number % 10)
        number = number // 10

    # Add zeroes at the tail of number
    while len(digits) < len(orig_number):
        digits.append(0)

    sequence.append(digits[0])
    for idx in range(1, len(digits)):
        if digits[idx] == digits[idx - 1] - 1:
            sequence.append(digits[idx])
        else:
            score += (len(sequence) * len(sequence))
            sequence = [digits[idx]]

    if len(sequence) > 1:
        score += (len(sequence) * len(sequence))
    else:
        score += 1

    return score

def compute_number_score(number):
    score = 0
    digits = [int(i) for i in str(number)]
    
    # Even
    score += len([i for i in digits if i % 2 == 0 or i == 0]) * 4

    # Multiple of 3
    if number % 3 == 0:
        score += 2
    
    # Seven
    score += len([i for i in digits if i == 7])

    # Five
    score += get_five_score(str(number))

    # Sequence
    score += get_sequence_score(str(number))

    return score

"""




def compute_number_score(n):
    score = 0
    if (n%3 == 0):
        score += 2
    num = str(n)
    i, length = 0, len(num)
    N = 0
    five = 0
    prev = -1
    while i < length:
        cur = num[i]
        if cur=='7':
            score += 1
        if int(cur) % 2 == 0:
            score += 4
        if cur == '5':
            if five != 0:
                score += 3
            five += 1
        else:
            five = 0
        if int(cur) + 1 == prev:
            N += 1
        else:
            score += N ** 2
            N = 1
        prev = int(cur)
        i +=1 
    score += N ** 2
    return score



print(compute_number_score(5555))


def check_log_history(history):
    stack = []
    for i in range(len(history)):
        action, lock = history[i].split()
        if action == "ACQUIRE":
            if lock in stack:
                return i+1
            stack.append(lock)
        elif action == "RELEASE":
            if not stack or stack[-1] != lock:
                return i+1
            stack.pop()
    if stack:
        return len(history) + 1
    return 0


history = ["ACQUIRE 364", "ACQUIRE 84", "RELEASE 84", "ACQUIRE 1337", "RELEASE 1337", "RELEASE 364", "RELEASE 1"]
print(check_log_history(history))


import math
print(math.log2(10) * 6)