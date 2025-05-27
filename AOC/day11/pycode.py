input = "5178527 8525 22 376299 3 69312 0 275"
example = "125 17"

n = 75 


def stringToVect(text):
    temp_str = "" 
    vec = []
    for i in range(len(text)):
        if text[i] == " ":
            vec.append(int(temp_str))
            temp_str = ""
        else:
            temp_str += text[i]
    vec.append(int(temp_str))
    return vec

def blink(vec):
    temp_vec = []
    for i in range(len(vec)):
        if vec[i] == 0:
            temp_vec.append(1)
        elif len(str(vec[i])) % 2 == 0:
            temp_len = int(len(str(vec[i]))/2)
            temp_vec.append(int(str(vec[i])[:temp_len]))
            temp_vec.append(int(str(vec[i])[temp_len:]))
        else:
            temp_vec.append(vec[i]*2024)
    return temp_vec

vec = stringToVect(input)
for i in range(n):
    print("iter : "+str(i))
    # print(str(vec))
    vec = blink(vec)

print(len(vec))
