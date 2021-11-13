import pandas as pd
import collections
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def category_pic():
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
    #plt.show()
    fig = BytesIO()
    plt.savefig(fig, format='png', bbox_inches='tight', pad_inches=0.0)
    fig.seek(0)
    fig_png = base64.b64encode(fig.getvalue()) 
    fig_str = str(fig_png, "utf-8")
    html = '<img src=\"data:image/png;base64,{}\"/>'.format(fig_str)
    return html
