# README
This project is a simple Python program that uses basic Python functions and the NumPy library in order to to solve systems of linear equations and work with matrices

# Functions
The following functions are included below in the program and are explained as to what each function does to the matrices:
 1) Gaussian Elimination: Solves a system of linear equations by eliminating variables
 2) LU Factorization: Breaks down a 4x4 matrix into a lower triangular matrix (L) and an upper triangular matrix (U), then calculates the determinant.
 3) Diagonal Dominance Check: Determines if a 5x5 matrix is diagonally dominant
 4) Positive Definiteness Test: Checks if a 3x3 matrix is positive definite

# Running the Program
To run the actual program, please ensure that you put the following matrcies that you want in A1, A2, A3, and A4 variables and run the following in your terminal: assignment_3.py

To run the test program please run the following in your terminal: test_ assignment_3.py

# Output
After running the program in your terminal, you should get the following output:
 1) The determinant from the Gaussian elimination for the 3×3 system
 2) The condition number of the 3×3 matrix
 3) The solution vector for the 3×3 system
 4) The determinant from the LU factorization for the 4×4 matrix
 5) The L matrix from the LU factorization
 6) The U matrix from the LU factorization
 7) A boolean indicating whether the given 5×5 matrix is diagonally dominant
 8) A boolean indicating whether the given 3×3 matrix is positive definite
