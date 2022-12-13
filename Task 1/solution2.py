# title Sum of elements on diag
# description Сумма элементов на главной и побочной диагоналях матрицы
# ---end---
def diagonalSum(matrix):
    diag_sum = 0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i == j or i + j == len(mat) - 1:
                diag_sum += mat[i][j]
                print(mat[i][j])

    return diag_sum
