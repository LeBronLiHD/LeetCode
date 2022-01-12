def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    if len(str) == 0:
        return 0

    c = str[0]
    i = 1
    
    while c == ' ' and i < len(str):
        c = str[i]
        i += 1
    
    str = str[i - 1:]
    begin = 0
    i = 1
    
    if (str[0]  < '0' or str[0] > '9') and i < len(str):
        if str[0] != '+' and str[0] != '-':
            return 0
        c = str[1]
        i = 2
        begin = 1
    
    while c >= '0' and c <= '9' and i < len(str):
        c = str[i]
        i += 1

    if c >= '0' and c <= '9':
        i += 1
    
    temp = str[begin:i - 1]
    if len(temp) == 0:
        return 0
    rev = int(temp)
    
    if str[0] == '-':
        rev *= -1
    if rev > pow(2,31) - 1:
        rev = pow(2,31) - 1
    elif rev < -pow(2,31):
        rev = -pow(2,31)
    return rev

s = "314"
ans = myAtoi(s)
print(ans)
s = "3.14"
ans = myAtoi(s)
print(ans)
s = "-314"
ans = myAtoi(s)
print(ans)
s = "-3.14"
ans = myAtoi(s)
print(ans)
s = "       -314"
ans = myAtoi(s)
print(ans)
s = "       -3.14"
ans = myAtoi(s)
print(ans)
s = "       314"
ans = myAtoi(s)
print(ans)
s = "       3.14"
ans = myAtoi(s)
print(ans)
s = "314aaaaaaaaaaaaaaaaaa"
ans = myAtoi(s)
print(ans)
s = "3.14aaaaaaaaaaaaaaa"
ans = myAtoi(s)
print(ans)
s = "-314aaaaaaaaaaaaaaa"
ans = myAtoi(s)
print(ans)
s = "-3.14aaaaaaaaaaaaaaaa"
ans = myAtoi(s)
print(ans)
s = "       -314aaaaaaaaaaaa"
ans = myAtoi(s)
print(ans)
s = "       -3.14aaaaaaaaaaaaa"
ans = myAtoi(s)
print(ans)
s = "       314aaaaaaaaaaaaaaaa"
ans = myAtoi(s)
print(ans)
s = "       3.14aaaaaaaaaaa"
ans = myAtoi(s)
print(ans)
s = ""
ans = myAtoi(s)
print(ans)
s = "+"
ans = myAtoi(s)
print(ans)