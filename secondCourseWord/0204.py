import random

# 随机生成1000个10000-30000之间的正整数
nums = [random.randint(10000, 30000) for i in range(1000)]

# 去重
nums_set = set(nums)
nums = list(nums_set)

# 排序并输出
nums.sort()
print(nums)