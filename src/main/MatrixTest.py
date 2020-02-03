import unittest
import ComplexNumber as complex
import Matrix as matrix

class ComplexNumberTest(unittest.TestCase):

    def testShouldAddTwoMatrices(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(-1, -1), complex.ComplexNumber(3, 0)], [complex.ComplexNumber(4, 6), complex.ComplexNumber(2, 2)]])
        m2 = matrix.Matrix([[complex.ComplexNumber(1, 0), complex.ComplexNumber(3, 4)], [complex.ComplexNumber(0, 2), complex.ComplexNumber(-3, 1)]])
        mTest = m1.add(m2)
        mSol =  matrix.Matrix([[complex.ComplexNumber(0, -1), complex.ComplexNumber(6, 4)], [complex.ComplexNumber(4, 8), complex.ComplexNumber(-1, 3)]])
        self.assertTrue(mTest.equals(mSol))


if __name__ == '__main__':
    unittest.main()
