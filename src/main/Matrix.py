import math
import sys
import ComplexNumber as complex

class Matrix:
    def __init__(self, pmatrix):
        self.mtx =pmatrix
        self.m = len(pmatrix) #rows
        self.n = len(pmatrix) #column

    def add (mat1, mat2):
        if (mat1.m != mat2.m and mat1.n != mat2.n):
            raise Exception('The dimensions of the matrices are not the same ')
        else:
            matrixResult = [[complex.ComplexNumber(0,0) for x in range(mat1.m)] for y in range(mat1.n)] 
            for i in range (mat1.m):
                for j in range (mat1.n):
                    matrixResult[i][j] = mat1.mtx[i][j].add(mat2.mtx[i][j])
            matResult = Matrix(matrixResult)
            return matResult

    def inverse (mat)
        matrixResult = [[complex.ComplexNumber(0,0) for x in range(mat.m)] for y in range(mat.n)] 
            for i in range (mat.m):
                for j in range (mat.n):
                    matrixResult[i][j] = mat.mtx[i][j].inverse()
        matResult = Matrix(matrixResult)
        return matResult
    
    def 

    def equals(mat1,mat2):
            result = True
            if (mat1.m!= mat2.m or mat1.n != mat2.n):
                raise Exception('The dimensions of the matrices are not the same ')
            for i in range(mat1.m):
                for j in range(mat1.n):
                    if(mat1.mtx[i][j].partReal != mat2.mtx[i][j].partReal or mat1.mtx[i][j].partImag != mat2.mtx[i][j].partImag):
                        result = False
            return result

    def showMatrix(mat):
        for i in range(mat.m):
                for j in range(mat.n):
                    print(mat.mtx[i][j].partReal,mat.mtx[i][j].partImag)