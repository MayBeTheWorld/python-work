from efficient_apriori import apriori

# 设置最小支持度和最小置信度阈值
min_support = 0.6
min_confidence = 0.8

# 定义五个事务
T1 = {'M', 'O', 'N', 'K', 'E', 'Y'}
T2 = {'D', 'O', 'N', 'K', 'E', 'Y'}
T3 = {'M', 'A', 'K', 'E'}
T4 = {'M', 'U', 'C', 'K', 'Y'}
T5 = {'C', 'O', 'K', 'Y'}

# 将事务放入列表中
transactions = [T1, T2, T3, T4, T5]

# 使用apriori算法找出频繁项集和关联规则
itemsets, rules = apriori(transactions, min_support=min_support, min_confidence=min_confidence)

# 输出频繁项集和支持度计数
print("频繁项集:")
for itemset, support in itemsets.items():
    print(f"{support}: {itemset}")
