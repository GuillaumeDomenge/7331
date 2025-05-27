import matplotlib.pyplot as plt
from math import gcd
from scipy.optimize import root
import numpy as np
# a = 94 
# b = 22
# c = 34
# d = 67
# z = 8400
# w = 5400
a = 94 
b = 22 
c = 34
d = 67
z = 8400
w = 5400
# x = np.linspace(0,z // a, 1000)
x = np.arange(0,z//a,1)

def getThings(a,b,c,d,z,w):
    ostep1 = b / gcd(a,b)
    ostep2 = d / gcd(c,d)
    mstep1 = a % b
    mstep2 = c % d
    s1 = z % b
    s2 = w % d 
    return ostep1, ostep2, mstep1, mstep2, s1, s2
def solveOne(a,b,c,d,z,w):
    delta = a * d - b * c
    if delta == 0:
        return 0
    x = (d * z - b * w) // delta
    y = (a * w - c * z) // delta
    return 3*x+y

def func(k):
    # print("in")
    t_val1 = z-k*a
    t_val2 = t_val1 // b
    # print(t_val2)
    # print("out")
    return t_val1 - t_val2 * b
def func2(k):
    t_val1 = w-k*c
    t_val2 = t_val1 // d
    return t_val1 - t_val2 * d

y = [func(i) for i in x]
y2 = [func2(i) for i in x]
print(b // gcd(a,b))
# sol = root(func, x0 = z//a/2,jac = False, method= "df-sane")
# print(sol.x)
# print([(z-i*a)//b for i in sol.x])
# print(sol.fun)

plt.figure()
plt.plot(x,y)
print(getThings(a, b, c, d, z,w))
# ans = [str((x[i],(z-x[i]*a)//b))+" and "+str(y[i]) for i in range(len(x)) if str(y[i]) == "0"]
# ans = [str((x[i],(z-x[i]*a)//b))+" and "+str(y[i]) for i in range(len(x))]

# ans2 = [str((x[i],(w-x[i]*c)//d))+" and "+str(y2[i]) for i in range(len(x)) if str(y2[i]) == "0"]
ans2 = [str((x[i],(w-x[i]*c)//d))+" and "+str(y2[i]) for i in range(len(x))]

# plt.show()
# print(ans)
print(ans2)

# print(z-190*a)

