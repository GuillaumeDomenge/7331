import numpy as np
import matplotlib.pyplot as plt
n = 1000
s0 = 100
k = 100
h = 90
r = 0.03
t = 5
s = 0.15
dt = 1/365
per = 5
a = np.random.normal(0,1,[n,1])

def oneStep(st,mu,s,dt):
    val = [elem * np.exp((mu-s**2/2)*dt-s*np.sqrt(dt)*np.random.normal(0,1)) for elem in st]
    return val

def call_val(S,k,h):
    if min(S)<h:
        return 0
    return max(S[-1]-k,0)

def valEur(S,k): 
    return max(S[-1]-k,0)


ts = np.linspace(0,t,int(t/dt))
values = np.zeros([n,ts.shape[0]])
# print(values[:,0])
values[:,0] = [s0 for i in range(n)] 
averages = []
averages.append(s0)
topp = []
topp.append(s0)
botp = []
botp.append(s0)
for i in range(1,values.shape[1]):
    values[:,i] = oneStep(values[:,i-1],r,s,dt,n)
    averages.append(sum(values[:,i])/n)
    topp.append(np.percentile(values[:,i],100-per))
    botp.append(np.percentile(values[:,i],per))

fig = plt.figure()
for i in range(n):
    plt.plot(ts,values[i,:],'0.8',zorder = 1)
plt.plot(ts,averages,'r',zorder = 3)
plt.fill_between(ts,topp,botp,color = (0.9,0.1,0.1,0.4),zorder=2)
plt.show()


print("Eur value = "+str(sum([valEur(values[i,:],k) for i in range(n)])/n))
print("Eur down & out = "+str(sum([call_val(values[i,:],k,h) for i in range(n)])/n))
# print(values[:,1]) 
