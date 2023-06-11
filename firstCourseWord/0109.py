import random
from collections import Counter

# 生成随机整数列表
numbers = [random.randint(0, 1000) for i in range(100000)]

# 方法1: 使用collections模块中的Counter类统计每个整数出现次数
print('方法1')
counter = Counter(numbers)

# 输出频率最高的前10个数和最低的前10个数
print("频率最高的前10个数:")
for number, count in counter.most_common(10):
    print(f"整数 {number} 出现次数为 {count}")
print("\n频率最低的前10个数:")
for number, count in counter.most_common()[:-11:-1]:
    print(f"整数 {number} 出现次数为 {count}")

# 方法2: 使用字典统计每个整数出现次数
print('\n方法2')
counts = {}
for number in numbers:
    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1

# 输出频率最高的前10个数和最低的前10个数
print("频率最高的前10个数:")
# 使用sorted()函数将字典counts按照值进行排序
sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
for number, count in sorted_counts[:10]:
    print(f"整数 {number} 出现次数为 {count}")
print("\n频率最低的前10个数:")
for number, count in sorted_counts[-10:]:
    print(f"整数 {number} 出现次数为 {count}")
