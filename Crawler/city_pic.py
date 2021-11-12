import pandas as pd
import random
import matplotlib.pyplot as plt
import matplotlib as mpl

df = pd.read_csv('前程无忧网招聘数据.csv')['城市']
'''
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df)
'''
for x in range(len(df)):
    df.values[x]=df.values[x][0:2]

data = df.value_counts()
city = list(data.index)[:10]
nums = list(data.values)[:10]
#print(city)
#print(nums)

colors = ['#FF0000', '#0000CD', '#00BFFF', '#008000', '#FF1493', '#FFD700', '#FF4500', '#00FA9A', '#191970', '#9932CC']
random.shuffle(colors)

plt.figure(figsize=(9, 6), dpi=100)
mpl.rcParams['font.family'] = 'KaiTi'
plt.bar(city, nums, width=0.5, color=colors)
plt.title('招聘岗位数最多的城市Top10', fontsize=16)
plt.xlabel('城市', fontsize=12)
plt.ylabel('岗位数', fontsize=12)
plt.show()