class Matrix:
    values = []

    def __init__(self, n_row, n_col, all_zero=True, two_d_array=None):
        self.values = []
        self.n_row = n_row
        self.n_col = n_col
        if two_d_array is not None:
            assert type(two_d_array) == list and type(two_d_array[0]) == list
            n_row = max(len(two_d_array), n_row)
            n_col = max(max([len(row) for row in two_d_array]), n_col)
            for i in range(n_row):
                row_val = []
                for j in range(n_col):

                    try:
                        row_val.append(float(two_d_array[i][j]))
                    except:
                        row_val.append(0)
                self.values.append(row_val)
        elif all_zero:
            for i in range(n_col):
                row_val = []
                for j in range(n_row):
                    row_val.append(0.0)
                self.values.append(row_val)

    def print_shape(self):
        print(f"Matrix Shape: ({self.n_col},{self.n_row})")

    def print_values(self, matrix_name = ""):
        if len(matrix_name) > 0:
            print(f"{matrix_name}:")
        for row in self.values:
            for row_val in row:
                print(f"{row_val}\t", end="")
            print("")
        print("")

    def set_values(self, values, row_pos, col_pos):
        self.values[row_pos][col_pos] = float(values)

    def set_diagonal(self, values=1):
        assert self.n_col == self.n_row, "set_diagonal only available to square matrix"
        for i in range(self.n_col):
            self.set_values(values, i, i)


def LU(M: Matrix) -> tuple():
    assert M.n_col == M.n_row
    new_M = Matrix(M.n_row, M.n_col, two_d_array=M.values)
    # Initize L and U Matrix
    L = Matrix(new_M.n_col, new_M.n_row)
    for i in range(new_M.n_col):
        L.set_diagonal(1.0)

    U = Matrix(new_M.n_col, new_M.n_row)
    for i in range(3):
        print(f"Iteration {i+1}:")
        new_M.print_values()
        # Assign diagonal value
        U.values[i][i] = new_M.values[i][i]

        for j in range(i + 1, new_M.n_col):
            L.values[j][i] = new_M.values[j][i] / U.values[i][i]
            U.values[i][j] = new_M.values[i][j]

        for j in range(i + 1, new_M.n_col):
            for k in range(i + 1, new_M.n_row):
                new_M.values[j][k] -= L.values[j][i] * U.values[i][k]

    return (L, U)
