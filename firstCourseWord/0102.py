import math


# 判断一个数是否为素数
def prime_number(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


# 输出结果
print(f"100到200之间的素数：")
for n in range(100, 201):
    if prime_number(n):
        print(n)
