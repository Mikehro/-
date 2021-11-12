import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import random

df = pd.read_csv('前程无忧网招聘数据.csv')['招聘信息']

for i in range(len(df)):
    str=df.values[i]
    list=str.split('|')
    df.values[i]=list[1]
data = df.value_counts()
#print(data)

labels = ['无需经验', '1年经验', '2年经验', '3-4年经验', '5-7年经验', '8-9年经验', '10年以上经验']
nums = [data[i] for i in labels]
#print(labels)
#print(nums)
colors = ['#0000CD', '#FF0000', '#FFD700', '#7FFF00', '#FF1493', '#9400D3', '#87CEFA']
random.shuffle(colors)
mpl.rcParams['font.family'] = 'KaiTi'
plt.style.use('ggplot')
plt.figure(figsize=(9, 6), dpi=100)
plt.barh(labels, nums, height=0.5, color=colors)
plt.title('招聘岗位对工作经验的要求', fontsize=16)
plt.xlabel('岗位数量', fontsize=12)
plt.show()
