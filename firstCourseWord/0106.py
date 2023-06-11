num = int(input("请输入一个整数："))
reversed_num = 0
# 除去数前面的0
str(num)
int(num)

while num > 0:
    digit = num % 10  # 取出最后一位数字
    reversed_num = reversed_num * 10 + digit  # 生成逆序整数
    num = num // 10  # 去除最后一位数字

print(reversed_num)
