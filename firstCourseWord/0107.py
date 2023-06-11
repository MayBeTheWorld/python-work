import math

# 输入半径
R = float(input("请输入圆的半径值："))

# 计算周长、面积、体积
C = 2 * math.pi * R
S = math.pi * R ** 2
V = (4 / 3) * math.pi * R ** 3

# 输出结果
print("圆的周长:", C)
print("圆的面积:", S)
print("半径为", R, "的圆球的体积:", V)
