"""项目介绍
这是一个机器学习算法中apriori算法的简单实现
用于求以下五个事务的频繁项集，关联规则以及强关联规则
"""

from itertools import combinations

# 定义项集
T1 = {'M', 'O', 'N', 'K', 'E', 'Y'}
T2 = {'D', 'O', 'N', 'K', 'E', 'Y'}
T3 = {'M', 'A', 'K', 'E'}
T4 = {'M', 'U', 'C', 'K', 'Y'}
T5 = {'C', 'O', 'K', 'Y'}

# 构造事务列表
transactions = [T1, T2, T3, T4, T5]

# 定义最小支持度阈值和最小置信度阈值
min_support = 0.6
min_confidence = 0.8


# 计算候选项集的支持度的函数
def get_support_count(current_itemset, all_transactions):
    """current_itemset参数为当前判断项集；all_transactions为事务列表"""
    count = 0
    for t in all_transactions:
        # 判断当前项集是否为事务列表中的项集的子集，满足则支持度+1
        '''这里的issubset函数是 Python 中一个集合（set）函数，用于判断一个集合是否为另一个集合的子集。'''
        if current_itemset.issubset(t):
            count += 1

    # 返回支持度
    return count


# 在候选项集中筛选频繁项集的函数
def pruning(current_items, all_transactions, min_supp):
    """current_items是当前被判断的候选项集；all_transactionss是事务列表；min_supp是最小支持度阈值"""
    # 用字典定义要返回的频繁项集
    result_itemsets = {}
    for item in current_items:
        # 获得某一项集支持度计数
        support_count = get_support_count(item, all_transactions)

        # 判断频繁项集
        if support_count / len(all_transactions) >= min_supp:
            result_itemsets[item] = support_count

        # 返回频繁项集
    return result_itemsets


# 获取所有频繁项集的函数
def get_frequent_itemsets(all_transactions, min_supp=min_support):
    """all_transactions为事务列表; min_supp为最小支持度阈值"""
    # 第一次扫描获取所有单个项的支持度计数
    # 用set集合定义第一轮候选项集，防止出现重复项
    items = set()

    # 连接
    for t in all_transactions:
        for item in t:
            '''frozenset是Python中的一个内置函数，它可以用于创建不可变的（即“冻结的”）集合对象。
            与普通的集合对象不同，frozenset对象是不可变的，因此不能添加、删除或修改其元素。
            在数据挖掘和机器学习中，frozenset常用于表示项集和事务。'''
            items.add(frozenset([item]))

    # 获得某一单项集支持度计数
    result_frequent_itemsets = pruning(items, all_transactions, min_supp)

    # 不断迭代直到没有新的频繁项集生成
    k = 2
    while True:
        # 定义候选项集
        candidate_itemsets = set()

        # 连接
        for itemset1 in result_frequent_itemsets:
            for itemset2 in result_frequent_itemsets:
                '''用union函数求两个集合对象的并集'''
                if len(itemset1.union(itemset2)) == k:
                    candidate_itemsets.add(itemset1.union(itemset2))

        # 当无法获得新候选项集时，说明得到最大频繁项集
        if len(candidate_itemsets) == 0:
            break

        # 剪枝
        new_frequent_itemsets = pruning(candidate_itemsets, all_transactions, min_supp)

        # 将得到的新频繁项集添加到all_frequent_itemsets中
        result_frequent_itemsets.update(new_frequent_itemsets)
        k += 1

    # 返回得到的所有频繁项集
    return result_frequent_itemsets


# 获取关联规则的置信度的函数
def get_confidence(rule, all_transactions):
    """rule为关联规则； all_transactions为事务列表"""
    # 解构传入的rule得到前置条件项集 antecedent_set，结论项集 consequent_set。
    antecedent_set, consequent_set = rule

    # 获得前置条件项集和结论项集的支持度计数
    antecedent_support = get_support_count(antecedent_set, all_transactions)

    # 计算前置条件项集和结论项集的支持度
    rule_support = get_support_count(antecedent_set.union(consequent_set), all_transactions)

    # 返回关联规则置信度
    return rule_support / antecedent_support


# 获取所有关联规则和强关联规则及其置信度的函数
def get_rules_and_strong_rules(frequent_itemsets, all_transactions, minsup, minconf):
    """frequent_itemsets为传入的所有频繁项集；all_transactions为事务列表；minsup为最小支持度阈值；minconf为最小置信度阈值"""
    # 定义关联规则置信度数值
    result_rules_confidence = []

    # 定义强关联规则数值
    result_strong_rules = []

    # 对所有频繁项集中的每个频繁项集进行判断
    '''在Python中，keys()是字典数据类型的一个方法，用于返回一个包含字典所有键的列表。'''
    for current_itemset in frequent_itemsets.keys():
        # 只考虑包含至少两个项的频繁项集
        if len(current_itemset) < 2:
            continue

        # 获取所有频繁项集并进行判断
        for i in range(1, len(current_itemset)):
            '''combinations是Python中的一个函数，它可以生成从给定集合中选择指定数量元素的所有组合。它是itertools模块中的一部分。'''
            for cunrrent_antecedent in combinations(current_itemset, i):
                # 获取条件项集
                cunrrent_antecedent = frozenset(cunrrent_antecedent)

                # 获取结论项集
                '''difference()是Python中集合(Set)对象的一个方法，用于返回两个集合之间的差集。差集指的是只存在于第一个集合中的元素集合。'''
                current_consequent = current_itemset.difference(cunrrent_antecedent)

                # 获取当前规则置信度
                current_confidence = get_confidence((cunrrent_antecedent, current_consequent), all_transactions)

                # 添加到关联规则数值
                result_rules_confidence.append((cunrrent_antecedent, current_consequent, current_confidence))

                # 把满足最小置信度阈值的频繁项集添加到强关联规则数值
                if current_confidence >= minconf:
                    result_strong_rules.append((cunrrent_antecedent, current_consequent, current_confidence))

    # 返回所有关联规则及其置信度和强关联规则及其置信度
    return result_strong_rules, result_rules_confidence


# 计算所有频繁项集
all_frequent_itemsets = get_frequent_itemsets(transactions, min_support)

# 获取所有强关联规则
all_strong_rules, all_rules = get_rules_and_strong_rules(all_frequent_itemsets, transactions, min_support, min_confidence)

# 输出结果
print("Frequent itemsets and suppoet counts:")
'''items() 是 Python 内置的一个方法，可以用于字典（dictionary）类型。它会返回一个视图对象，其中包含了字典中所有的键值对，每个键值对都表示为一个元组。
其中，每个元组的第一个元素是键（key），第二个元素是对应的值（value）。'''
for itemset, support in all_frequent_itemsets.items():
    '''format()是Python内置函数之一，用于格式化字符串。通过format()函数，您可以将值插入到字符串中，并通过指定格式规则控制这些值的显示方式。'''
    print("{}: {}".format(tuple(itemset), support))

print("\nrules and support counts:")
for antecedent, consequent, confidence in all_rules:
    print("{} => {}: {:.2%}".format(tuple(antecedent), tuple(consequent), confidence))

print("\nStrong rules and support counts:")
for antecedent, consequent, confidence in all_strong_rules:
    print("{} => {}: {:.2%}".format(tuple(antecedent), tuple(consequent), confidence))
