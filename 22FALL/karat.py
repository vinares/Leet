from collections import defaultdict, deque

def find_pairs(student_course_pairs_1):
    ans = dict()
    n = len(student_course_pairs_1)
    for i in range(1, n):
        id, course = student_course_pairs_1[i]
        for j in range(i):
            uid, ucourse = student_course_pairs_1[j]
            if id == uid:
                continue
            if (uid, id) not in ans and (id, uid) not in ans:
                ans[(uid, id)] = []
            if course == ucourse:
                if (uid, id) in ans:
                    ans[(uid, id)].append(course)
                else:
                    ans[(id, uid)].append(course)
    return ans


student_course_pairs_1 = [
    ["58", "Software Design"],
    ["58", "Linear Algebra"],
    ["94", "Art History"],
    ["94", "Operating Systems"],
    ["17", "Software Design"],
    ["58", "Mechanics"],
    ["58", "Economics"],
    ["17", "Linear Algebra"],
    ["17", "Political Science"],
    ["94", "Economics"],
    ["25", "Economics"],
]

print(find_pairs(student_course_pairs_1))


def reachAllZeros(board, start):
    if not board:
        return True
    m, n = len(board), len(board[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    ans = False
    zeros = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] != -1:
                zeros += 1

    def dfs(i, j, left):
        nonlocal ans
        if i < 0 or j < 0 or i >= m or j >= n or board[i][j] == -1 or ans:
            return
        tmp = board[i][j]
        if left == 0:
            ans = True
        board[i][j] = -1
        for dx, dy in directions:
            dfs(i+dx, j+dy, left-1)
        board[i][j] = tmp
        return
    dfs(start[0], start[1], zeros)
    return ans


def findAllTreasures(board, start, end):
    if not board:
        return None
    treasures, m, n = 0, len(board), len(board[0])
    for i in range(m):
        for j in range(n):
            if board[i][j] == 1:
                treasures += 1
    paths = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(i, j, path, treasure):
        if (i < 0 or j < 0 or i >= m or j >= n or board[i][j] == -1):
            return
        val = board[i][j]
        if val == 1:
            treasure -= 1
        if i == end[0] and j == end[1] and treasure == 0:
            paths.append(path+[(i, j)])
            return
        board[i][j] = -1
        for dx, dy in directions:
            x, y = i+dx, j+dy
            dfs(x, y, path+[(i, j)], treasure)
        board[i][j] = val
        return

    dfs(start[0], start[1], [], treasures)
    if not paths:
        return None
    min_length = m*n
    path = []
    for p in paths:
        if len(p) < min_length:
            min_length = len(p)
            path = []
            path.append(p)
        elif len(p) == min_length:
            path.append(p)
    return path


board = [
    [1, 0, 0, 0, 0],
    [0, -1, -1, 0, 0],
    [0, -1, 0, 1, 0],
    [-1, 0, 0, 0, 0],
    [0, 1, -1, 0, 0],
    [0, 0, 0, 0, 0],
]
board1 = [
    [ 0,  0,  0, 0, -1 ],
    [ 0, -1, -1, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
    [ 0, -1,  0, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
]
print(findAllTreasures(board, (5, 0), (0, 4)))
print(findAllTreasures(board, (5, 2), (2, 0)))
print(reachAllZeros(board1, (1, 3)))


def longest_non_decreasing_path(board, start, end):
    if not board:
        return 0
    m, n = len(board), len(board[0])
    start_points = []
    for i in range(m):
        for j in range(n):
            if board[i][j] == start:
                start_points.append((i, j))
    if not start_points:
        return 0
    directions, _1dmove = [], [0, 1, -1]
    for x in _1dmove:
        for y in _1dmove:
            if x == 0 and y == 0:
                continue
            directions.append((x, y))

    ans = 0

    def dfs(i, j, length, cur):
        nonlocal ans
        if i < 0 or j < 0 or i >= m or j >= n or board[i][j] > end or board[i][j] < cur:
            return
        val = board[i][j]
        if val == end and length >= ans:
            ans = length + 1
        board[i][j] = -1
        for dx, dy in directions:
            dfs(i+dx, j+dy, length+1, val)
        board[i][j] = val
        return
    for x, y in start_points:
        dfs(x, y, 0, start)
    return ans


board = [[1, 2, 3], [2, 2, 1]]
print(longest_non_decreasing_path(board, 1, 3))


def PowerfulCard(matchup):
    rev_G = defaultdict(list)
    degrees = defaultdict(int)
    for out_edge, in_edge in matchup:
        rev_G[in_edge].append(out_edge)
        degrees[out_edge] += 1
        if in_edge not in degrees:
            degrees[in_edge] = 0
    source = []
    for node, val in degrees.items():
        if val == 0:
            source.append(node)
    while source:
        next_source = set()
        for s in source:
            for u in rev_G[s]:
                next_source.add(u)
        if not next_source:
            return list(source)
        else:
            source = list(next_source)
    return source



matchup = [
    ['r', 'n'],
    ['n', 'sl'],
    ['r', 'w'],
    ['n', 'm'],
    ['w', 'e'],
    ['e', 'el']
]

matchup = [
    ['a', 'b'],
    ['c', 'd'],
    ['e', 'f'],
    ['d', 'k'],
    ['f', 'l'],
    ['k', 'g'],
    ['a', 'c'],
    ['e', 'a']
]

print(PowerfulCard(matchup))


def longestCommonContinuousHistory(history):
    maxlen = 0
    ans = ''
    m, n = len(history[0]), len(history[1])
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if history[0][j-1] == history[1][i-1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)
            if dp[i][j] > maxlen:
                maxlen = dp[i][j]
                ans = history[0][j-dp[i][j]:j]

    return ans


history = [
    ["3234.html", "xys.html", "7hsaa.html"],
    ["3234.html", "sdhsfjdsh.html", "xys.html", "7hsaa.html"]
]
print(longestCommonContinuousHistory(history))


def get_rectangle_coordinates(matrix):
    if not matrix:
        return []
    m, n = len(matrix), len(matrix[0])
    res = []

    def helper(i, j, matrix, res):
        flagr, flagc = 0, 0
        for x in range(i, m):
            if matrix[x][j] != 0:
                flagc = 1
                break
            for y in range(j, n):
                if matrix[x][y] != 0:
                    flagr = 1
                    break
                matrix[x][y] = 5
        endr = y-1 if flagr else y
        endc = x-1 if flagc else x
        res[-1] += [endc, endr]
        return

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                res.append([i, j])
                helper(i, j, matrix, res)
    return res


matrix = [
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 0]
]
print(get_rectangle_coordinates(matrix))


def reflowAndJustify(lines, maxlen):
    if not lines:
        return []
    lines = ' '.join(lines).split()
    i, n = 0, len(lines)
    groups = []
    while i < n:
        tmp_group = []
        remaining = maxlen
        while i < n:
            if remaining < len(lines[i]):
                break
            tmp_group.append(lines[i])
            remaining -= (len(lines[i])+1)
            i += 1
        groups.append(tmp_group)
    ans = []
    for group in groups:
        if len(group) == 1:
            ans.append(group[0])
            break
        spaces = maxlen - sum(len(w) for w in group)
        average_slash = spaces//(len(group)-1)
        extra_slash = spaces - average_slash*(len(group)-1)
        tmp = group[0]
        for i in range(1, len(group)):
            tmp += '-' * (average_slash + (extra_slash > 0)) + group[i]
            if extra_slash > 0:
                extra_slash -= 1
        ans.append(tmp)
    return ans


lines = ["The day began as still as the",
         "night abruptly lighted with",
         "brilliant flame"]


assert (reflowAndJustify(lines, 24) == ["The--day--began-as-still",
                                        "as--the--night--abruptly",
                                        "lighted--with--brilliant",
                                        "flame"])


def find_zero_and_one_parent(list_of_parent_child_pairs):
    degree = defaultdict(int)
    for p, c in list_of_parent_child_pairs:
        degree[c] += 1
        if p not in degree:
            degree[p] = 0
    return [x for x in degree if degree[x] < 2]


def find_if_common_ancestor_exists(list_of_parent_child_pairs, node_1, node_2):
    graph = defaultdict(list)
    for p, c in list_of_parent_child_pairs:
        graph[c].append(p)
    visited = set()
    q = deque([node_1])
    while q:
        cur = q.popleft()
        visited.add(cur)
        for u in graph[cur]:
            if u == node_2:
                return True
            if u not in visited:
                q.append(u)
    q = [node_2]
    visited_2 = set()
    while q:
        cur = q.pop()
        visited_2.add(cur)
        for u in graph[cur]:
            if u in visited:
                return True
            if u not in visited_2:
                q.append(u)
    return False


def find_farthest_common_ancestor(list_of_parent_child_pairs, node_1, node_2):
    graph = defaultdict(list)
    for p, c in list_of_parent_child_pairs:
        graph[c].append(p)
    if graph[node_2] == []:
        node_1, node_2 = node_2, node_1
    visited = set()
    q = deque([node_1])
    while q:
        cur = q.popleft()
        visited.add(cur)
        for u in graph[cur]:
            if u not in visited:
                q.append(u)
    candidates = []
    layer = 0
    q = [(node_2, layer)]
    visited_2 = set()
    while q:
        cur, l = q.pop()
        visited_2.add(cur)
        for u in graph[cur]:
            if u in visited_2:
                continue
            if u in visited:
                if l >= layer:
                    layer = l+1
                    candidates = []
                if l+1 == layer:
                    candidates.append(u)
            q.append((u, l+1))
    return candidates


list_of_parent_child_pairs = [
    [3, 5], [5, 8], [2, 5], [1, 2],
    [1, 4], [4, 0], [4, 13], [13, 6],
    [9, 6], [4, 9], [11, 7], [7, 15],
    [19, 15], [11, 1]
]
print(find_zero_and_one_parent(list_of_parent_child_pairs))
print(find_if_common_ancestor_exists(list_of_parent_child_pairs, 6, 15))
print(find_farthest_common_ancestor(list_of_parent_child_pairs, 19, 15))


def invalidBadgeRecords(badge_records):
    badge_in_miss, badge_out_miss = [], []
    tracker = defaultdict(int)
    for record in badge_records:
        name, action = record[0], record[1]
        if action == 'enter':
            if tracker[name] != 0:
                badge_out_miss.append(name)
            tracker[name] = 1
        elif action == 'exit':
            if tracker[name] != 1:
                badge_in_miss.append(name)
            tracker[name] = 0
    for name, cnt in tracker.items():
        if cnt != 0:
            badge_out_miss.append(name)
    return [badge_out_miss, badge_in_miss]


badge_records = [
    ["Martha",   "exit"],
    ["Paul",     "enter"],
    ["Martha",   "enter"],
    ["Martha",   "exit"],
    ["Jennifer", "enter"],
    ["Paul",     "enter"],
    ["Curtis",   "enter"],
    ["Paul",     "exit"],
    ["Martha",   "enter"],
    ["Martha",   "exit"],
    ["Jennifer", "exit"]
]
print(invalidBadgeRecords(badge_records) == [["Paul", "Curtis"], ["Martha"]])


def reachAllZeros(board, start):
    if not board:
        return True
    m, n = len(board), len(board[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    ans = False
    zeros = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] != -1:
                zeros += 1
    print(zeros)
    def dfs(i, j, left):
        nonlocal ans
        if i < 0 or j < 0 or i >= m or j >= n or board[i][j] == -1 or ans:
            return
        tmp = board[i][j]
        if left == 1:
            ans = True
            print(1111111111111)
        board[i][j] = -1
        for dx, dy in directions:
            dfs(i+dx, j+dy, left-1)
        board[i][j] = tmp
        return
    dfs(start[0], start[1], zeros)
    return ans


board1 = [
    [ 0,  0,  0, 0, -1 ],
    [ 0, -1, -1, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
    [ 0, -1,  0, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
]
print(reachAllZeros(board1, (5, 0)))
