class TicTocToe:
    def __init__(self, n):
        self.n, self.col, self.row, self.diag1, self.diag2 = n, [0 for i in range(n)], [0 for i in range(n)], 0, 0

    def move(self, x, y, player):
        if player == 1:
            offset = 1
        else:
            offset = -1
        self.col[y] += offset
        self.row[x] += offset
        if x == y: self.diag1 += offset
        if x == self.n - y - 1: self.diag2 += offset

        if self.n == self.diag1 or self.n == self.diag2 or self.n in self.col or self.n in self.row:
            return 1
        elif -self.n == self.diag1 or -self.n == self.diag2 or -self.n in self.col or -self.n in self.row:
            return 2
        else:
            return 0

chess = TicTocToe(3)
end = 0
player = 1
while not end:
    x = int(input())
    y = int(input())
    end = chess.move(x, y, player)
    if player == 1: player += 1
    else: player -= 1