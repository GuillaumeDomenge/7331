'''Imports'''
from math import *
import numpy as np
'''Definitions'''
def bsmlevel(z):
    sz = s0*np.exp((r-1/2*sig**2)*T+sig*(T)**0.5*z)
    return sz
def MCestimator(hs):
    c0 = exp(-r*T)*1/(len(hs))*sum(hs)
    return c0
'''Constants'''
s0 = 100 #Initial stock index level
k = 105 #Strike price
T = 1 #Time to maturity (years)
r = 0.05 # Constant riskless short rate
sig = 0.2 # Constant volatility
I = 100000
np.random.seed(1000)
zi = np.random.standard_normal(I)
sts = bsmlevel(zi)
hs = np.maximum(sts-k,0)
c0 = MCestimator(hs)
print(c0)




