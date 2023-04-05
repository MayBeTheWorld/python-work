# 在这里写上你的代码 :-)
def collatz(number):
    if number % 2 == 0:
        print(int(number // 2))
        return int(number // 2)
    elif number % 2 == 1:
        print(int(3 * number + 1))
        return int(3 * number + 1)

def aaa(number):
    if number % 1 != 0:
        print("请填入整数")
    elif number != 1:
        while number != 1:
            number = collatz(number)
    else:
        return number

while True:
    print('Enter number:')
    number = input()
    aaa(int(number))
