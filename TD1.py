# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 10:12:08 2022

@author: Ahmed
"""

from IPython.display import display
import numpy as np
from sympy import *

r, l, Z1, R, L, C, z, w, Z1, Z2, Z3, Zeq, U, U2,Pr = symbols("r l Z1 R L C  z  w Z1 Z2 Z3 Zeq U U2 Pr", real=True)

Z1 = r + (I * w * l)
Z2 = I * w* L
Z3 = R + 1 / (I * C * w)

Zeq = Z1 + ((Z2 * Z3) / (Z2 + Z3));

print("The equivalent impedance is: " )
pprint (cancel(Zeq))

w1=2*pi*50

exp2={r:2,R: 5, w:w1, l: 1/w1, L:3/w1, C:0.5/w1, U:127}

print("The magnitude of impedance is: " )
print(abs(Zeq.evalf(subs=(exp2))))
print("The argument of impedance is: " )
print(np.rad2deg(float(arg(Zeq.evalf(subs=(exp2))))))


It=U/Zeq
print("The RMS of the current is: " )
print(abs(It.evalf(subs=(exp2))))
print("The argument of the current is: " )
print(np.rad2deg(float(arg(It.evalf(subs=(exp2))))))

P=It*U*cos((arg(Zeq)))
Q=It*U*sin(arg(Zeq))

print("The consumed active power: " )
print (abs(P.evalf(subs=(exp2))))

print("The consumed reactive power: " )
print (abs(Q.evalf(subs=(exp2))))

U2x=U-(r*abs(It)*cos(arg(Zeq)))-(l*w*abs(It)*sin(arg(Zeq)))
U2y=r*abs(It)*sin(arg(Zeq))-l*w*abs(It)*cos(arg(Zeq))

U2=U-r*It-I*l*w*It
#U2=sqrt(U2x**2+U2y**2)
print("The RMS voltage across Z2 is: " )
print (abs(U2.evalf(subs=(exp2))))
                                  
print("The argument of the voltage across Z2 is: " )
print(np.rad2deg(float(arg(U2.evalf(subs=(exp2))))))   

I1=U2/(I*L*w)  
print("The RMS current that cross Z2 is: " )
print (abs(I1.evalf(subs=(exp2))))
                                                              
print("The argument of the current that cross Z2 is: " )
print(np.rad2deg(float(arg(I1.evalf(subs=(exp2))))))

I2=U2/(R+1/(I*C*w))  
print("The RMS current that cross Z3 is: " )
print (abs(I2.evalf(subs=(exp2))))
                                                              
print("The argument of the current that cross Z3 is: " )
print(np.rad2deg(float(arg(I2.evalf(subs=(exp2))))))

Pr=abs( (r*It**2).evalf(subs=(exp2)))
PR=abs((R*I2**2).evalf(subs=(exp2)))

print ("The active power consumed in the circuit is Pr+PR = P: \n", abs(Pr), "+" , PR, "=", Pr+PR)

Ql=abs( (l*w*It**2).evalf(subs=(exp2)))
QL=abs((L*w*I1**2).evalf(subs=(exp2)))
QC=abs (((I2**2)/(C*w)).evalf(subs=(exp2)))
print ("The reactive power consumed in the circuit is Ql+QL-QC = Q: \n", Ql, "+" , QL,"-" ,QC,"=", Ql+QL-QC)

