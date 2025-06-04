with open("/home/guillaume/Documents/7331/AOC/day15/example.txt", "r") as file:
    data = [line.strip("\n") for line in file]
import numpy as np
is_two = 0
board = []
instructions = []
for elem in data:
    if is_two == 1:
        instructions.append(elem)
    else:
        if elem != "":
            board.append(elem)
        else:
            is_two = 1
board = np.array([[elem for elem in line] for line in board])
instructions_t = []
for line in instructions:
    instructions_t += line

def applyOne(board, instruction):

print(instructions_t)
