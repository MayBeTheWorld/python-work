id_num = input("请输入身份证号码：")

if len(id_num) == 18 and id_num[:-1].isdigit() and (id_num[-1].isdigit() or id_num[-1] == 'X'):
    print("身份证号码验证通过")
else:
    print("身份证号码不符合要求")