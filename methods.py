import numpy as np
#forward phase
# Begin with the leftmost nonzero column. This is a pivot column. The pivot position is at the top.
def step_1(A,set_i,j):
    return A[set_i][j]

# Select a nonzero entry in the pivot column as a pivot. If necessary, interchange rows to move this entry into the pivot position.
def step_2(A,set_i,set_j):
    m,n = A.shape
    
    for j in range(set_j,n):
        if step_1(A,set_i,j) == 0:
            for i in range(m-1,set_i,-1):
                if A[i][j]!=0:
                    A[[set_i,i]] = A[[i,set_i]]
                    return j
        else:
            return j
    # every value in the row is a zero, the algorithm stops
    return None

# Use row replacement operations to create zeros in all positions below the pivot.
def step3(A,i:int,j:int):
    
    m,n = A.shape
    for x in range(i+1,m):
        if A[x][j] != 0:
            a = A[x] * A[i][j]
            b = A[i] * A[x][j]
            A[x] = a - b

# Cover (or ignore) the row containing the pivot position and cover all rows, if any,
# above it. Apply steps 1–3 to the submatrix that remains. Repeat the process until
# there are no more nonzero rows to modify.
def step_4(A):
    pivots = []
    m,n = A.shape
    set_i,set_j = 0,0
    for i in range(m):
        j = step_2(A,set_i,set_j)
        if j==None:
            break
        
        set_i =i+1
        set_j = j+1
       
        pivots.append((i,j))
        step3(A,i,j)
        
    
    return A,pivots

# backward phase
# Beginning with the rightmost pivot and working upward and to the left, create
# zeros above each pivot. If a pivot is not 1, make it 1 by a scaling operation.

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
    return step_5(echelon,pivots)