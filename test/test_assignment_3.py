import numpy as np

def gaussian_elimination(A, b):
 n = len(b)
 A = A.astype(float)
 b = b.astype(float)
 for i in range(n):
  p = A[i, i]
  for j in range(i+1, n):
   f = A[j, i] / p
   A[j, i:] = A[j, i:] - f * A[i, i:]
   b[j] = b[j] - f * b[i]
 x = np.zeros(n)
 for i in range(n-1, -1, -1):
  x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
 d = 1
 for i in range(n):
  d *= A[i, i]
 return x, d


def lu_decomposition(A):
 n = A.shape[0]
 L = np.eye(n)
 U = A.copy().astype(float)
 for i in range(n):
  for j in range(i+1, n):
   f = U[j, i] / U[i, i]
   L[j, i] = f
   U[j, i:] = U[j, i:] - f * U[i, i:]
 return L, U


def diagonally_dominant(A):
 n = A.shape[0]
 for i in range(n):
  if abs(A[i, i]) < np.sum(np.abs(np.delete(A[i], i))):
   return False
 return True


def positive_definite(A):
 e = np.linalg.eigvals(A)
 return np.all(e > 0)


A1 = np.diag([0.998206, 0.998206, 1.249])
x_true = np.array([2, -1, 1])
b1 = A1.dot(x_true)
x1, d1 = gaussian_elimination(A1.copy(), b1.copy())
c1 = np.max(np.abs(np.diag(A1))) / np.min(np.abs(np.diag(A1)))

print(d1)
print(c1)
print(x1)


A2 = np.array([[1, 1, 0, 3],
               [2, 1, -1, 1],
               [3, -1, -1, 2],
               [-1, 2, 3, -1]], float)
L2, U2 = lu_decomposition(A2.copy())
d2 = np.prod(np.diag(U2))

print(d2)
print(L2)
print(U2)


A3 = np.array([[9, 0, 5, 2, 1],
               [3, 9, 1, 2, 1],
               [0, 1, 7, 2, 3],
               [4, 2, 3, 12, 2],
               [3, 2, 4, 0, 8]], float)
dd = diagonally_dominant(A3)
print(dd)


A4 = np.array([[2, 2, 1],
               [2, 3, 0],
               [1, 0, 2]], float)
pd = positive_definite(A4)
print(pd)
