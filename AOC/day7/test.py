ys = [23,47,15, 820]
nums = [[2,3],[4,5,27],[15],[4,2,2,10]]

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


def isOperationWPath(res, num_list, depth, path):
    # print(depth)
    if res < 0:
        return (0, "")
    elif depth == len(num_list) and res == num_list[0]:
        return (1, str(num_list[0])+path)
    elif depth == len(num_list):
        return (0, "")
    elif depth < len(num_list):
        # temp_vec = num_list[:-(depth+1)]
        # # print("num_list[:-(depth-1)] :"+str(temp_vec))
        # temp_vec.append(int(str(num_list[-(depth+1)])+str(num_list[-depth])))
        # # print("int(str()+str()) :" + str(temp_vec))
        # temp_vec += num_list[len(num_list)+1-depth:]
        # # print("num_list[-(depth-1):] :"+str(num_list[len(num_list)+1-depth:]))
        # print(str(temp_vec)+": "+str(depth))
        # input("Press enter to continue")
        if num_list[-depth] != 0 and res % num_list[-depth] != 0:
            temp_tuple = isOperationWPath(res-num_list[-depth], num_list, depth + 1,"+"+str(num_list[-depth])+path)
            print(str(res) + " : " + str(temp_tuple)+" : "+str(depth)+ " : "+str(num_list))
            if temp_tuple[0] == 1:
                return temp_tuple
            elif unConcat(res, num_list[-depth]) != "NaN":
                return isOperationWPath(unConcat(res, num_list[-depth]), num_list, depth, "|"+str(num_list[-depth])+path)
        else:
            temp_tuple = isOperationWPath(res-num_list[-depth], num_list, depth + 1, "+"+str(num_list[-depth])+path)
            if temp_tuple[0] == 1:
                return temp_tuple
            temp_tuple = isOperationWPath(res/num_list[-depth], num_list, depth + 1, "*"+str(num_list[-depth])+path) 
            if temp_tuple[0] == 1:
                return temp_tuple
            if unConcat(res, num_list[-depth]) != "NaN":
                return isOperationWPath(unConcat(res, num_list[-depth]), num_list, depth, "|"+str(num_list[-depth])+path)
    else:
        return (0, "")

for i in range(len(ys)):
    print(isOperationGPT(ys[i],nums[i],1,""))

