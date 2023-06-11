# 建立10个姓名的列表和十个学号的列表
names = ["张一", "张二", "张三", "张四", "张五", "张六", "张七", "张八", "张九", "张十"]
student_ids = [2021210000 + i for i in range(10)]

# 使用zip函数将两个列表打包成zip对象，并转换为字典
name_id_dict = dict(zip(student_ids, names))

# 输出结果
print(name_id_dict)
