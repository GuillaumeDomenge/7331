
from math import gcd
from scipy.optimize import root
with open("/home/guillaume/Documents/7331/AOC/day13/input.txt", "r") as file:
    data = [line[7:] for line in file]

def isAns(an, bn, zn):
    a0 = an[0]
    a1 = an[1]
    b0 = bn[0]
    b1 = bn[1]
    z0 = zn[0]
    z1 = zn[1]
    if z0 % gcd(a0, b0) != 0 or z1 % gcd(a1, b1) != 0:
        return 0
    # t_1
    k = max(zn[0] // an[0], zn[0] // bn[0])
    print(str(k)+" from "+str(an[0])+" or "+str(bn[0]))
    for i in range(1,k+1):
        # print(i)
        if (zn[0]-i*an[0]) % bn[0] == 0:
            # print(str(i)+" and "+str(zn[0]))
            if zn[1] == i*an[1] + ((zn[0]-i*an[0]) // bn[0])*bn[1]:
                return 3*i+((zn[0]-i*an[0]) // bn[0])
    return 0

def isTwo(an, bn, zn):
    a0 = an[0]
    a1 = an[1]
    b0 = bn[0]
    b1 = bn[1]
    z0 = zn[0]
    z1 = zn[1]
    if z0 % gcd(a0, b0) != 0 or z1 % gcd(a1, b1) != 0:
        return [0,0]
    # t_1
    k = max(zn[0] // an[0], zn[0] // bn[0])
    # print(str(k)+" from "+str(an[0])+" or "+str(bn[0]))
    for i in range(1,k+1):
        # print(i)
        if (zn[0]-i*an[0]) % bn[0] == 0:
            # print(str(i)+" and "+str(zn[0]))
            if zn[1] == i*an[1] + ((zn[0]-i*an[0]) // bn[0])*bn[1]:
                x = i
                y = ((zn[0]-i*an[0]) // bn[0])
                return [x,y] 
    return [0,0]

def solveOne(a,b,c,d,z,w):
    delta = a * d - b * c
    if delta == 0 or z % gcd(a,b) != 0 or w % gcd(c,d) != 0:
        return 0
    x = (d * z - b * w) // delta
    y = (a * w - c * z) // delta
    if x != int(x) or y != int(y) or y < 0 or x < 0:
        return 0
    if x*a+y*b != z or x*c+y*d != w:
        return 0
    return 3*x+y

def solveTwo(a,b,c,d,z,w):
    delta = a * d - b * c
    if delta == 0 or z % gcd(a,b) != 0 or w % gcd(c,d) != 0:
        return [0,0] 
    x = (d * z - b * w) // delta
    y = (a * w - c * z) // delta
    if x != int(x) or y != int(y) or y < 0 or x < 0:
        return [0,0]
    if x*a+y*b != z or x*c+y*d !=w:
        return [0,0]
    return [x,y] 


a = []
b = []
prizes = []
data = [line.replace("X+","").replace("Y+","").replace("Y=","").replace("X=","").replace("\n","") for line in data]
data = [line for line in data if len(line) > 0]
for line in data:
    # print(str(line)+"  "+str(len(line)))
    if line[0] == "A":
        t_v1, t_v2 = line.replace("A: ","").split(", ")
        t_v1 = int(t_v1)
        t_v2 = int(t_v2)
        a.append([t_v1,t_v2])
    elif line[0] == "B":
        t_v1, t_v2 = line.replace("B: ","").split(", ")
        t_v1 = int(t_v1)
        t_v2 = int(t_v2)
        b.append([t_v1,t_v2])
    else:
        t_v1, t_v2 = line.split(", ")
        t_v1 = int(t_v1)
        t_v2 = int(t_v2)
        prizes.append([t_v1,t_v2])


# print(a)
# print(b)
# print(prizes)
prizes2 = [[prize[0]+10000000000000,prize[1]+10000000000000] for prize in prizes]
count = 0
count2 = 0
for i in range(len(a)):
    # print(solveOne(a[i][0],b[i][0],a[i][1],b[i][1],prizes[i][0],prizes[i][1]))
    # t1 = isTwo(a[i],b[i],prizes[i]) 
    # t2 = solveTwo(a[i][0],b[i][0],a[i][1],b[i][1],prizes[i][0],prizes[i][1])
    # if t1 != t2:
        # print("At a[i] = "+str(a[i])+", b[i] = "+str(b[i])+", z[i] = "+str(prizes[i])+" answer dicrepancy of "+str(t1)+" "+str(t2))
    count += solveOne(a[i][0],b[i][0],a[i][1],b[i][1],prizes2[i][0],prizes2[i][1]) 


print(count)
# for i in range(len(a)):
#     print(i)
#     count2 += isAns(a[i], b[i], prizes2[i])
# print(count2)
