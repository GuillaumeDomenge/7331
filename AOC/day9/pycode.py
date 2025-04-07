import numpy as np

def decompressor(key):
    id = 0
    is_file = 1
    temp_string = ""
    for element in key:
        if is_file == 1:
            temp_string += str(id)*int(element)
            is_file = 0
            id += 1
        else:
            temp_string += "."*int(element)
            is_file = 1
    return temp_string

def checksum(process):
    counter = 0
    for i in range(len(process)):
        if process[i] != ".":
            counter += i*int(process[i])
    return counter
def part_one( inp: str) -> int:
        disk = []
        num = 0

        for i, count in enumerate(inp):
            count = int(count)
            if i % 2 == 0:
                disk += [num] * count
                num += 1
            else:
                disk += [None] * count

        i = 0
        while i < len(disk):
            if disk[i] is None:
                if (last := disk.pop()) is None:
                    # simply try again as this continues the loop without increasing `i`
                    continue

                disk[i] = last
            i += 1

        return sum(
            i * num for i, num in enumerate(disk)
        )
def fileMover(process):
    temp_string = [x for x in process]
    ind = len(process)-1 
    first_dot = process.index(".")
    # print("ind : " + str(ind)) 
    while ind > first_dot:
        # print(ind)
        # print("length : "+str(len(temp_string)))
        if temp_string[ind] == ".":
            ind -= 1
        else:
            temp_string[first_dot] = temp_string[ind]
            temp_string[ind] = "."
            # print(temp_string)
            # temp_string[ind] = "."
            first_dot += temp_string.index(".")
            ind -= 1
    return temp_string 

def partTwo(inp):
    space = []
    mem = [] 
    ind = 0
    pos = 0
    disk = []
    print(inp)
    for i in range(len(inp)):
        if i % 2 == 0:
            mem.append((pos,int(inp[i])))
            disk += [ind]*int(inp[i])
            ind += 1
        else:
            space.append((pos, int(inp[i])))
            disk += ["."]*int(inp[i])
        pos += int(inp[i])
    while len(mem) > 0:
        # print("----------------------------------")
        # print(disk)
        # print(mem)
        # print(space)
        current = mem.pop()
        spot = next(((idx, (n, k)) for  idx, (n, k) in enumerate(space) if k >= current[1]), (None, None))
        if spot[0] is None or spot[1][0] > current[0]:
            continue
        # print("disk["+str(spot[1][0])+" : "+str(spot[1][0]+current[1])+"] = "+str(disk[spot[1][0] : spot[1][0]+current[1]])+" is replaced by :"+str(disk[current[0] : current[0]+current[1]]))
        disk[spot[1][0] : spot[1][0]+current[1]] = disk[current[0] : current[0]+current[1]]
        disk[current[0] : current[0] + current[1]] = ["."]*int(current[1])
        
        if current[1] < spot[1][1]:
            space[spot[0]] = (spot[1][0]+current[1], spot[1][1] - current[1])
        else:
            del space[spot[0]]
    return disk

def main():
    with open("/home/guillaume/Documents/7331/AOC/day9/input.txt", "r") as file:
        b =file.read() 
    b = b.strip()
    print("something 1 : " + b[:20])
    a = "2333133121414131402"
    # print(a)
    # print("2")
    # process = decompressor(b)
    # print("something 2 : " + str(process[:400]))
    # mid_answ = fileMover(process) 
    # print(checksum(mid_answ))
    # print(part_one(b))

    print("-----------------------------------")
    p2_midanswer = partTwo(b)
    print(checksum(p2_midanswer))

if __name__ == "__main__":
    main()
