

def get_data() -> list[list[int]]:
    with open("./input.txt", "r") as file:
        # Read and process all lines, splitting into two sorted arrays
        data = [list(map(str, line.strip().split())) for line in file]
    if not data:
        raise ValueError("Failed: Input data is empty or invalid")

    return data

inputt = get_data()
count=0
Xs = []
Ms = []
As = []
Ss = []
for i in range(len(inputt)):
    #print(inputt[i])
    tstring = ""
    for j in range(len(inputt[0][0])):
        if inputt[i][0][j]=="X":
            tstring+="X"
            try: #This block checks for "XMAS" to the right of the "X" (D1)
                if inputt[i][0][j+1]=="M":
                    try:
                        if inputt[i][0][j+2]=="A":
                            try:
                                if inputt[i][0][j+3]=="S":
                                    count+=1
                            except:
                                pass
                    except:
                        pass
            except:
                pass# End of D1
            try: # This block checks for "XMAS" to the lower diagonal right of the "X" (D2)
                if inputt[i+1][0][j+1]=="M":
                    try:
                        if inputt[i+2][0][j+2]=="A":
                            try:
                                if inputt[i+3][0][j+3]=="S":
                                    count+=1
                            except:
                                pass
                    except:
                        pass
            except:
                pass # End of D2
            try: # This block checks for "XMAS" below the "X" (D3)
                if inputt[i+1][0][j]=="M":
                    try:
                        if inputt[i+2][0][j]=="A":
                            try:
                                if inputt[i+3][0][j]=="S":
                                    count+=1
                            except:
                                pass
                    except:
                        pass
            except:
                pass # End of D3
            try: # This block checks for "XMAS" diagonal left of the "X" (D4)
                if inputt[i+1][0][j-1]=="M" and j>2:
                    try:
                        if inputt[i+2][0][j-2]=="A":
                            try:
                                if inputt[i+3][0][j-3]=="S":
                                    count+=1
                            except:
                                pass
                    except:
                        pass
            except:
                pass # End of D4
            try: # This block checks for "XMAS" to the left of the "X" (D5)
                if inputt[i][0][j-1]=="M" and j>2:
                    try:
                        if inputt[i][0][j-2]=="A":
                            try:
                                if inputt[i][0][j-3]=="S":
                                    count+=1
                            except:
                                pass
                    except:
                        pass
            except:
                pass # End of D5
            try: # This block checks for "XMAS" upper diag left of the "X" (D6)
                if inputt[i-1][0][j-1]=="M" and i>2 and j>2:
                    try:
                        if inputt[i-2][0][j-2]=="A":
                            try:
                                if inputt[i-3][0][j-3]=="S":
                                    count+=1
                            except:
                                pass
                    except:
                        pass
            except:
                pass # End of D6
            try: # This block checks for "XMAS" up of the "X" (D7)
                if inputt[i-1][0][j]=="M" and i>2:
                    try:
                        if inputt[i-2][0][j]=="A":
                            try:
                                if inputt[i-3][0][j]=="S":
                                    count+=1
                            except:
                                pass
                    except:
                        pass
            except:
                pass # End of D7
            try: # This block checks for "XMAS" up right of the "X" (D8)
                if inputt[i-1][0][j+1]=="M" and i>2:
                    try:
                        if inputt[i-2][0][j+2]=="A":
                            try:
                                if inputt[i-3][0][j+3]=="S":
                                    count+=1
                            except:
                                pass
                    except:
                        pass
            except:
                pass # End of D8
    #print(tstring)
#print(inputt[0][0][1])
print(count)