import numpy as np
# A = np.array([[4,1,-2,3,4,3],[7,2,2,4,5,4],[0,4,2,3,2,5],[1,2,3,6,4,2],[1,0,2,0,0,2],[3,2,4,2,3,4],[4,1,-2,3,4,3]])


def step_1(A,set_i,j):
    return A[set_i][j]

def step_2(A,set_i,set_j):
    m,n = A.shape
    print(f"entering step_2 wit set_i {set_i} and set_j {set_j}")
    for j in range(set_j,n):
        if step_1(A,set_i,j) == 0:
            for i in range(m-1,0,-1):
                if A[i][j]!=0:
                    print(f"A[{i}][{j}] is not 0, changin rows...") 
                    A[[0,i]] = A[[i,0]]
                    return j
        else:
            return j
    return None


def step3(A,i,j):
    print(f"entering step3 with set_i {i} and set_j {j} ")
    m,n = A.shape
    for x in range(i+1,m):
        if A[x][j] != 0:
            a = A[x] * A[i][j]
            b = A[i] * A[x][j]
            A[x] = a - b