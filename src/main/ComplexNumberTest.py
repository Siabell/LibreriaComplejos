import unittest
import ComplexNumber as complex

class ComplexNumberTest(unittest.TestCase):

    def testShouldAddTwoComplexNumbers(self):
        c1 = complex.ComplexNumber(3, -1)
        c2 = complex.ComplexNumber(1,4)
        cResultTest = c1.add(c2)
        self.assertEqual(cResultTest.partReal,4)
        self.assertEqual(cResultTest.partImag,3)

if __name__ == '__main__':
    unittest.main()
