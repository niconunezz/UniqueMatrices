import numpy as np
# A = np.array([[4,1,-2,3,4,3],[7,2,2,4,5,4],[0,4,2,3,2,5],[1,2,3,6,4,2],[1,0,2,0,0,2],[3,2,4,2,3,4],[4,1,-2,3,4,3]])

# Seleccionamos la columna mas a la izquierda, sera la columna pivote
def step_1(A,set_i,j):
    return A[set_i][j]

# Si la primera fila vale 0, lo sustituimos por la ultima columna no nula
def step_2(A,set_i,set_j):
    m,n = A.shape
    print(f"entering step_2 wit set_i {set_i} and set_j {set_j}")
    for j in range(set_j,n):
        if step_1(A,set_i,j) == 0:
            for i in range(m-1,set_i,-1):
                if A[i][j]!=0:
                    print(f"A[{i}][{j}] is not 0, changin rows...") 
                    A[[set_i,i]] = A[[i,set_i]]
                    return j
        else:
            return j
    # tdos los valores de la fila valen 0, hemos terminado
    return None

# Hacemos nulos todos los valores por debajo del pivote
def step3(A,i:int,j:int):
    print(f"entering step3 with set_i {i} and set_j {j} ")
    m,n = A.shape
    for x in range(i+1,m):
        if A[x][j] != 0:
            a = A[x] * A[i][j]
            b = A[i] * A[x][j]
            A[x] = a - b

# Repetimos paso 1,2 y 3 para la submatriz que surge al eliminar la fila y columna del pivote
def step_4(A):
    pivots = []
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
        pivots.append((i,j))
        step3(A,i,j)
        print(A)
    
    return A,pivots

#backward phase
# pasamos la matriz escalonada a su forma reducida
def make_one(A,i:int,j:int):
    A[i] = A[i]/A[i][j]
    
def make_zeros(A,i,j):
    for row in range(i-1,-1,-1):
        if A[row][j] !=0:
            a = A[row][j]*A[i]
            b = A[i,j]*A[row]
            A[row] = a - b

def step_5(A,pivots:list):
    m,n = A.shape
    pivots = pivots[::-1]
    for p in pivots:
        i,j = p
        if A[i][j] != 1:
            make_one(A,i,j)
        make_zeros(A,i,j)

    return A
        
def reduced_echelon(A):
    echelon,pivots = step_4(A)
    print(echelon)
    return step_5(echelon,pivots)