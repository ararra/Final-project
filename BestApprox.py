from numpy import *
import matplotlib.pyplot as pl
from numpy.linalg import solve
import time

class LowLevel(object):
    """
    Contains the mechanic behind the Remez Algorithm.
    """
    def __init__(self,
                 Function, 
                 Degree,
                 Reference,
                 Interval):
        self.Degree = Degree
        self.Reference = Reference
        self.BoundaryPoint = Interval
        self.Function = Function
        self.DenseGrid = [x for x in linspace(self.BoundaryPoint[0],
                                              self.BoundaryPoint[1], 1000)]

    def CreatePolynomial(self, test_ref = None):
        timecp = time.time()
        """
        Solve the equation system;
        |vandermonde(ref) + errorterm| |coefficients| = |f(ref)|
        for our polynomial coefficients.
        """
        ref = array(self.Reference)
        def VanderMonde():            
            pwr = arange(ref.size-1, -1, -1) -1
            pwr[-1] = 0
            matrix = ref.reshape(-1,1)**pwr.reshape(1,-1)
            matrix[:,-1] *= -1
            matrix[:,-1] **= arange(0, ref.size)
            return(matrix)
        
        def SolveEquationSystem():
            Coeff = solve(VanderMonde(), self.Function(ref))
            return(Coeff[:-1], Coeff[-1])
        timecp1 = time.time()
        self.tcptot = timecp - timecp1
        #create dictionary of time for funktions
        self.coefficients, self.error = SolveEquationSystem()
        """
        UNITTESTs
        """
        if test_ref != None:
            ref = array(test_ref)
            self.mtest = VanderMonde()
        
    def GetPoint(self):
        time_gp = time.time()
        """
        This method will derive the horizontal position that correspondes with the
        maximum error of the polynomial against the function.
        """
        ErrorAt = lambda X: abs(self.Function(X) - polyval(self.coefficients, X))
        ExtendedError = [ ErrorAt(x) for x in self.DenseGrid]
 
        for x in self.DenseGrid:
            if ErrorAt(x) == max(ExtendedError):
                break
        time_gp1 = time.time()
        self.time_gp_tot = time_gp - time_gp1
        return(x)

    def ExchangeReferenceWith(self, PointAtMaxError):
        time_Exchange = time.time()         
        """
        This method will place the maximum error
        from previous polynomial into the reference,
        at a appropriate position.
        """
        Coeff = self.coefficients
        LenghtOfReference = len(self.Reference)-1
        
        if self.Reference[0] == PointAtMaxError:
            if sign(self.Function(PointAtMaxError) - polyval(Coeff, PointAtMaxError)) \
                    == sign(self.Function(0) - polyval(Coeff, 0)):            
                self.Reference[0] = PointAtMaxError
            else:
                self.Reference[-1] = PointAtMaxError
                
        if self.Reference[-1] == PointAtMaxError:
            if sign(self.Function(PointAtMaxError) - polyval(Coeff, PointAtMaxError)) \
                == sign(self.Function(len(self.Reference)) - polyval(Coeff, len(self.Reference))):
                self.Reference[-1] = PointAtMaxError
            else:
                self.Reference[0] = PointAtMaxError


        lower = 0
        upper = len(self.Reference)-1
        while True:
            print("in loop")
            if lower == upper:
                break
            midindex = (upper + lower)// 2 
            midref = self.Reference[midindex]
            if self.Reference[midindex] <= PointAtMaxError and self.Reference[midindex+1] >= PointAtMaxError:
                if sign(self.Function(PointAtMaxError) - polyval(Coeff, PointAtMaxError)) \
                            == sign(self.Function(self.Reference[midindex]) - polyval(Coeff, self.Reference[midindex])):
                    self.Reference[midindex] = PointAtMaxError
                    break
                else:
                    self.Reference[midindex+1] = PointAtMaxError
                    break
            elif self.Reference[midindex] < PointAtMaxError:
                lower = midindex +1
            elif self.Reference[midindex] > PointAtMaxError:
                upper = midindex
        """
        def LowerEndPoint() : return(self.Reference[0])
        def UpperEndPoint() : return(self.Reference[-1])
        
        PointAt = lambda i: self.Reference[i]
        PointAtNext = lambda i: self.Reference[i+1]
        
        def MaxErrorAround(index):
            if    PointAt(index) <= PointAtMaxError \
               and PointAtNext(index) >= PointAtMaxError: return(True)
            else: return(False)
        def MaxErrorIsBelow():
            if PointAtMaxError < LowerEndPoint(): return(True)
        def MaxErrorIsAbove():
            if PointAtMaxError > UpperEndPoint(): return(True)

        def SignAlternatesAt(PointLocatedInRef):
            def SignOfErrorAtPoint(): 
                return(sign(self.Function(PointAtMaxError) 
                          - polyval(Coeff, PointAtMaxError)))
            def SignOfErrorAtRef():
                return(sign(self.Function(PointLocatedInRef)
                          - polyval(Coeff, PointLocatedInRef))) 
            if SignOfErrorAtPoint() == SignOfErrorAtRef(): return(True)
            else: return(False)

        def ExhangePointAt(i):
            self.Reference[i] = PointAtMaxError
        def SortReference():
            self.Reference = sort(self.Reference)
        
        for index in range(LenghtOfReference):
            if MaxErrorAround(index) == True:
                if SignAlternatesAt(PointAt(index)) == True:
                    ExhangePointAt(index)
                else:
                    ExhangePointAt(index+1)
            elif MaxErrorIsBelow() == True:
                if SignAlternatesAt(LowerEndPoint()) == True:
                    ExhangePointAt(0)
                    SortReference()
                else:
                    ExhangePointAt(-1)
                    SortReference()
            elif MaxErrorIsAbove() == True:
                if SignAlternatesAt(UpperEndPoint()) == True:
                    ExhangePointAt(-1)
                    SortReference()
                else:
                    ExhangePointAt(0)
                    SortReference()
        """
        time_Exchange1 = time.time()
        self.time_Exchange_tot = time_Exchange - time_Exchange1
        
class PlotBestApprox(object):
    def __init__(self, coefficients, Interval, 
                       Function = None, Reference = None, PartialCoeff = None):
        self.coefficients = coefficients
        self.a,self.b = Interval[0], Interval[1]
        self.DenseGrid = array([x for x in linspace(self.a,self.b, 1000)])
        self.Function = Function
        self.Reference = Reference
        self.PartialCoeff = PartialCoeff

    def PlotAll(self):
        pl.plot(self.DenseGrid, polyval(self.coefficients, self.DenseGrid), 'b')
        if self.Function != None: 
            pl.plot( self.DenseGrid, self.Function(self.DenseGrid), 'r' ) 
        if self.Reference != None:
            """what?
            y = [ 0 for i in self.Reference ]
            """
            y = 0
            pl.plot(self.Reference, y ,'o')
            "partial coeff?"
        if self.PartialCoeff != None:
            for coeff in self.PartialCoeff:
                pl.plot(self.DenseGrid, Polyval(coeff, self.DenseGrid), 'g--')
        pl.grid()

    def PlotFinalApproximation(self,i):
        pl.plot(self.DenseGrid, polyval(self.coefficients, self.DenseGrid), 'b')
        pl.plot(self.DenseGrid, self.Function(self.DenseGrid), 'r')
        """why
        y = [ 0 for i in self.Reference ]
        """
        pl.plot(self.Reference, [ 0 for h in self.Reference ] ,'o')
        pl.grid()
        pl.ylim(-50, 50)
        pl.xlim(self.a-5,self.b+5)
        pl.show()
    
    def PlotPartialPolynomials(self, PartialCoefficients):
        i = 0 #why
        for coeff in PartialCoefficients:           
            reference = self.Reference[i] # why
            "y = [ 0 for i in reference ]"
            i +=1
            arg = self.DenseGrid, polyval(coeff, self.DenseGrid), 'g'
            pl.plot(*arg)
            pl.plot(self.DenseGrid, self.Function(self.DenseGrid), 'r')            
            pl.plot(reference, [ 0 for i in reference ], 'o')
            pl.ylim(-40, 40)
            pl.xlim(self.a-5,self.b+5)

            pl.savefig('fig{}.png'.format(i))
            pl.close()

                      
class BestApprox(object):
    """
    Uses the LowerLevel mechanics to
    approximate a simple function.
    """
    def __init__(self,
                 Function, 
                 Interval,
                 MaxNumberOfIterations = 1000, 
                 Tolerance = 1.e-3):            
        if not isinstance(Interval, (list,tuple,None)):
            raise Exception("Interval must be of type list,array or tuple")
        for point in Interval:
            if not isinstance(point, (float,int)):
                raise Exception("should be float or int!")                
        if len(Interval) != 2: Interval = [min(Interval), max(Interval)]
        if Function == None: raise Exception("Function needs attributes")
        try: [Function(x) for x in linspace(Interval[0], Interval[1], 100)]
        except Exception: raise Exception("Function is not well defined")            
        self.BoundaryPoints = Interval
        self.Function = Function
        self.MaxNumberOfIterations = MaxNumberOfIterations
        self.Tolerance = Tolerance
                         
    def Remez(self, Reference = None, Degree=None): 
        """
        Approximate the function over the given interval
        by finding a polynomial with a maximum degree.
        """
        if not isinstance(Reference, (list, ndarray)): 
            raise Exception('Reference is required to be of type list or array')
        if not isinstance(Degree, (int,float)):
            if self.Degree != len(Reference)-2:
                raise Exception('Degree is required')
        if Degree < 0: Degree = abs(Degree)
        if isinstance(Degree, float): Degree = round(Degree)
        if len(Reference) != Degree +2: raise Exception('Dimensions did not match')    
        self.Reference = Reference        
        PreviousError = 1e5
        args = self.Function, Degree, self.Reference, self.BoundaryPoints 
        mech = LowLevel(*args)        
        self.ListOfCoeff = []
        self.ListOfRef = []
        ToleranceLargerThanDifferenceIn =\
        lambda Error: abs(PreviousError - Error) < self.Tolerance
        
        for iteration in range(self.MaxNumberOfIterations): 
            mech.CreatePolynomial()           
            Point = mech.GetPoint()
            mech.ExchangeReferenceWith(Point)
            
            self.ListOfCoeff.append(mech.coefficients)
            self.ListOfRef.append(mech.Reference)
            if ToleranceLargerThanDifferenceIn(mech.error): break
            else: PreviousError = mech.error

        self.Reference = mech.Reference 
        return(mech.coefficients)

def main():
    f = lambda X: X*sin(X)**2 - X*cos(X)
    Reference = lambda a,b,DegOfP: linspace(a, b, round(abs(DegOfP))+2) 
    Interval = -2*pi, 5*pi
    for Deg in range(30,40):
        print(Deg)
    
        Function = BestApprox(f, Interval)    
        Polynomial = Function.Remez(Reference(Interval[0], Interval[1], Deg), Deg)
    
        #PartialApproximations = Function.ListOfCoeff
        graphic = PlotBestApprox(Polynomial, Interval, f, Function.Reference)    
        #graphic.PlotPartialPolynomials(PartialApproximations)
        graphic.PlotFinalApproximation(Deg)   
if __name__=='__main__':
    main()
