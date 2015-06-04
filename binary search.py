# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 12:45:43 2015

@author: Dator
"""

from  scipy import *
from  pylab import *


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