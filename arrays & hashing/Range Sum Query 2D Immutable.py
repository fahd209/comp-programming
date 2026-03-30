class NumMatrix:

    # init object then preform pre work to create sum of sub matrix
    def __init__(self, matrix: List[List[int]]):
        ROW, COL = len(matrix), len(matrix[0])
        self.matrix = [[0] * (COL + 1) for r in range(ROW + 1)]

        for r in range(ROW):
            row_prefix_sum = 0
            for c in range(COL):
                top_num = self.matrix[r][c + 1]
                row_prefix_sum += matrix[r ][c]
                self.matrix[r + 1][c + 1] = row_prefix_sum + top_num

        print(self.matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottom_right = self.matrix[r2][c2]
        above_matrix_sum = self.matrix[r1 - 1][c2]
        bottom_left =  self.matrix[r2][c1 - 1]
        top_left_matrix_sum = self.matrix[r1 - 1][c1 - 1]

        return bottom_right - above_matrix_sum - bottom_left + top_left_matrix_sum