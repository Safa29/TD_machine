# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 10:12:08 2022

@author: Ahmed
"""


import numpy as np
from sympy import *
import math
Vlmax, van, vbn, vcn, w, t, S, Il,Vll,Vln,R, L,IRL,Z = symbols("Z IRL Vlmax van vbn vcn w t S Il Vln Vll R L", real=True)


exp2={R:5.11,L: 2.95, w:2*pi*50, Vll: 460}

F=100
u0=4*np.pi*10**-7
S=2*30*40*10**-6
e=2*2.5*10**-3

B=np.sqrt(2*F*u0/S)
print('We need',B,'T to generate 100N')

ATair=B*e/u0;
print ('We will need',At,'AT to circulate',B,'T in the air gap')

l=(15+85+120)*2*10**-3
ATfer=l*200

ATt=ATair+ATfer

i=ATt/n

H=ATt/l

B=1.5
F=(B**2)*S/(2*u0)