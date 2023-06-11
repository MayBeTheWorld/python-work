import requests
from bs4 import BeautifulSoup
import jieba
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


# 爬取整页新闻函数
def news_get(base_url):
    # 发起请求
    req = requests.get(base_url)
    # 设置编码
    req.encoding = 'utf-8'
    # 获取网页内容
    html = req.text
    # 创建BeautifulSoup对象
    soup = BeautifulSoup(html, 'html.parser')
    # 存储结果的列表
    news_list = []
    # 提取新闻标题
    sou = soup.find_all('span', attrs={'class': 'news_title'})
    for new in sou:
        news_list.append(new.a.string)
    # 返回新闻标题列表
    return news_list


# 提取指定数量新闻
news = []
num = 100
page = 1
while len(news) < num:
    url = 'https://xc.hfut.edu.cn/1955/list' + str(page) + '.htm'
    news.extend(news_get(url))
    page += 1
print(len(news))

# 保留100条
if len(news) > num:
    news = news[:100]
print(len(news))


# 使用jieba进行分词
seg_list = []

# 遍历数组并进行分词
for title in news:
    seg_list.append(jieba.lcut(title))

# 将分词结果拼接成字符串
word_str = ''
for i in range(len(seg_list)):
    word_str += ' '.join(seg_list[i])

# 读取背景图片
background_image = np.array(Image.open("school.jpg"))

# 设置词云图的参数,并构建词云
wordcloud = WordCloud(
    mask=background_image,
    background_color="white",
    width=800,
    height=600,
    max_words=1000,
    max_font_size=1000,
    relative_scaling=0.6,
    random_state=50,
    scale=2,
    font_path=r'C:\Windows\Fonts\simfang.ttf',
    ).generate(word_str)

# 根据图片生成颜色
image_colors = ImageColorGenerator(background_image)

# 绘制词云图
plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis('off')
plt.show()


