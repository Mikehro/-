import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import random

df = pd.read_csv('前程无忧网招聘数据.csv')['薪资']

part_interval = ["5K-10K", "10K-15K", "15K-20K", "20K-25K", "25K-30K", "30K-35K", "35-50K", "50K以上"]
count1, count2, count3, count4, count5, count6, count7, count8 = 0, 0, 0, 0, 0, 0, 0, 0
salary = None
for i in df.values:
    if str(i) == 'nan':
        pass
    elif i[-3:] == '万/月':
        i = i.replace('万/月', '-万/月')
        x = i.split('-')
        salary = (float(x[0]) + float(x[1])) * 10 / 2
    elif i[-3:] == '千/月':
        i = i.replace('千/月', '-千/月')
        x = i.split('-')
        salary = (float(x[0]) + float(x[1])) / 2
    elif i[-3:] == '万/年':
        i = i.replace('万/年', '-万/年')
        x = i.split('-')
        salary = (float(x[0]) + float(x[1])) / 2 * 10 / 12
    else:
        continue

    if 5 < salary <= 10:
        count1 += 1
    elif 10 < salary <= 15:
        count2 += 1
    elif 15 < salary <= 20:
        count3 += 1
    elif 20 < salary <= 25:
        count4 += 1
    elif 25 < salary <= 30:
        count5 += 1
    elif 30 < salary <= 35:
        count6 += 1
    elif 35 < salary <= 50:
        count7 += 1
    else:
        count8 += 1

nums = [count1, count2, count3, count4, count5, count6, count7, count8]
colors = ['#0000CD', '#FF0000', '#FFD700', '#7FFF00', '#FF1493', '#9400D3', '#FF8C00', '#87CEFA']
random.shuffle(colors)
mpl.rcParams['font.family'] = 'KaiTi'
plt.figure(figsize=(9, 6), dpi=100)
plt.axes(aspect='equal')
explodes = [0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5]
plt.pie(nums, pctdistance=0.75, shadow=True,
		colors=colors, autopct='%.2f%%', explode=explodes,
		startangle=15, labeldistance=1.1,
		)
plt.legend(part_interval, bbox_to_anchor=(1.0, 1.0))
plt.title('招聘岗位的薪酬分布', fontsize=15)
plt.show()