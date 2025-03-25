import numpy as np
import math


with open("/home/guillaume/Documents/7331/AOC/day6/input.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

def get_data():
    with open("/home/guillaume/Documents/7331/AOC/day6/input.txt", "r") as file:
        data = [list(map(str, line.strip())) for line in file]
    if not data:
        raise ValueError("Failed: Input data is empty or invalid")
    return data

def list_to_array(data):
    arr = np.array(data)
    return arr

def getPosition(arr):
    lenX, lenY = np.shape(arr)
    position = [0,0]
    for i in range(lenX):
        for j in range(lenY):
            if arr[i][j] == '^':
                position = [i, j]
    return position
    
def getXs(ori_arr):
    temp_arr = np.copy(ori_arr)
    isInside = 1
    direction = 0
    position = getPosition(temp_arr)
    loop_counter = 1
    while isInside == 1:
        if direction == 0:
            if position[0] == 0:
                isInside = 0
                temp_arr[position[0]][position[1]] = 'X'
            elif temp_arr[position[0]-1][position[1]] == '#':    
                direction = 1
            else:
                temp_arr[position[0]][position[1]] = 'X'
                position[0] = position[0]-1
        elif direction == 1:
            if position[1] == np.shape(temp_arr)[1]-1:
                isInside = 0
                temp_arr[position[0]][position[1]] = 'X'
            elif temp_arr[position[0]][position[1]+1] == '#':    
                direction = 2
            else:
                temp_arr[position[0]][position[1]] = 'X'
                position[1] = position[1]+1
        elif direction == 2:
            if position[0] == np.shape(temp_arr)[0]-1:
                isInside = 0
                temp_arr[position[0]][position[1]] = 'X'
            elif temp_arr[position[0]+1][position[1]] == '#':    
                direction = 3
            else:
                temp_arr[position[0]][position[1]] = 'X'
                position[0] = position[0]+1
        else:
            if position[1] == 0:
                isInside = 0
                temp_arr[position[0]][position[1]] = 'X'
            elif temp_arr[position[0]][position[1]-1] == '#':    
                direction = 0
            else:
                temp_arr[position[0]][position[1]] = 'X'
                position[1] = position[1]-1
        loop_counter += 1
    return temp_arr

def simulatePaths(ori_arr):
    isInside = 1
    direction = 0
    temp_arr = np.copy(ori_arr)
    pass_counter = np.zeros((np.shape(temp_arr)[0],np.shape(temp_arr)[1],4))
    position = getPosition(temp_arr)
    # print(position)
    loop_counter = 0
    while isInside == 1:
        if direction == 0:
            if position[0] == 0:
                isInside = 0
                temp_arr[position[0]][position[1]] = 'X'
            elif temp_arr[position[0]-1][position[1]] == '#':    
                direction = 1
            else:
                if pass_counter[position[0]][position[1]][direction] == 0:
                    pass_counter[position[0]][position[1]][direction] += 1
                else:
                    isInside = 2
                temp_arr[position[0]][position[1]] = 'X'
                position[0] = position[0]-1
        elif direction == 1:
            if position[1] == np.shape(temp_arr)[1]-1:
                isInside = 0
                temp_arr[position[0]][position[1]] = 'X'
            elif temp_arr[position[0]][position[1]+1] == '#':    
                direction = 2
            else:
                if pass_counter[position[0]][position[1]][direction] == 0:
                    pass_counter[position[0]][position[1]][direction] += 1
                else:
                    isInside = 2
                temp_arr[position[0]][position[1]] = 'X'
                position[1] = position[1]+1
        elif direction == 2:
            if position[0] == np.shape(temp_arr)[0]-1:
                isInside = 0
                temp_arr[position[0]][position[1]] = 'X'
            elif temp_arr[position[0]+1][position[1]] == '#':    
                direction = 3
            else:
                if pass_counter[position[0]][position[1]][direction] == 0:
                    pass_counter[position[0]][position[1]][direction] += 1
                else:
                    isInside = 2
                temp_arr[position[0]][position[1]] = 'X'
                position[0] = position[0]+1
        else:
            if position[1] == 0:
                isInside = 0
                temp_arr[position[0]][position[1]] = 'X'
            elif temp_arr[position[0]][position[1]-1] == '#':    
                direction = 0
            else:
                if pass_counter[position[0]][position[1]][direction] == 0:
                    pass_counter[position[0]][position[1]][direction] += 1
                else:
                    isInside = 2
                temp_arr[position[0]][position[1]] = 'X'
                position[1] = position[1]-1
        loop_counter += 1
        # print("Loop #"+str(loop_counter))
    return isInside 


def countXs(arr):
    counter = 0
    for line in arr:
        for element in line:
            if element == 'X':
                counter += 1
    return counter

def countLoops(arr, arrXs):
    temp_arr = np.copy(arr)
    temp_arrX = np.copy(arrXs)
    counter = 0
    block_number = 0
    for i in range(np.shape(temp_arr)[0]):
        for j in range(np.shape(temp_arr)[1]):
            if temp_arrX[i][j] == 'X':
                block_number += 1
                print("block_number ="+str(block_number))
                temp_arr = np.copy(arr)
                temp_arr[i][j] = '#'
                if simulatePaths(temp_arr) == 2:
                    counter += 1
                    print("In loop #"+str(counter))
    return counter

def main():
    data = get_data()
    arr = list_to_array(data)
    print(getPosition(arr))
    pos = getPosition(arr)
    print(arr[pos[0]])
    arrXs = getXs(arr)
    print(arr[pos[0]])
    nXs = countXs(arrXs)
    print("There are "+str(nXs)+" Xs")
    print(getPosition(arr))
    nLoops = countLoops(arr, arrXs)
    print("And " + str(nLoops)+" loops")



if __name__ == "__main__":
    main()
