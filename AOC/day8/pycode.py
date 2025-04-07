import numpy as np
def getData():
    with open("/home/guillaume/Documents/7331/AOC/day8/input.txt", "r") as file:
        data = [list(map(str, line.strip())) for line in file] 
    if not data:
        raise ValueError("Failed: Input data is empty or invalid")
    return data


def getDictAndVecs(arr):
    dim = arr.shape 
    dic = [] 
    vec = []
    counter = 0
    for i in range(dim[0]):
        for j in range(dim[1]):
            if arr[i][j] != '.':
                if arr[i][j] not in dic:
                    counter += 1
                    # print(counter)
                    dic.append(arr[i][j])
                    # print(dic)
                    vec.append([np.array([i, j])])
                else:
                    vec[dic.index(arr[i][j])].append(np.array([i, j]))
    return dic, vec

def redrawFreqs(arr, intfs_arr):
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if arr[i][j] != ".":
                intfs_arr[i][j] = arr[i][j]
                


def getInterfs(x1, x2):
    return 2*x1-x2, 2*x2-x1

def getInterfsP2(x1, x2, shape):
    interfs = []
    for i in range(0,shape[0]):
        c1 = x1-i*(x2-x1)
        c2 = x2-i*(x1-x2)
        interfs.append(c1)
        interfs.append(c2)
    return interfs

def drawInterfs(vec, shape):
    intfs_arr = np.full(shape,".", dtype=str)
    for subvec in vec: 
        # print(subvec)
        for i in range(len(subvec)-1):
            for j in range(i+1,len(subvec)):
                temp1, temp2 = getInterfs(subvec[i],subvec[j])
                # print(str(subvec[i])+" | "+str(subvec[j])+" --> "+str(temp1)+" & "+str(temp2))
                if 0 <= temp1[0] < shape[0] and 0 <= temp1[1] < shape[1]:
                    intfs_arr[temp1[0]][temp1[1]] = "#" 
                if 0 <= temp2[0] < shape[0] and 0 <= temp2[1] < shape[1]:
                    intfs_arr[temp2[0]][temp2[1]] = "#" 
    return intfs_arr 

def drawInterfsP2(vec, shape):
    intfs_arr = np.full(shape,".", dtype=str)
    for subvec in vec: 
        # print(subvec)
        for i in range(len(subvec)-1):
            for j in range(i+1,len(subvec)):
                temp1 = getInterfsP2(subvec[i],subvec[j], shape)
                # print(str(subvec[i])+" | "+str(subvec[j])+" --> "+str(temp1)+" & "+str(temp2))
                for element in temp1:
                    if 0 <= element[0] < shape[0] and 0 <= element[1] < shape[1]:
                        intfs_arr[element[0]][element[1]] = "#"
    return intfs_arr
            
def countIntfs(arr):
    counter = 0
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if arr[i][j] == "#":
                counter += 1
    return counter

def main():
    data = getData()
    arr = np.array(data)
    fre_dic, frec_vec = getDictAndVecs(arr)
    print(fre_dic)
    print(frec_vec)
    intfs_arr = drawInterfs(frec_vec, arr.shape)
    answer = countIntfs(intfs_arr)
    redrawFreqs(arr, intfs_arr)
    print(intfs_arr)
    print(answer)
    intfs_arr = drawInterfsP2(frec_vec, arr.shape)
    answer = countIntfs(intfs_arr)
    redrawFreqs(arr, intfs_arr)
    print(intfs_arr)
    print(answer)

    

if __name__ == "__main__":
    main()
