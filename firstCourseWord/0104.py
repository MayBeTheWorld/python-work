import turtle
import math

# 输入三角形的三个边长
a = float(input("请输入第一条边的长度："))
b = float(input("请输入第二条边的长度："))
c = float(input("请输入第三条边的长度："))

# 判断是否构成三角形
if a + b > c and a + c > b and b + c > a:
    # 创建Turtle对象
    t = turtle.Turtle()
    t.speed(5)

    # 计算面积
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    # 长度较小按比例扩大边长
    if max(a, b, c) <= 100:
        scale = 5 * (100 // max(a, b, c))
        a *= scale
        b *= scale
        c *= scale

    # 计算三角形的角，用degress函数转换为角度制
    angle1 = 180 - math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))
    angle2 = 180 - math.degrees(math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)))
    angle3 = 180 - math.degrees(math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)))

    # 计算起点的位置
    start_x = -a / 2  # 向左位移
    if math.sin(angle3) > 0:
        start_y = -b * math.sin(angle3) / 2  # 向下位移
    else:
        start_y = b * math.sin(angle3) / 2  # 向下位移
    # print(start_y)

    # 将Turtle对象的位置移动到合适的起点位置
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()

    # 绘制三角形并填充红色
    t.fillcolor("red")
    t.begin_fill()
    t.forward(a)
    t.left(angle3)
    t.forward(b)
    t.left(angle1)
    t.forward(c)
    t.left(angle2)
    t.end_fill()

    # 显示面积
    t.penup()
    t.goto(0, start_y - 30)
    t.write(f"面积: {area}", align="center", font=("Arial", 16, "normal"))

else:
    # 不能构成三角形，显示提示信息
    print("无法构成三角形")

# 点击关闭窗口
turtle.done()
