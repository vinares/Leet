import collections
from operator import itemgetter

def meanAndChessboard(matrix, queries):
    white = []
    black = []
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if (i + j) % 2:
                black.append((matrix[i][j], i, j))
            else:
                white.append((matrix[i][j], i, j))
    black.sort(key=itemgetter(0))
    white.sort(key=itemgetter(0))
    new_black, new_white = [black[0]], [white[0]]
    for i in range(1, len(black)):
        if black[i][0] == new_black[-1][0]:
            if black[i][2] < new_black[-1][2]:
                new_black.pop()
                new_black.append(black[i])
            elif black[i][2] == new_black[-1][2]:
                if black[i][1] < new_black[-1][1]:
                    new_black.pop()
                    new_black.append(black[i])
        else:
            new_black.append(black[i])
    for i in range(1, len(white)):
        if white[i][0] == new_white[-1][0]:
            if white[i][2] < new_white[-1][2]:
                new_white.pop()
                new_white.append(white[i])
            elif white[i][2] == new_white[-1][2]:
                if white[i][1] < new_white[-1][1]:
                    new_white.pop()
                    new_white.append(white[i])
        else:
            new_white.append(white[i])


    for quiry in queries:
        average = new_black[quiry[0]][0] + new_white[quiry[1]][0]
        if not average % 2:
            matrix[new_black[quiry[0]][2]][new_black[quiry[0]][1]] = average // 2
            matrix[new_white[quiry[1]][2]][new_white[quiry[1]][1]] = average // 2
        else:
            matrix[new_black[quiry[0]][2]][new_black[quiry[0]][1]] = average // 2
            matrix[new_white[quiry[1]][2]][new_white[quiry[1]][1]] = average // 2

    return matrix
matrix = [[2, 0, 4],
          [2, 8, 5],
          [6, 0, 9],
          [2, 7, 10],
          [4, 3, 4]]
queries = [[0, 0], [1, 3]]
print(meanAndChessboard(matrix, queries))