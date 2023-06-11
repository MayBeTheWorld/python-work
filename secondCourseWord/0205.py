import random


# 定义计算函数
def calculate(n):
    return n, n ** 2, n ** 3


# 生成包含10个元素的随机整数列表
numbers = [random.randint(1, 200) for _ in range(10)]

# 调用函数输出每一项的整数值、整数的平方值、整数的立方值
for num in numbers:
    values = calculate(num)
    print(f"整数值: {values[0]}, 平方值: {values[1]}, 立方值: {values[2]}")
