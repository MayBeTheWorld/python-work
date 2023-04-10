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
        if current_itemset.issubset(t):
            count += 1
    return count


# 在候选项集中筛选频繁项集的函数
def pruning(current_items, all_transactions, min_supp):
    """current_items是当前被判断的候选项集；all_transactionss是事务列表；min_supp是最小支持度阈值"""
    result_itemsets = {}
    for item in current_items:
        support_count = get_support_count(item, all_transactions)
        if support_count / len(all_transactions) >= min_supp:
            result_itemsets[item] = support_count
    return result_itemsets


# 获取所有频繁项集的函数
def get_frequent_itemsets(all_transactions, min_supp=min_support):
    """all_transactions为事务列表; min_supp为最小支持度阈值"""
    items = set()

    # 连接
    for t in all_transactions:
        for item in t:
            items.add(frozenset([item]))
    result_frequent_itemsets = pruning(items, all_transactions, min_supp)
    k = 2
    while True:
        candidate_itemsets = set()

        # 连接
        for itemset1 in result_frequent_itemsets:
            for itemset2 in result_frequent_itemsets:
                if len(itemset1.union(itemset2)) == k:
                    candidate_itemsets.add(itemset1.union(itemset2))
        if len(candidate_itemsets) == 0:
            break

        # 剪枝
        new_frequent_itemsets = pruning(candidate_itemsets, all_transactions, min_supp)
        result_frequent_itemsets.update(new_frequent_itemsets)
        k += 1
    return result_frequent_itemsets


# 得到所有频繁项集
all_frequent_itemsets = get_frequent_itemsets(transactions, min_support)

# 输出结果
print("Frequent itemsets and suppoet counts:")
for itemset, support in all_frequent_itemsets.items():
    print("{}: {}".format(tuple(itemset), support))
