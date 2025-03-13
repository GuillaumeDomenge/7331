import math 
with open("/home/guillaume/Documents/7331/AOC/day5/input.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
def get_data() -> list[list[str]]:
    with open("/home/guillaume/Documents/7331/AOC/day5/input.txt", "r") as file:
        # Read and process all lines, splitting into two sorted arrays
        data = [list(map(str, line.strip().split())) for line in file]
    if not data:
        raise ValueError("Failed: Input data is empty or invalid")
    return data

def is_instruction_correct(instruction : list)-> bool:
    instruction_length = len(instruction)
    for i in range(instruction_length-1):
        for j in range(i+1,instruction_length):
            #print("----")
            #print(instruction)
            tstring = instruction[j] + "|" +instruction[i]
            #print(tstring)
            if tstring in rulesl:
                return False
    return True

def instructionCorrector(instruction : list)-> list:
    instruction_length = len(instruction)
    for i in range(instruction_length-1):
        for j in range(i+1, instruction_length):
            tString = instruction[j] + "|" + instruction[i]
            if tString in rulesl:
                tempVal = instruction[i]
                instruction[i] = instruction[j]
                instruction[j] = tempVal
                return instructionCorrector(instruction)
    return instruction

inputt = get_data()

rulesl = []
pagesl = []
isrule = True
for i in range(len(lines)):
    if not isrule:
        pagesl.append(list(map(str, inputt[i][0].split(","))))
    if inputt[i] == []:
        isrule = False 
    if isrule:
        rulesl.append(inputt[i][0])
print(rulesl[0])
print(type(rulesl[0]))

print("---------------------------------------------------------------------------------------")
count = 0
sumIncorrect = 0
for page in pagesl:
    if is_instruction_correct(page):
        count+= int(page[math.floor(len(page)/2)])
    else:
        sumIncorrect += int(instructionCorrector(page)[math.floor(len(page)/2)])
               #print(page)

print(sumIncorrect)
print(count)

#print("The pages are: ")
#for i in pagesl:
#    print(i)
#for i in range(10-1):
#    tstring = str(i)+" :: "
#    for j in range(i+1,10):
#        tstring+= str(j)+"-"
#    print(tstring)
