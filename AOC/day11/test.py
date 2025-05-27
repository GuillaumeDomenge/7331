import numpy as np
import os
terminal_width = os.get_terminal_size().columns
np.set_printoptions(linewidth=terminal_width, suppress=True)
input = "5178527 8525 22 376299 3 69312 0 275"
example = "125 17"
test = "0 1 10"
n = 5 

def stringToVect(text):
    temp_str = "" 
    vec = []
    for i in range(len(text)):
        if text[i] == " ":
            vec.append(int(temp_str))
            temp_str = ""
        else:
            temp_str += text[i]
    vec.append(int(temp_str))
    return vec

def blink(vecnum, vec, calc_mat, new_elems):
    vecnum = np.matmul(calc_mat,vecnum)
    m = len(vec)
    # print(vecnum)
    t_new_elems = []
    for elem in new_elems:
        vec.append(elem)
    m2 = len(new_elems)
    for i in range(m2):
        t_elems = oneStoneBlink(new_elems[i])
        for j in range(len(t_elems)):
            if t_elems[j] in vec:
                calc_mat[vec.index(t_elems[j]),m+i] += 1
                print("m = "+str(m))
                print("i = "+str(i))
                print(str(new_elems[i])+" regave us "+str(t_elems[j])+" at ("+str(vec.index(t_elems[j]))+","+str(m+i)+")" )
            elif t_elems[j] in t_new_elems:
                calc_mat[m+m2+t_new_elems.index(t_elems[j]),m+i] += 1
                print(str(vec[m+i])+" gives us "+str(t_elems[j]))
            elif t_elems[j] not in t_new_elems:
                t_new_elems.append(t_elems[j])
                calc_mat = np.pad(calc_mat, pad_width=((0,1),(0,1)), mode = 'constant', constant_values=0)
                calc_mat[-1,m+i] += 1
    new_elems = t_new_elems

    return vecnum, vec, calc_mat, new_elems 

def oneStoneBlink(number):
    n = len(str(number))
    if number == 0:
        return [1]
    if n % 2 == 0:
        return [int(str(number)[:int(n/2)]),int(str(number)[int(n/2):])]
    return [number * 2024]

vec = stringToVect(input) 
vecnum = np.ones([len(vec),1]).astype(int)
calc_mat = np.zeros([len(vec),len(vec)]).astype(int)
new_elems = []
for i in range(len(vec)):
    t_v = oneStoneBlink(vec[i])
    for elem in t_v:
        if elem in vec:
            calc_mat[vec.index(elem),i] = 1
        else:
            new_elems.append(elem)
            calc_mat = np.pad(calc_mat, pad_width=((0,1),(0,1)), mode = 'constant', constant_values=0)
            calc_mat[-1,i] = 1


for elem in new_elems:
    t_v = oneStoneBlink(elem)
    for el in t_v:
        if el in vec:
            calc_mat[vec.index(el),len(vec)+new_elems.index(elem)] = 1
        elif el in new_elems:
            calc_mat[len(vec)+new_elems.index(el), len(vec)+new_elems.index(elem)] = 1
# print(calc_mat)
# print(vec)
# print(new_elems)
# print(vecnum)
vecnum = np.vstack((vecnum,np.zeros([len(new_elems),1]).astype(int)))
# print(vecnum)
for i in range(n):
    vecnum, vec, calc_mat, new_elems = blink(vecnum, vec, calc_mat, new_elems)
    vecnum = np.vstack((vecnum,np.zeros([len(new_elems),1]).astype(int)))
    # print(type(vec))
    t_vec = [elem for elem in vec] + new_elems 
    t_arr = np.array([[elem] for elem in vec]) 
    t_arr2 = np.array([[elem] for elem in vecnum[:t_arr.shape[0],0]])
    t_arr3 = np.array([elem for elem in t_vec])
    t_arr4 = np.array([[-1]]+[[elem] for elem in t_vec])
    # print(t_arr3.shape)
    # print(calc_mat.shape)
    print(np.hstack((t_arr2,t_arr)))
    # print(vec)
    print(np.hstack((t_arr4,np.vstack((t_arr3, calc_mat)))))
    print("At gen : "+str(i+1)+" we have "+ str(sum(vecnum))+ " stones")


# for i in range(n):
#     print("iter : "+str(i))
#     # print(str(vec))
#     vec = blink(vec)

print(sum(vecnum))
