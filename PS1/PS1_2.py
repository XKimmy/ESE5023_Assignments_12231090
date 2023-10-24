import numpy as np
import random

r1 =5
c1 = 10
M1 = [[random.randint(0,50) for _ in range(c1)] for _ in range(r1)]

r2 =10
c2 = 5
M2 = [[random.randint(0,50) for _ in range(c2)] for _ in range(r2)]

print("M1:", M1)
print("M2:", M2)


def Matrix_nultip(M1,M2):
    
    mul = [[0 for _ in range(c2)] for _ in range(r1)]
    
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                mul[i][j] += M1[i][k] * M2[k][j]
                
    return mul

result1 = Matrix_nultip(M1, M2)



# Check the result
result2 = np.dot(M1, M2)
print("Check the result:")
print(result1 == result2)
