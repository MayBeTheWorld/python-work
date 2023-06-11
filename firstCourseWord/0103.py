import math


# 判断一个数是否为素数
def prime_number(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


# 验证哥德巴赫猜想
correct_count = 0
for num in range(6, 201, 2):
    found = False
    for n in range(2, num // 2 + 1):
        if prime_number(n) and prime_number(num - n):
            correct_count += 1
            found = True
            break
    if not found:
        print("偶数", num, "不符合哥德巴赫猜想")
if correct_count == len(range(6, 201, 2)):
    print("均符合哥德巴赫猜想")
    