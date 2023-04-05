n = 5


def Dup(str1, num):
    global n
    n = num
    return str1 * n
# end of def


str2 = Dup("Hello", 2)
print(str2, n)  # HelloHello 5
