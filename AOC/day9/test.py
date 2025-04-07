import numpy as np
a = "2333133121414131402"

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

def fileMover(process):
    temp_string = [x for x in process]
    ind = len(process)-1 
    first_dot = process.index(".")
    print("ind : " + str(ind)) 
    while ind > first_dot:
        print(ind)
        print("length : "+str(len(temp_string)))
        if temp_string[ind] == ".":
            ind -= 1
        else:
            temp_string[first_dot] = temp_string[ind]
            temp_string[ind] = "."
            print(temp_string)
            # temp_string[ind] = "."
            first_dot += temp_string[first_dot:].index(".")
            ind -= 1
    return temp_string 


process = decompressor(a)
mid_answ = fileMover(process)
print(p1 := part_one(a))
