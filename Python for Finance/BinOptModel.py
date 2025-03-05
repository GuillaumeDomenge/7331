import math
import time
import numpy as np
import matplotlib.pyplot as plt
import numba



M = 5000

S0 = 26.1
T = 1.0
r =  0.06
sigma = 0.2

def simulate_tree(M):
    dt = T / M
    u = math.exp(sigma * math.sqrt(dt))
    d = 1 / u
    S = np.zeros((M + 1, M + 1))
    S[0, 0] = S0
    z = 1 
    for t in range(1, M + 1):
        for i in range(z):
            S[i, t] = S[i, t-1] * u
            S[i+1, t] = S[i, t-1] * d
        z += 1
    return S

def sim_tree_2(M):
    up = np.arange(M + 1)
    up = np.resize(up, (M + 1, M + 1))
    # print(up)
    down = up.T * 2
    # print(up - down)
    dt = T / M
    S = S0 * np.exp(sigma * math.sqrt(dt) * (up - down))
    return S

def timeit(func,x):
    start = time.time()
    func(x)
    return time.time() - start

sim_tree_1_nb = numba.jit(simulate_tree)
sim_tree_2_nb = numba.jit(sim_tree_2)

x = np.arange(1,50) * 40
y1 = []
y2 = []
y3 = []
y4 = []

for element in x:
    y1.append(timeit(simulate_tree,element))
    y2.append(timeit(sim_tree_2,element))
    y3.append(timeit(sim_tree_1_nb,element))
    y4.append(timeit(sim_tree_2_nb,element))

plt.plot(x[5:],y1[5:], 'r')
plt.plot(x[5:],y2[5:], 'b')
plt.plot(x[5:],y3[5:], 'k')
plt.plot(x[5:],y4[5:], 'g')
plt.show()

# print("----Non NP---")
# ttime = time.time()
# print(simulate_tree(M))
# print("And time : "+str(time.time()-ttime))
# print("---- Yes NP-----")
# ttime = time.time()
# print(sim_tree_2(M))
# print("And time : "+str(time.time()-ttime))
            
