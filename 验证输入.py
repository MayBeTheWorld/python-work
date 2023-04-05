# 在这里写上你的代码 :-)
while True:
    try:
        print('Enter your number')
        number = int(input())
        print('你填入了' + str(number))
    except ValueError:
        print('必须填入一个整数')
