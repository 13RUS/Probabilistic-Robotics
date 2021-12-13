import math
from math import sqrt
import numbers
import numpy as np

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])
        
    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        if self.h == 1:
            factor = 1 / matrix[0][0]
            
        elif self.h == 2:
            # If the matrix is 2x2, check that the matrix is invertible
            if self[0][0] * self[1][1] == self[0][1] * self[1][0]:
                raise ValueError('The matrix is not invertible.')
            else:
                # Calculate the inverse of the square 1x1 or 2x2 matrix.
                a = self[0][0]
                b = self[0][1]
                c = self[1][0]
                d = self[1][1]
            
                factor = 1 / (a * d - b * c)
  
        return factor 

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
       
        
        selfsum = 0 
        
        for i in range(self.h):
            for j in range (self.w):
                if (i==j): 
                 
                    selfsum=selfsum+self[i][j]

      
        return selfsum
        
        # TODO - your code here

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        inverse = []
        
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        if self.h == 1:
            inverse.append([1 / self[0][0]])
        elif self.h == 2:
        # If the matrix is 2x2, check that the matrix is invertible
            if self[0][0] * self[1][1] == self[0][1] * self[1][0]:
                raise ValueError('The matrix is not invertible.')
            else:
                # Calculate the inverse of the square 1x1 or 2x2 matrix.
                a = self[0][0]
                b = self[0][1]
                c = self[1][0]
                d = self[1][1]
            
                factor = 1 / (a * d - b * c)
            
                inverse = [[d, -b],[-c, a]]
            
                for i in range(len(inverse)):
                    for j in range(len(inverse[0])):
                        inverse[i][j] = factor * inverse[i][j]
        return Matrix(inverse)

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        matrix_transpose = []
        # Loop through columns on outside loop
        for c in range(self.h):
            new_row = []
            # Loop through columns on inner loop
            for r in range(self.w):
            # Column values will be filled by what were each row before
                new_row.append(self[r][c])
            matrix_transpose.append(new_row)
        
        return Matrix(matrix_transpose)

    def is_square(self):
        return self.h == self.w

    def dot_product(vectorA, vectorB):
        result = 0
    
        for i in range(len(vectorA)):
            result += vectorA[i] * vectorB[i]
        
        return result
   
    def get_column(matrix, column_number):
        column = []
        for i in range (len(matrix)):
            column.append(matrix[i][column_number])
        return column
    
    
    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        
        matrixSum = []
    
        # matrix to hold a row for appending sums of each element
        row = []
    
       
        # For loop within a for loop to iterate over the matrices
        for r in range(self.h):
            row = [] # reset the list
            for c in range(self.w):
                row.append(self[r][c] + other[r][c]) # add the matrices
            
            matrixSum.append(row)
    
        return Matrix(matrixSum)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        
        row = []
        matrixNeg = []
    
        # For loop within a for loop to iterate over the matrices
        for r in range(self.h):
            row = [] # reset the list
            for c in range(self.w):
                row.append(self[r][c] * (-1)) # add the matrices
            
            matrixNeg.append(row)
        
        return Matrix(matrixNeg)
        
        
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        
        matrixSum = []
    
        # matrix to hold a row for appending sums of each element
        row = []
    
       
        # For loop within a for loop to iterate over the matrices
        for r in range(self.h):
            row = [] # reset the list
            for c in range(self.w):
                row.append(self[r][c] - other[r][c]) # add the matrices
            
            matrixSum.append(row)
    
        return Matrix(matrixSum)


    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        C = [[0 for row in range(self.h)] for col in range(other.w)]
        for i in range(self.h):
            for j in range(other.w):
                for k in range(other.h):
                    C[i][j] += self[i][k]*other[k][j]
       
        return Matrix(C)  
            
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        matrixSum=[]
        if isinstance(other, numbers.Number):
            pass      
            for r in range(self.h):        
                row = [] # reset the list
                for c in range(self.w):            
                    row.append(self[r][c]*other) # add the matrices  
                matrixSum.append(row)
            
            return Matrix(matrixSum)
            #   
            # TODO - your code here
            #
            