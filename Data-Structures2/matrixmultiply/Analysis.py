import matplotlib.pyplot as plt
import time
import random


def multiply(A, B):
    n = len(A)

    if n == 1:
        C = [[0]]
        C[0][0] = A[0][0] * B[0][0]
        return C
    else:
        A11 = [[0 for i in range(n//2)] for j in range(n//2)]
        A12 = [[0 for i in range(n//2)] for j in range(n//2)]
        A21 = [[0 for i in range(n//2)] for j in range(n//2)]
        A22 = [[0 for i in range(n//2)] for j in range(n//2)]

        B11 = [[0 for i in range(n//2)] for j in range(n//2)]
        B12 = [[0 for i in range(n//2)] for j in range(n//2)]
        B21 = [[0 for i in range(n//2)] for j in range(n//2)]
        B22 = [[0 for i in range(n//2)] for j in range(n//2)]

        split(A, A11, A12, A21, A22)
        split(B, B11, B12, B21, B22)

        P01 = multiply(A11, B11)
        P02 = multiply(A12, B21)
        P03 = multiply(A11, B12)
        P04 = multiply(A12, B22)
        P05 = multiply(A21, B11)
        P06 = multiply(A22, B21)
        P07 = multiply(A21, B12)
        P08 = multiply(A22, B22)

        C11 = add(P01, P02)
        C12 = add(P03, P04)
        C21 = add(P05, P06)
        C22 = add(P07, P08)

        C = [[0 for i in range(n)] for j in range(n)]
        join(C11, C12, C21, C22, C)

        return C
        
        
def Strassen(A, B):
    n = len(A)
    
    if n == 1:
        C = [[0]]
        C[0][0] = A[0][0] * B[0][0]
        return C
    else:
        A11 = [[0 for x in range(n//2)] for y in range(n//2)]
        A12 = [[0 for x in range(n//2)] for y in range(n//2)]
        A21 = [[0 for x in range(n//2)] for y in range(n//2)]
        A22 = [[0 for x in range(n//2)] for y in range(n//2)]
        B11 = [[0 for x in range(n//2)] for y in range(n//2)]
        B12 = [[0 for x in range(n//2)] for y in range(n//2)]
        B21 = [[0 for x in range(n//2)] for y in range(n//2)]
        B22 = [[0 for x in range(n//2)] for y in range(n//2)]
        
        split(A, A11, A12, A21, A22)
        split(B, B11, B12, B21, B22)

        S01 = add(A11, A22)
        S02 = add(B11, B22)
        S03 = add(A21, A22)
        S04 = subtract(B12, B22)
        S05 = subtract(B21, B11)
        S06 = add(A11, A12)
        S07 = subtract(A21, A11)
        S08 = add(B11, B12)
        S09 = subtract(A12, A22)
        S010 = add(B21, B22)
        
        P01 = Strassen(S01, S02)
        P02 = Strassen(S03, B11)
        P03 = Strassen(A11, S04)
        P04 = Strassen(A22, S05)
        P05 = Strassen(S06, B22)
        P06 = Strassen(S07, S08)
        P07 = Strassen(S09, S010)
                
        C11 = subtract(add(add(P01, P04), P07), P05)
        C12 = add(P03, P05)
        C21 = add(P02, P04)
        C22 = subtract(add(add(P03, P06), P01), P02)
                
        C = [[0 for x in range(n)] for y in range(n)]
        join(C11, C12, C21, C22, C)

        return C
    

def subtract(A, B):
    n = len(A)
    C = [[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]

    return C


def split(A, A11, A12, A21, A22):
    n = len(A) // 2

    for i in range(n):
        A11[i][:n] = A[i][:n]
        A12[i][:n] = A[i][n:]
        A21[i][:n] = A[i+n][:n]
        A22[i][:n] = A[i+n][n:]


def join(C11, C12, C21, C22, C):
    n = len(C11)

    for i in range(n):
        C[i][0 : n] = C11[i][0 : n]
        C[i][n : 2 * n] = C12[i][0 : n]
        C[i + n][0 : n] = C21[i][0 : n]
        C[i + n][n : 2 * n] = C22[i][0 : n]


def add(A, B):
    n = len(A)
    C = [[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]

    return C


def normalMultiplication(A, B):
    C = [[0 for fila in range(len(B[0]))] for col in range(len(A))]
    
    # Realiza la multiplicación
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C




if __name__ == '__main__':

    A = [[8,1,4,34], [7,8,4,3], [6,86,3,3], [7,1,5,7]]
    B = [[6,5,3,23], [12,7,7,1], [2,1,13,54], [7,9,21,44]]
    
    C = multiply(A, B)
    D = Strassen(A, B)
    d = normalMultiplication(A, B)

    print(C)
    print(D)
    print(d)

    TiemposNormal = []
    TiemposDivideConquer = []
    TiemposStrassen = []

    for n in range(7):
       
        A = [[random.randint(1, 100) for i in range(2**n)] for j in range(2**n)]
        B = [[random.randint(1, 100) for i in range(2**n)] for j in range(2**n)]


        start = time.time()
        multiply(A, B)
        end = time.time()
        TiemposDivideConquer.append(end - start)

        start2 = time.time()
        Strassen(A, B)
        end2 = time.time()
        TiemposStrassen.append(end2 - start2)

        start3 = time.time()
        normalMultiplication(A, B)
        end3 = time.time()
        TiemposNormal.append(end3 - start3)

    x = [2**n for n in range(7)]

    plt.plot(x, TiemposNormal, label='Normal')
    plt.plot(x, TiemposDivideConquer, label='Divide and conquer')
    plt.plot(x, TiemposStrassen, label='Strassen')
    plt.xlabel('Tamaño 2**n')
    plt.ylabel('Segundos')
    plt.title('Multiplicacion_Matrices')
    plt.legend()
    plt.show()

    
    