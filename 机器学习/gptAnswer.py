# 频繁项集生成函数
def frequent_itemsets(data, support_threshold):
    items = []
    # 去重
    for transaction in data:
        for item in transaction:
            if [item] not in items:
                items.append([item])

    items.sort()
    # 转化为set类型便于后续操作
    transaction_list = list(map(set, data))
    num_transactions = len(transaction_list)
    freq_sets = {}
    # 计算每个单项的支持度
    for item in items:
        count = 0
        for transaction in transaction_list:
            if item.issubset(transaction):
                count += 1
        support = float(count) / num_transactions
        if support >= support_threshold:
            freq_sets[item[0]] = support

    current_freq_sets = freq_sets
    all_freq_sets = {1: current_freq_sets}
    k = 2
    # 迭代生成频繁项集
    while current_freq_sets != {}:
        current_freq_sets = generate_new_sets(current_freq_sets, k - 1, support_threshold, transaction_list)
        if current_freq_sets != {}:
            all_freq_sets[k] = current_freq_sets
        k += 1

    return all_freq_sets


# 连接步
def join_sets(item_set, length):
    return set([item1.union(item2) for item1 in item_set for item2 in item_set if len(item1.union(item2)) == length])


# 剪枝步
def prune_sets(item_set, freq_sets, length):
    return set([item for item in item_set if all([subset in freq_sets for subset in combinations(item, length - 1)])])


# 生成新的频繁项集
def generate_new_sets(freq_sets, k, support_threshold, transaction_list):
    # 连接步
    candidates = join_sets(freq_sets, k + 1)
    # 剪枝步
    freq_sets = {}
    for candidate in candidates:
        pruned_candidate = prune_sets(candidate, freq_sets, k + 1)
        count = 0
        for transaction in transaction_list:
            if pruned_candidate.issubset(transaction):
                count += 1
        support = float(count) / len(transaction_list)
        if support >= support_threshold:
            freq_sets[frozenset(pruned_candidate)] = support

    return freq_sets


# 计算置信度
def confidence(freq_sets, rules, confidence_threshold):
    pruned_rules = []
    for rule in rules:
        antecedent = frozenset(rule[0])
        consequent = frozenset(rule[1])
        # 计算支持度和置信度
        support_antecedent = freq_sets[antecedent]
        support_total = freq_sets[antecedent.union(consequent)]
        conf = support_total / support_antecedent
        if conf >= confidence_threshold:
            pruned_rules.append((rule[0], rule[1], conf))

    return pruned_rules


# 执行Apriori算法并打印结果
data = [['M', 'O', 'N', 'K', 'E', 'Y'], ['D', 'O', 'N', 'K', 'E', 'Y'], ['M', 'A', 'K', 'E'], ['M', 'U', 'C', 'K', 'Y'],
        ['C', 'O', 'K', 'Y']]
freq_sets = frequent_itemsets(data, 0.6)

# 找到所有的规则
all_rules = []
for k, item_list in freq_sets.items():
    if k == 1:
        continue
    # 生成所有���能的规则
    for item in item_list:
        s = [frozenset([x]) for x in item]
        rules = [(antecedent, item.difference(antecedent)) for antecedent in s]
        all_rules.extend(rules)

pruned_rules = confidence(freq_sets, all_rules, 0.8)