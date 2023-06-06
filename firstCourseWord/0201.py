import random

# 生成200个0~1之间的浮点数并存储到列表中
random_list = [random.random() for _ in range(200)]

# 计算平均数
mean = sum(random_list) / len(random_list)
# 计算方差
variance = sum((x - mean)**2 for x in random_list) / len(random_list)

# 输出结果
print("随机数列表: ", random_list)
print("均值为: ", mean)
print("方差为: ", variance)
