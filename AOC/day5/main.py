with open("input.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
def get_data() -> list[list[int]]:
    with open("./input.txt", "r") as file:
        # Read and process all lines, splitting into two sorted arrays
        data = [list(map(str, line.strip().split())) for line in file]
    if not data:
        raise ValueError("Failed: Input data is empty or invalid")

    return data

def is_instruction_correct(instruction : list)-> bool:
    instruction_length = len(instruction)
    return True

inputt = get_data()

rulesl = []
pagesl = []
isrule = True
for i in range(len(lines)):
    if not isrule:
        pagesl.append(inputt[i])
    if inputt[i] == []:
        isrule = False 
    if isrule:
        rulesl.append(inputt[i])

#print("The rules are: ")
#for i in rulesl:
#    print(i)

#print("The pages are: ")
#for i in pagesl:
#    print(i)
    

