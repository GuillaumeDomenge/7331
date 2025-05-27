import numpy as np

with open("/home/guillaume/Documents/7331/AOC/day12/ownexample.txt", "r") as file:
    data = [list(map(str, line.strip())) for line in file]
data = np.array(data)
data = np.pad(data, pad_width=((1,1),(1,1)), mode = "constant", constant_values=0)

dim = data.shape  

def checkNeigh(arr,i,j):
    t_wallcount = 0
    state = 0
    if arr[i+1,j] == arr[i,j]:
        state = "s"
    else:
        t_wallcount += 1
    if arr[i,j+1] == arr[i,j]:
        state = "e"
    else: 
        t_wallcount += 1
    if arr[i,j-1] == arr[i,j]:
        state = "w"
    else:
        t_wallcount += 1
    if arr[i-1,j] == arr[i,j]:
        state = "n"
    else:
        t_wallcount += 1
    return state, t_wallcount

def checkWalls(arr,i,j):
    t_wallcount = 0
    if arr[i+1,j] != arr[i,j]:
        t_wallcount += 1
    if arr[i-1,j] != arr[i,j]:
        t_wallcount += 1
    if arr[i,j+1] != arr[i,j]:
        t_wallcount += 1
    if arr[i,j-1] != arr[i,j]:
        t_wallcount += 1
    return t_wallcount

membership_arr = np.zeros(dim).astype(int)
fencenum_arr = np.zeros(dim).astype(int)
cornernum_arr = np.zeros(dim).astype(int)

def rec(i,j,val):
    membership_arr[i,j] = val
    if data[i,j] == data[i-1,j] and membership_arr[i-1,j] == 0:
        rec(i-1,j, val)
    if data[i,j] == data[i,j-1] and membership_arr[i,j-1] == 0:
        rec(i,j-1,val)
    if data[i,j] == data[i+1,j] and membership_arr[i+1,j] == 0:
        rec(i+1,j,val)
    if data[i,j] == data[i,j+1] and membership_arr[i,j+1] == 0:
        rec(i, j+1, val)

def innerCorners(r,c):
    n_innies = 0
    if data[r,c] == data[r-1,c] and data[r,c] == data[r,c+1] and data[r,c] != data[r-1,c+1]:
        n_innies += 1
    if data[r,c] == data[r-1,c] and data[r,c] == data[r,c-1] and data[r,c] != data[r-1,c-1]:
        n_innies += 1
    if data[r,c] == data[r+1,c] and data[r,c] == data[r,c+1] and data[r,c] != data[r+1,c+1]:
        n_innies += 1
    if data[r,c] == data[r+1,c] and data[r,c] == data[r,c-1] and data[r,c] != data[r+1,c-1]:
        n_innies += 1
    return n_innies

def outieCorners(r,c):
    n_outies = 0
    if data[r,c] != data[r-1,c] and data[r,c] != data[r-1,c+1] and data[r,c] != data[r,c+1]:
        n_outies += 1
    if data[r,c] != data[r-1,c] and data[r,c] != data[r-1,c-1] and data[r,c] != data[r,c-1]:
        n_outies += 1
    if data[r,c] != data[r+1,c] and data[r,c] != data[r+1,c+1] and data[r,c] != data[r,c+1]:
        n_outies += 1
    if data[r,c] != data[r+1,c] and data[r,c] != data[r+1,c-1] and data[r,c] != data[r,c-1]:
        n_outies += 1
    return n_outies 

def calcSides(tup):
    i,j = 0,0
    first_tup = (-1,-1)
    first_direc = 3
    side_c = 1
    direc = 1
    counter = 0
    last_step = 0
    first_step = 0
    print("new calc")
    while ((i,j) != first_tup or direc != first_direc) and counter < 100:
        if counter == 1:
            first_tup = (i,j)
            first_direc = direc
        counter += 1
        # print(((i,j) != first_tup or direc != first_direc) and counter < 25)
        print("Checking : "+str((i,j))+" against "+str(first_tup)+" and direc = "+str(first_direc)+" side_c = "+str(side_c))
        if (i,j) == (0,0):
            (i,j) = tup
        if direc == 0:
            if data[i,j-1] == data[i,j]:
                direc = 3
                side_c += 1
                last_step = 1
                if counter == 1:
                    first_step = 1
                (i,j) = (i,j-1)
            elif data[i-1,j] == data[i,j]:
                (i,j) = (i-1,j)
            elif data[i,j+1] == data[i,j]:
                direc = 1
                side_c += 1
                last_step = 1
                if counter == 1:
                    first_step = 1
                (i,j) = (i,j+1)
            else:
                direc = 2
                side_c += 2
                last_step = 2
                if counter == 1:
                    first_step = 2
        elif direc == 1:
            if data[i-1,j] == data[i,j]:
                direc = 0
                side_c += 1
                last_step = 1
                if counter == 1:
                    first_step = 1
                (i,j) = (i-1,j)
            elif data[i,j+1] == data[i,j]:
                (i,j) = (i,j+1)
            elif data[i+1,j] == data[i,j]:
                direc = 2
                side_c += 1
                last_step = 1
                if counter == 1:
                    first_step = 1
                (i,j) = (i+1,j)
            else:
                direc = 3
                side_c += 2
                last_step = 2
                if counter == 1:
                    first_step = 2
        elif direc == 2:
            if data[i,j+1] == data[i,j]:
                direc = 1
                side_c += 1
                last_step = 1
                if counter == 1:
                    first_step = 1
                (i,j) = (i,j+1)
            elif data[i+1,j] == data[i,j]:
                (i,j) = (i+1,j)
            elif data[i,j-1] == data[i,j]:
                direc = 3
                side_c += 1
                last_step = 1
                if counter == 1:
                    first_step = 1
                (i,j) = (i,j-1)
            else:
                direc = 0
                side_c += 2
                last_step = 2
                if counter == 1:
                    first_step = 2
        elif direc == 3:
            if data[i+1,j] == data[i,j]:
                direc = 2
                side_c += 1
                last_step = 1
                if counter == 1:
                    first_step = 1
                (i,j) = (i+1,j)
            elif data[i,j-1] == data[i,j]:
                (i,j) = (i,j-1)
            elif data[i-1,j] == data[i,j]:
                direc = 0
                side_c += 1
                last_step = 1
                if counter == 1:
                    first_step = 1
                (i,j) = (i-1,j)
            else:
                direc = 1
                side_c += 2
                last_step = 2
                if counter == 1:
                    first_step = 2

    print("last_step = "+str(last_step)+" & first_step = "+str(first_step))
    t_val = side_c+min(-last_step-first_step+1,-1) 
    # t_val = side_c-last_step+min(1-first_step,0)     
    return t_val 
        
        



last_mem_num = 0
first_in_mem = []
for i in range(1,dim[0]-1):
    for j in range(1,dim[1]-1):
        # print("At :"+ str(i)+","+str(j)+" value is :"+str(membership_arr[i,j]))
        if i == 1 and j == 1:
            rec(i,j,1)
            first_in_mem.append((i,j))
            last_mem_num = 1
        if membership_arr[i,j] == 0:
            last_mem_num +=1
            rec(i,j,last_mem_num)
            first_in_mem.append((i,j))
        fencenum_arr[i,j] = checkWalls(data,i,j)
        cornernum_arr[i,j] = innerCorners(i,j) + outieCorners(i,j)



# for i in range(1,dim[0]-1):
#     for j in range(1,dim[1]-1):
#         t_val1, t_val2 = checkNeigh(data, i, j)
#         if i == 1 and j == 1:
#             membership_arr[i,j] = 1
#             last_m0em_num += 1
#             fencenum_arr[i,j] = t_val2
#         else:
#             if t_val1 == "n":
#                 membership_arr[i,j] = membership_arr[i-1,j]
#             elif t_val1 == "w": 
#                 membership_arr[i,j] = membership_arr[i,j-1]
#             else:
#                 membership_arr[i,j] =  last_mem_num + 1
#                 last_mem_num += 1
#         fencenum_arr[i,j] = t_val2

mem_num = []
group_walls = []
group_corners = []
# walls2 = [calcSides(tup) for tup in first_in_mem]
ans = 0
ans2 = 0
for i in range(1,int(membership_arr.max())+1):
    mem_num.append(np.count_nonzero(membership_arr == i))
    group_walls.append(np.sum(fencenum_arr[membership_arr == i]))
    group_corners.append(np.sum(cornernum_arr[membership_arr == i]))
    ans += mem_num[-1]*group_walls[-1]
    ans2 += mem_num[-1]*group_corners[-1]

print(mem_num)
print(group_corners)
# print(group_walls)
print(first_in_mem)
print(data[1:-1,1:-1])
# print(membership_arr[1:-1,1:-1])
print(ans)
print(ans2)
