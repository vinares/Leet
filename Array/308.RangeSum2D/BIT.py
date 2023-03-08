class NumArray:
    def __init__(self, matrix: list):
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.fenwick = [[0] * (self.n + 1)] * (self.m + 1)
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                self.fenwick[i][j] = sum(matrix[i - 1][j - (j & -j) : j])
                print(self.fenwick[0])

    def update(self, i: int, j: int, val: int) -> None:
        row, col = i + 1, j + 1
        I, J = row, col
        diff = val - self.matrix[i][j]
        for k in range(row, self.m + 1, I & -I):
            for l in range(col, self.n + 1, J & -J):
                print(k,l)
                self.fenwick[k][l] += diff


    def sumRange(self, i: int, j: int) -> int:
        ans = 0
        i += self.n
        j += self.n
        while i <= j:
            if i % 2 == 1:
                ans += self.segement[i]
                i += 1
            if j % 2 == 0:
                ans += self.segement[j]
                j -= 1
            i //= 2
            j //= 2
        return ans

    def sum11ij(self, i: int, j: int) -> int:
        return



matrix  = [[1,2,3], [4,5,6], [7,8,9]]
case = NumArray(matrix)
print(case.sumRange(2,1,3,4))