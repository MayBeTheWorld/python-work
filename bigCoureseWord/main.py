import requests
from bs4 import BeautifulSoup
import re
import json


# 字符串处理函数，排除字符串中间的换行符和空格并生成数组
def str_list(string):
    # '\s+'来匹配一个或多个连续的空格或换行符
    pattern = r'\s+'
    result = re.split(pattern, string)
    # 移除空字符串
    result = [s for s in result if s]
    return result


# 天气信息爬虫
def weather_get(url):
    # 发起请求
    req = requests.get(url)
    # 设置编码
    req.encoding = 'utf-8'
    # 获取网页内容
    html = req.text
    # 创建BeautifulSoup对象
    soup = BeautifulSoup(html, 'html.parser')

    # 获取七天的粗略数据
    text_list = []
    # 获取外层类名为day的div标签
    day_div = soup.find_all('div', class_='day')
    for day in day_div:
        text = ''
        for i in day:
            text += i.text
        text_list.append(str_list(text))
    # print(text_list)

    # 获取七天的详细数据
    detail_list = []
    # 获取外层类名为hour-table的table标签
    hour_table = soup.find_all('table', class_='hour-table')
    for i in hour_table:
        current_str = str_list(i.text)
        # 由于天气是以图片的形式呈现的，这里把无法获取的天气元素的表头去除
        current_str.pop(9)
        detail_list.append(current_str)
    if detail_list[0].index('05:00') != 8:
        for i in range(8):
            del detail_list[0][4 * i + detail_list[0].index('05:00') + 1:4 * i + 9]
    # print(detail_list)

    return text_list, detail_list


general_data, detail_data = weather_get('https://weather.cma.cn/web/weather/58433.html')
data = {}
for i in range(7):
    # 添加某天粗略数据的键值对
    key = general_data[i].pop(0)
    general_value = general_data[i]
    data[key] = {
        'general': general_value,
        'detail': {}
    }

    # 添加某天详细数据的键值对
    increas_num = int(len(detail_data[i]) / 8)
    # print(detail_data[i])
    # print(len(detail_data[i]))
    # print(increas_num)
    for j in range(8):
        detail_key = detail_data[i][increas_num * j]
        detail_value = detail_data[i][increas_num * j + 1: increas_num * j + increas_num]
        data[key]['detail'].update({detail_key: detail_value})

# print(data)

# 转换为 JSON 格式的字符串
json_str = json.dumps(data, ensure_ascii=False)
print(json_str)

with open('data.json', "w") as file:
    json.dump(data, file, ensure_ascii=False)

with open('data.json', 'r') as file:
    json_data = json.load(file)

print(json_data)
