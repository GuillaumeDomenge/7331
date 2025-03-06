import numpy as np

a = [[0,1,2,3,4,5],[10,11,12,13,14,15],[20,21,22,23,24,25],[30,31,32,33,34,35]]
b = [1,2,3]
c = [1,0,-6,2,3,-3,5,2]

Aarr = np.array(a)
z = np.zeros([3,10])
c_vec = np.array(c)
# z[1:2][1:3] = np.ones([2,3])
positive_indices = np.where(c_vec > 0)[0]
# print(np.where(c_vec > 0)[0])
random_index = np.random.choice(positive_indices)
print(Aarr[0,1:-1])
