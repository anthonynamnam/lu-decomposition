import Matrix

# ----- Example 1 -----
# Create the matrix
a = Matrix.Matrix(3, 3, two_d_array=[[2, -1, -2], [-4, 6, 3], [-4, -2, 8]])

# Print the matrix A
a.print_values(matrix_name = "A")
# Perform LU decomposition
(x, y) = Matrix.LU(a)
# Print the LU decomposition result, i.e. Matrix L and U
x.print_values(matrix_name = "L")
y.print_values(matrix_name = "U")
