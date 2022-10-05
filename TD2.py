# -*- coding: utf-8 -*-
"""
Created on Tue Oct 04 10:12:08 2022

@author: Ahmed
"""


import numpy as np
from sympy import *
import math
Vlmax, van, vbn, vcn, w, t, S, Il,Vll,Vln,R, L,IRL,Z = symbols("Z IRL Vlmax van vbn vcn w t S Il Vln Vll R L", real=True)


exp2={R:5.11,L: 2.95, w:2*pi*50, Vll: 460}

Vln=Vll/math.sqrt(3)
Vlmax=math.sqrt(2)*Vll/math.sqrt(3)

van=abs(Vlmax.evalf(subs=(exp2)))*cos(w*t)
vbn=abs(Vlmax.evalf(subs=(exp2)))*cos(w*t-(2*pi/3))
vcn=abs(Vlmax.evalf(subs=(exp2)))*cos(w*t+(2*pi/3))

print('van= ', van)
print('vbn= ', vbn)
print('vcn= ', vcn)



S=50000*np.exp(np.deg2rad(20)*1j)

P=re(S)
Q=im(S)
print ('The active power P: ', P, 'W')

print ('The reactive power Q: ', Q, 'VAR')

Il=conjugate(S)/(3*Vln)

print ('The RMS of line current is:', abs(Il.evalf(subs=(exp2))), 'A')
print ('The argument of line current is:', np.rad2deg(float(arg(Il.evalf(subs=(exp2))))), 'deg')

Z= R+I*w*L
IRL=Vln/Z

print ('The RMS impedance current is: ' ,abs(IRL.evalf(subs=(exp2))), 'A')
print ('The argument impedance current is: ' ,np.rad2deg(float(arg(IRL.evalf(subs=(exp2))))), 'deg')

Ic=Il-IRL

print ('The RMS impedance current is: ' ,abs(Ic.evalf(subs=(exp2))), 'A')
print ('The argument impedance current is: ' ,np.rad2deg(float(arg(Ic.evalf(subs=(exp2))))), 'deg')