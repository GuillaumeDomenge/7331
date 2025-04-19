import numpy as np
with open("/home/guillaume/Documents/7331/AOC/day10/input.txt", "r") as file:
    data = [list(map(str, line.strip())) for line in file]

data = np.array(data).astype(int)
# print(data)

dp = np.zeros([len(data),len(data[0])]).astype(int)
# print(dp)
data3d = [] 
nrows = dp.shape[0]
ncols = dp.shape[1]
nfloors = 10
# print(data)
# print(data3d[:][:][0])
for i in range(0,10):
    tempval = (data == i).astype(int)
    data3d.append(np.pad(tempval, pad_width=((1,1),(1,1)), mode = 'constant', constant_values=0))
    # print(tempval)
# print(data3d[0])

pathcounter = np.empty([nrows+2, ncols+2], dtype=object)
for i in range(nrows+2):
    for j in range(ncols+2):
        if data3d[9][i,j] == 1:
            pathcounter[i,j] = {(i,j)}
        else:
            pathcounter[i,j] = {}

# print(data3d[8])
def convo(ws, xs):
    if ws.shape != xs.shape:
        raise ValueError("Missmatch between array dimensions :"+str(ws.shape) + "!=" + str(xs.shape))
    # print("ws is " + str(ws))
    # print("xs is " + str(xs))
    t_val = set() 
    if ws[0,1] == 1:
        t_val = t_val.union(xs[0,1])
    if ws[1,0] == 1:
        t_val = t_val.union(xs[1,0])
    if ws[2,1] == 1:
        t_val = t_val.union(xs[2,1])
    if ws[1,2] == 1:
        t_val = t_val.union(xs[1,2])

    return t_val
    
def summer(arr1, arr2):
    if arr1.shape != arr2.shape:
        raise ValueError("Missmatch between array dimensions :"+str(arr1.shape) + "!=" + str(arr2.shape))
    suma = 0
    for i in range(arr1.shape[0]):
        for j in range(arr1.shape[1]):
            if arr2[i,j] == 1:
                suma += len(arr1[i,j])
    return suma


for k in range(1,10):
    t_k = 9-k 
    # print(t_k)
    # print(pathcounter)
    for i in range(nrows):
        for j in range(ncols):
            if data3d[t_k][i+1,j+1] == 1:
                pathcounter[i+1,j+1] = convo(data3d[t_k+1][i:i+3,j:j+3],pathcounter[i:i+3,j:j+3])
# print(pathcounter)
print(summer(pathcounter, data3d[0]))
