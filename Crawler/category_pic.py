import pandas as pd
import collections
from wordcloud import WordCloud
import matplotlib.pyplot as plt

df = pd.read_csv('前程无忧网招聘数据.csv')['职位']
data = list(df.values)
word_list = []
for i in data:
    word_list.append(i)
word_counts = collections.Counter(word_list)

wc = WordCloud(
    background_color='white',
    width=1000, height=600,
    font_path='STXINWEI.TTF',
    max_font_size=100,
    min_font_size=15, 
    random_state=60   
).generate_from_frequencies(word_counts)

plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()