import Matrix

# ----- Example -----
# Create the matrix
A = Matrix.Matrix(
    n_row=3,
    n_col=3,
    two_d_array=[[2, -1, -2], [-4, 6, 3], [-4, -2, 8]],
)

# Print the matrix A
A.print_values(matrix_name="A")

# Perform LU decomposition
(L, U) = Matrix.LU(A, print_step=False)

# Print the LU decomposition result, i.e. Matrix L and U
L.print_values(matrix_name="L")
U.print_values(matrix_name="U")
