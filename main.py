import numpy as np
from methods import *

# A = np.array([[4,1,-2,3,4,3],[7,2,2,4,5,4],[0,4,2,3,2,5],[1,2,3,6,4,2],[1,0,2,0,0,2],[3,2,4,2,3,4],[4,1,-2,3,4,3]])
# A = np.array([[2,3,-1,10],[1,-2,2,-5],[3,1,-4,6]])
A = np.array([[0,0,0,0],[0,0,0,1],[0,0,0,0]])

# print(A)

# Seleccionamos la columna mas a la izquierda, sera la columna pivote
# Si la primera fila vale 0, lo sustituimos por la ultima columna no nula


def echelon(A):
    m,n = A.shape
    set_i,set_j = 0,0
    for i in range(m):
        j = step_2(A,set_i,set_j)
        if j==None:
            break
        print(f"the {i}th pivot column is the {j}th column, its {A[i][j]}")
        set_i =i+1
        set_j = j+1
        print(A)
        step3(A,i,j)
        print(A)
    
    print("finally...")
    print(A)

echelon(A)
# print(A)
