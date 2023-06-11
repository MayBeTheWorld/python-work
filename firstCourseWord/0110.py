# 生成字典的键值分别是26个大写字母及其对应ASCII值
ascii_dict = {chr(i): i for i in range(65, 91)}

# 添加26个小写字母及其对应ASCII值
ascii_dict.update({chr(i): i for i in range(97, 123)})

print(ascii_dict)
