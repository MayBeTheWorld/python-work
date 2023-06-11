import jieba
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# 读取txt文件内容
with open(r'4316.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 使用结巴分词进行分词
seg_list = jieba.lcut(text)

# 排除长度为一的字符和划分线
seg_list = [word for word in seg_list if len(word) > 1 and word != '------------']

# 将分词结果拼接成字符串
word_str = ' '.join(seg_list)

# 设置词云图的参数,并构建词云
wordcloud = WordCloud(
    background_color='white',
    width=800,
    height=600,
    max_words=1000,
    max_font_size=1000,
    relative_scaling=0.6,
    random_state=50,
    scale=2,
    font_path=r'C:\Windows\Fonts\simfang.ttf',
    stopwords=STOPWORDS.update(['没有', '他们', '你们', '我们', '可以', '就是', '她们', '自己', '不是', '因为', '这里', '似乎', '一个'])
).generate(word_str)

# 绘制词云图
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
