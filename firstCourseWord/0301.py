import pandas as pd

# 设置列宽度为最大值
pd.set_option('display.max_colwidth', None)
# 设置显示所有列
pd.set_option('display.max_columns', None)
# 设置显示所有列
pd.set_option('display.max_rows', None)

# 读取.xls文件
dataframe1 = pd.read_excel('HISCO2.xls')
# 读取.xlsx文件
dataframe2 = pd.read_excel('HISGDP.xlsx')
# dataframe = pd.read_excel('HISGDP.xlsx', skiprows=24)

# 查看数据
print(dataframe1.head(6))
print(dataframe2.head())
# print(dataframe)







