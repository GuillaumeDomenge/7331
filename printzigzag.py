s = 'PAYPALISHIRING'
n = 1
l = [[] for i in range(n)]

for i in range(len(s)):
    val = abs(-abs(i%(max(2*(n-1),1))-(n-1))+(n-1))
    l[val].append(s[i])
l = [j for i in l for j in i]
l = ''.join(l)
print(l)