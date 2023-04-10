import pyfpgrowth

transactions = [
    {'M', 'O', 'N', 'K', 'E', 'Y'},
    {'D', 'O', 'N', 'K', 'E', 'Y'},
    {'M', 'A', 'K', 'E'},
    {'M', 'U', 'C', 'K', 'Y'},
    {'C', 'O', 'K', 'Y'}
]
min_supp = 0.6

patterns = pyfpgrowth.find_frequent_patterns(transactions, len(transactions) * min_supp)

print(patterns)