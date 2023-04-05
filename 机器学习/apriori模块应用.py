import pandas as pd
from apyori import apriori

# 初始化各个数据
dataset = [
    {'M', 'O', 'N', 'K', 'E', 'Y'},
    {'D', 'O', 'N', 'K', 'E', 'Y'},
    {'M', 'A', 'K', 'E'},
    {'M', 'U', 'C', 'K', 'Y'},
    {'C', 'O', 'K', 'Y'}
]
min_supp = 0.6
min_conf = 0.8

# 使用apriori函数
result = list(apriori(transactions=dataset, min_support=min_supp, min_confidence=min_conf))

supports = []
confidences = []
lifts = []
bases = []
adds = []
for r in result:
    for x in r.ordered_statistics:
        supports.append(r.support)
        confidences.append(x.confidence)
        lifts.append(x.lift)
        bases.append(list(x.items_base))
        adds.append(list(x.items_add))
    resultshow = pd.DataFrame({
        'support': supports,
        'confidence': confidences,
        'base': bases,
        'add': adds})
print(resultshow.tail(8))
