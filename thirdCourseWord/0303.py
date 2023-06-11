import re


def is_id_number(id_card):
    # 身份证号正则表达式
    pattern = r'^\d{17}[\dXx]$'
    if re.match(pattern, id_card):
        return True
    else:
        return False


def is_phone_number(phone_number):
    # 手机号正则表达式
    pattern = r'^1[3456789]\d{9}$'
    if re.match(pattern, phone_number):
        return True
    else:
        return False


# 输入身份证号或手机号
input_str = input("请输入身份证号或手机号：")

# 根据输入内容进行验证
if is_id_number(input_str):
    print("身份证号合法")
elif is_phone_number(input_str):
    print("手机号合法")
else:
    print("输入内容不合法")