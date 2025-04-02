import math

def getData() ->list[list[str]]:
    with open("/home/guillaume/Documents/7331/AOC/day7/input.txt", "r") as file:
        data = [list(map(str, line.strip().split())) for line in file]
    if not data:
        raise ValueError("Failed: Input data is empty or invalid")
    return data

def splitData(data):
    left_vec = []
    right_vec = []
    for line in data: 
        temp_vec = []
        for element in line:
            # print(element == ":")
            # print(ascii(element)+ 'is \"' + element)
            if element[-1] == ":":
                print("is in :")
                left_vec.append(int(element[:-1]))
            else:
                temp_vec.append(int(element)) 
                # print(temp_val)
        right_vec.append(temp_vec)
    return left_vec, right_vec

def isOperation(res, num_list, depth):
    if res < 0:
        return 0
    elif depth == len(num_list) and res == num_list[0]:
        return 1
    elif depth == len(num_list):
        return 0
    elif num_list[-depth] != 0 and res % num_list[-depth] != 0:
        return isOperation(res-num_list[-depth], num_list, depth + 1)
    else:
        return max(isOperation(res-num_list[-depth], num_list, depth + 1),isOperation(res/num_list[-depth], num_list, depth + 1))


def isOperationP2(res, num_list, depth):
    # print(depth)
    if res < 0:
        return 0
    elif depth == len(num_list) and res == num_list[0]:
        return 1
    elif depth == len(num_list):
        return 0
    elif depth < len(num_list):
        temp_vec = num_list[:-(depth+1)]
        # print("num_list[:-(depth-1)] :"+str(temp_vec))
        temp_vec.append(int(str(num_list[-(depth+1)])+str(num_list[-depth])))
        # print("int(str()+str()) :" + str(temp_vec))
        temp_vec += num_list[len(num_list)+1-depth:]
        # print("num_list[-(depth-1):] :"+str(num_list[len(num_list)+1-depth:]))
        print(str(temp_vec)+": "+str(depth))
        # input("Press enter to continue")
        if num_list[-depth] != 0 and res % num_list[-depth] != 0:
            return max(isOperationP2(res-num_list[-depth], num_list, depth + 1), isOperationP2(res, temp_vec, depth))
        else:
            return max(isOperationP2(res-num_list[-depth], num_list, depth + 1), isOperationP2(res/num_list[-depth], num_list, depth + 1), isOperationP2(res, temp_vec, depth))
    elif num_list[-depth] != 0 and res % num_list[-depth] != 0:
        return isOperationP2(res-num_list[-depth], num_list, depth + 1)
    else:
        return max(isOperationP2(res-num_list[-depth], num_list, depth + 1),isOperationP2(res/num_list[-depth], num_list, depth + 1))


def unConcat(Y, xi):
    n = len(str(xi))
    if len(str(Y)) < n:
        return "NaN"
    if Y == xi:
        return 0
    if str(Y)[-n:] == str(xi):
        return int(str(Y)[:-n])
    return "NaN"

def isOperationGPT(res, num_list, depth, path):
    if res < 0:
        return (0, "")
    
    if depth == len(num_list):
        if res == num_list[0]:
            return (1, str(num_list[0]) + path)
        return (0, "")

    current_num = num_list[-depth]

    # Try subtraction
    temp_result = isOperationGPT(res - current_num, num_list, depth + 1, "+" + str(current_num) + path)
    if temp_result[0] == 1:
        return temp_result

    # Try multiplication only if divisible
    if current_num != 0 and res % current_num == 0:
        temp_result = isOperationGPT(res // current_num, num_list, depth + 1, "*" + str(current_num) + path)
        if temp_result[0] == 1:
            return temp_result

    # Try concatenation (assuming `unConcat` is a valid function)
    unconcat_res = unConcat(res, current_num)
    if unconcat_res != "NaN":
        # print(str(res) + " : " + str(unconcat_res)+" : "+str(depth)+ " : "+str(num_list))
        return isOperationGPT(unconcat_res, num_list, depth + 1, "|" + str(current_num) + path)

    return (0, "")

def main():
    data = getData() 
    print(data)
    results, nums = splitData(data)
    print(nums)
    sumation = 0
    for i in range(len(results)):
        if isOperation(results[i], nums[i], 1) == 1:
            sumation += results[i]
    print("result for part 1 is : " + str(sumation))
    sumation = 0
    for i in range(len(results)):  
        if isOperationGPT(results[i], nums[i], 1, "")[0] == 1:
            sumation += results[i]
    print("resutl for part 2 is : " + str(sumation))

if __name__ == "__main__":
    main()
