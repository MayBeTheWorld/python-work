import random

# 生成200个0~1之间的浮点数并存储到列表中
random_list = [random.random() for i in range(200)]

# 计算平均数
average = sum(random_list) / len(random_list)
# 计算方差
variance = sum((x - average) ** 2 for x in random_list) / len(random_list)

# 输出结果
print("随机数列表: ", random_list)
print("均值为: ", average)
print("方差为: ", variance)
