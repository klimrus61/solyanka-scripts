def sum_prod_diags1(m):
    s, n = 0, len(m)
    for d in 0, -1:
        for x in range(n):
            h = v = 1
            for u in range(n-x):
                h *= m[u ^ d][x+u]
                if x: v *= m[(x+u) ^ d][u]
            s += (d | 1) * (h + v)
    return s

def sum_prod_diags(matrix):
    len_mat = len(matrix)
    res = 0
    d_r, d_b = 1, 1
    for i in range(len_mat):
        d_r *= matrix[i][i]
        d_b *= matrix[len_mat-i-1][i]
        higher_d_r, lower_d_r = 1, 1
        higher_d_b, lower_d_b = 1, 1
        for j in range(len_mat-i):
            if i != 0:
                higher_d_r *= matrix[i+j][j]
                lower_d_r *= matrix[j][i+j]
                higher_d_b *= matrix[len_mat-i-1-j][j]
                lower_d_b *= matrix[len_mat-j-1][i+j]
        res += higher_d_r + lower_d_r - higher_d_b -lower_d_b
    res = res + d_r - d_b
    return res

M1=[[ 1,  4, 7,  6,  5],
    [-3,  2, 8,  1,  3],
    [ 6,  2, 9,  7, -4],
    [ 1, -2, 4, -2,  6],
    [ 3,  2, 2, -4,  7]]
print(sum_prod_diags1(M1))

import numpy as np 

def sum_prod_diags(matrix):
    mtrx = np.array(matrix) 
    dia  = np.diagonal
    prd  = np.prod
    ln   = len(mtrx)
    rg   = range(-ln + 1, ln)
    return sum([prd( dia(mtrx,i) ) for i in rg]) - sum([prd( dia( np.fliplr(mtrx) ,i)) for i in rg])