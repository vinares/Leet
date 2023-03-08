def alterSum(n):
    n = str(n)
    ans = 0

    for i, c in enumerate(n):
        if i % 2:
            ans -= int(c)
        else:
            ans += int(c)
    return ans
print(alterSum(15))

def replaceConsonant(message):
    ans = []

    for c in message:
        if c in 'aeiouAEIOU' or not c.isalnum():
            ans.append(c)
        elif c == 'z':
            ans.append('b')
        elif c == 'Z':
            ans.append('B')
        else:
            shift = 2 if c in 'dDhHnNtT' else 1
            pos = ord(c) + shift
            ans.append(chr(pos))
    return ''.join(ans)

print(replaceConsonant('abcdefgHIJKLMN123'))
from collections import defaultdict
def countId(msgs, members):
    hashtable = {}
    for member in members:
        id = int(member[2:])
        hashtable[id] = 0
    for messege in msgs:
        m = messege.split()
        cur_ids = set()
        for word in m:
            if len(word) < 3 or word[0:3] != '@id':
                continue
            ids = word[1:].split(',')
            for id in ids:
                if id not in members:
                    continue
                num = int(id[2:])
                cur_ids.add(num)
        for id in cur_ids:
            hashtable[id] += 1
    res = []
    for id, cnt in sorted(hashtable.items(), key=lambda x: (x[1], -x[0]), reverse=True):
        res.append('id' + str(id) + '=' + str(cnt))
    return res

msgs = [
    "Hi @id1,id3,id8, today is a good day @id1",
    "oh id2",
    "see ya @id8",
]
members = ["id1", "id2", "id8", "id300", "id30"]
print(countId(msgs, members))


def matchPattern(board, pattern):
    if not board: return [-1, -1]
    m, n = len(board), len(board[0])
    p, q = len(pattern), len(pattern[0])
    for i in range(0, m-p+1):
        for j in range(0, n-q+1):
            memory = {}
            Not_Match = False
            for x in range(p):
                r = x+i
                for y in range(q):
                    c = y+j
                    char = pattern[x][y]
                    if char.isdigit():
                        if board[r][c] != int(char):
                            Not_Match = True
                            break
                    else:
                        if char in memory and memory[char] == board[r][c]:
                            continue
                        elif (char in memory and memory[char] != board[r][c]) or (char not in memory and board[r][c] in memory.values()):
                            Not_Match = True
                            break
                        else:
                            memory[char] = board[r][c]
                if Not_Match: break
            if not Not_Match:
                return [i, j]
    return [-1, -1]


board = [[4,1,1,3,2],
         [2,4,1,3,3],
         [1,1,4,2,3]]
pattern = [['a', 'c'],
['a', 'c']]

print(matchPattern(board, pattern))


def overlapping(centers):
    centers.sort()
    ans = 0

    for i in range(len(centers)):
        for j in range(i+1, len(centers)):
            if centers[j][0]-centers[i][0] > 2: break
            if abs(centers[j][1]-centers[i][1]) <= 2: ans += 1
    return ans

centers = [[1,1],[2,2],[0,4]]
print(overlapping(centers))


def tShift(arr):
    index = arr.index(min(arr))
    if sorted(arr) != arr[index:] + arr[:index]:
        return -1
    else:
        return min(index, len(arr)-index)
print(tShift([3, 4, 5, 1, 2]))

def rotate90Clockwise(A):
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp
 