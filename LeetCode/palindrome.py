a = 'bsnetpqmwhqjunkooftuosgkmkxpmvuehtlpwpktltwlvpdaycnhewdbdrhluyjldecezujgxixehsmjjuyerpllrvzqskizkulqzowzfvqcdsllvgupndbaiuzihcxklvxbodpnrymwobhlvllybdlfabfvnizjpriapuzszdhohfgezayokrivbgbgingspoxsridokhwekawchjdcpylvefubulvxneuizglrjktfcdirwnpqztdpsicslzaeiaibrepifxpxfkczwoumkkuaqkbjhxvasxflmrctponwwenvmtdaqaavubyrzbqjbjxpejmucwunanxwpomqyondyjuzxmzpevxqmbkrwcpdiiph'

def ispalyndrome(s:str) -> bool:
    res = True
    for i in range(0,len(s)//2):
        if s[i]!=s[len(s)-1-i]:
            res = False
    return res




# def longestPalindrome( s: str) -> str:
#     lset = min((len(s)-len(set(list(s))))*2+1,len(s))
#     while lset>1:
#         for i in range(0,len(s)-lset+1):
#             if ispalyndrome(s[i:i+lset]):
#                 return s[i:i+lset]
#         lset-=1
#     return s[0]

def longestPalindrome(s: str) -> str:
    n = len(s)
    ispalyndrome_table = [False]*n
    for i in range(n):
        ispalyndrome_table[i] = [False]*n
    for i in range(n):
        ispalyndrome_table[0][i] = True
    stay = True
    row = 0
    locrow = 0
    for i in range(n-1):
        if s[i]==s[i+1]:
            ispalyndrome_table[1][i]=True
    while stay and row<(n-2):
        for i in range(n-row-1):
            if ispalyndrome_table[row][i]:
                print('i :'+str(i)+' row :' +str(row)+'1 = '+str(i+row+1))
                # if s[i]==s[i+row+1] and i!=(n-1):
                #     ispalyndrome_table[row+1][i] = True
                if i!=0 and s[i-1]==s[i+row+1] and i!=(n-1):
                    ispalyndrome_table[row+2][i-1] = True
        stay = any(ispalyndrome_table[row+1]) or any(ispalyndrome_table[row+2])
        row+=1
    print(ispalyndrome_table)
    for x in range(n):
        try:
            i = ispalyndrome_table[x].index(True)
            locrow=x
        except:
            i = i
    return s[i:i+locrow+1]
        
        

print(longestPalindrome(a))