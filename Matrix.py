class Matrix:
    values = []

    def __init__(self, n_row, n_col, all_zero=True, two_d_array=None):
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
                        print(i, j, two_d_array[i][j])
                        row_val.append(two_d_array[i][j])
                    except:
                        row_val.append(0)
                self.values.append(row_val)
        elif all_zero:
            for i in range(n_col):
                row_val = []
                for j in range(n_row):
                    row_val.append(0)
                self.values.append(row_val)

    def print_shape(self):
        print(f"Matrix Shape: ({self.n_col},{self.n_row})")

    def print_values(self):
        for row in self.values:
            print(row)

    def set_values(self, values, row_pos, col_pos):
        self.values[row_pos - 1][col_pos - 1] = values


def LU(M):
    pass
