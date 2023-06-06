n = int(input("请输入一个正整数 n: "))

# 使用for循环求解
for_result = 0
for i in range(1, n+1):
    for_result += i

# 使用sum函数求解
sum_result = sum(range(1, n + 1))

# 打印结果
print("使用for循环求解的结果:", for_result)
print("使用sum函数求解的结果:", sum_result)
