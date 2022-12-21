# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 20:54:02 2022

@author: hieli
"""

import numpy as np
from pylab import *
import scipy.integrate as integrate
from random import *

G = 6.67 * 10 ** -11 #the gravitional constant
M_sun = 1.99 * 10 ** 30 #the mass of the sun in kg



m_earth = 5.97 * 10 ** 24 #mass of the earth in kg

d1 = 54.078 * 10 ** 9 #distance of mercury in m
d2 =  233 * 10 ** 9 # distance to mars in m


r = np.linspace(d1, d2, num=100)

v = np.sqrt(G*M_sun/r) #the velocity of the orbit at distance r around the sun

plt.plot(r, v)


F = G*M_sun*m_earth/(r**2)
plt.show()
