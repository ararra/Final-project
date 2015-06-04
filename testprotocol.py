import BestApprox as C
import unittest
from numpy import *


def Reference(a,b, MaxNumberOfIterations):
    return( linspace( a,
                      b,
                      MaxNumberOfIterations+2 ) )

def Function(x):
    return( sin(x) )

Interval = [ -pi, pi]
deg = 0
MaxIterations = 10
ref = Reference(Interval[0], Interval[1], deg)

lowlevel = C.LowLevel(Function, deg, ref, Interval)
function = C.BestApprox(Function, Interval, MaxIterations)
coeff = function.Remez(Reference(Interval[0], Interval[1], deg), deg)
lowlevel.CreatePolynomial(ref)
point = lowlevel.GetPoint()
lowlevel.ExchangeReferenceWith(point)

class TestIdentity(unittest.TestCase):
    def test_m(self):   
        resault = polyval(coeff, -pi/2) - Function(-pi/2)
        expected = 1

        self.assertAlmostEqual(resault, expected)

    def test_p(self):
        """
        initial polynomial,
        """        
        resault = lowlevel.error 
        expected = 0.

        self.assertAlmostEqual(resault, expected)

    def test_mat(self):        
        resualt = lowlevel.mtest
        expected = array( [[1,1],[1,-1]] )
 
        self.assertTrue((resualt == expected).all())

    def test_gp(self):        
        resualt = point
        expected = (-pi/2)
        
        self.assertAlmostEqual(resualt, expected, 1)

    def test_exhange(self):        
        resualt = lowlevel.Reference[0]
        expected = (-pi/2)
        
        self.assertAlmostEqual(resualt, expected, 1)


if __name__=='__main__':
    unittest.main()
