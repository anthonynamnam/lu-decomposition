import Matrix

a = Matrix.Matrix(3, 3, two_d_array=[[2, -1, -2], [-4, 6, 3], [-4, -2, 8]])
print("A:")
a.print_values()
(x, y) = Matrix.LU(a)
print("L:")
x.print_values()
print("U:")
y.print_values()
