import timeit
import scipy
from numpy import *
import matplotlib.pyplot as pl
from BestApprox import *

f = lambda X: sin(X)
g = lambda X: e**X
y = lambda X: e**(1/X)
q = lambda X: e**sin(X)


def Approx(function):
    Reference = lambda a,b,DegOfP: linspace(a, b, round(abs(DegOfP))+2) 
    Interval = -2*pi, 5*pi
    Deg = 8
    Function = BestApprox(function, Interval)    
    Polynomial = Function.Remez(Reference(Interval[0], Interval[1], Deg), Deg)



FirstFunction = []
SecondFunction = []
ThirdFunction = []
ForthFunction = []
k = []
for i in range(1,20):
    start_time = timeit.default_timer()
    Approx(f)
    FirstFunction.append(timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    Approx(g)
    SecondFunction.append(timeit.default_timer() - start_time)

    
    start_time = timeit.default_timer()
    Approx(y)
    ThirdFunction.append(timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    Approx(q)
    ForthFunction.append(timeit.default_timer() - start_time)
    
    k.append(i)

ax = pl.subplot(111)
funktion = ['sinx', 'e**x', 'e**1/x', 'e**sinx']
i = -1
for func in [FirstFunction, SecondFunction, ThirdFunction, ForthFunction]:
    i += 1
    ax.plot(k, func, label=funktion[i])

ax.legend()
pl.savefig('time.png')



