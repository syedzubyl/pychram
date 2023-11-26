import numpy as np

# create two 2d numpy arrays
print("OPERATION ON MATRICES")
print("---------------------")
A = np.random.randint(10, size=(3, 3))
print("A>>", A)
B = np.random.randint(10, size=(3, 3))
print("B>>",B)

# perform matrix addition
print("ADDITION\n")
print("--------")
C = A + B
print("A + B =")
print(C)

# perform matrix subtraction
print("SUBTRACTION\n")
print("-----------")
D = A - B
print("A - B =")
print(D)

# perform matrix multiplication
print("MULTIPLICATION\n")
print("---------------")
E = A.dot(B)
print("A * B =")
print(E)

# perform matrix scaling
print("SCALING")
print("-------")
print(A)
A1 = np.array([1, 2, 3, 4, 5, 6])
A1.resize(4, 4)
print("Scaling A1 Matrix is: \n", A1)
f = np.hstack((A, B))
print(f)
