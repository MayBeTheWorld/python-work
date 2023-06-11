import pandas as pd
import json


# 定义一个函数将文本从GBK编码转换为UTF-8编码
def gbk2utf8(line):
    try:
        line = line.decode("gbk").encode("utf-8")
    except:
        return line
    else:
        return line


# 读取CSV文件，指定编码为GBK
data = pd.read_csv(r'price2016.csv', encoding="gbk")

# 创建一个空字典用于存储数据
dictionary = dict()

# 将列名转换为UTF-8编码，并添加到字典中
li = list(map(gbk2utf8, list(data.columns)))
for i in range(len(li)):
    dictionary[li[i]] = list(data.loc[::][list(data.columns)[i]])

# 将字典转换为JSON格式并保存到文件
with open('price2016.json', 'w') as f:
    json.dump(dictionary, f)

# 将字典转换为JSON格式并打印输出
print(json.dumps(dictionary, ensure_ascii=False))
