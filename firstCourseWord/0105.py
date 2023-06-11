# 多彩多边形
import turtle
import random


# 生成指定数量的随机颜色
def random_colors(num):
    colors = []
    for i in range(num):
        r = random.random()
        g = random.random()
        b = random.random()
        color = (r, g, b)  # 将 RGB 颜色表示为一个元组
        colors.append(color)
    return colors


# 创建画笔对象
t = turtle.Pen()

# 设置画笔速度和大小
t.speed(10)
t.pensize(2)

# 设置边数
sides = int(input("输入想生产的多边形边数"))
current_colors = random_colors(sides)
# print(current_colors)
# 绘制多边形
for x in range(360):
    t.pencolor(current_colors[x % sides])  # 设置线条颜色
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + 1)
    t.width(x * sides / 200)

# 点击关闭窗口
turtle.done()
