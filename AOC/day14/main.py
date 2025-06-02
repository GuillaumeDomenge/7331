

with open("/home/guillaume/Documents/7331/AOC/day14/example.txt", "r") as file:
    data = [line.strip("\n") for line in file]


def simN(p,v,dim,n):
    t_x = (p[0]+v[0]*n) % dim[1]
    t_y = (p[1]+v[1]*n) % dim[0]
    return [t_x,t_y]

def printBoard(dim, pos):
    lines = []
    for i in range(dim[0]):
        line = ""
        for j in range(dim[1]):
            t_c = pos.count([j,i])
            if t_c == 0:
                line += "."
            else:
                # print(str(t_c)+" at pos "+str([j,i]))
                line += str(t_c)
        lines.append(line)
    for line  in lines:
        print(line)


def simOne(posit, speeds, dim):
    t_posit = []
    for i in range(len(posit)):
        t_val = [(posit[i][0]+speeds[i][0]) % dim[1],(posit[i][1]+speeds[i][1]) % dim[0]]
        t_posit.append(t_val)
    return t_posit

def cCuad(dim, pos):
    v_split = (dim[1]-1)//2
    h_split = (dim[0]-1)//2
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0

    for elem in pos:
        if elem[0]<h_split:
            if elem[1]<v_split:
                c1 += 1
            elif elem[1]>v_split:
                c2 += 1
        elif elem[0]>h_split:
            if elem[1]<v_split:
                c3 += 1
            elif elem[1]>v_split:
                c4 += 1
    return c1*c2*c3*c4, [c1,c2,c3,c4]

posit_b = []
speeds = []

for i in range(len(data)):
    t_left, t_right = data[i].split(" ")
    t_left = t_left.replace("p=", "").split(",")
    posit_b.append([int(t_left[0]), int(t_left[1])])
    t_right  = t_right.replace("v=", "").split(",")
    speeds.append([int(t_right[0]), int(t_right[1])])

posit_e = []
dim = [103,101]
dim = [7,11]
for i in range(len(posit_b)):
    posit_e.append(simN(posit_b[i],speeds[i],dim,100))
printBoard(dim, posit_e)
print(cCuad(dim,posit_e))
posit_e = posit_b
for i in range(100):
    posit_e = simOne(posit_e,speeds, dim)

print(cCuad(dim, posit_e))

# for i in range(len(data)):
# dim = [7,11]
# n_pos = [2,4]
# printBoard(dim,[n_pos])
# print("")
# for i in range(1,6):
#     n_pos = simN(n_pos,[2,-3],dim,1)
#     printBoard(dim, [n_pos])
#     print("")
# print(simN([2,4],[2,-3],[6,10],5))
