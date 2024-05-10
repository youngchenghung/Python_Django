# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:27:07 2024

@author: USER
"""

#%%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 讀取raw data
df = pd.read_csv('/Users/kohakudaitoku/Documents/聯成/Python_Django/django_test/Django_test/mytestweb/PTT_Gossiping_data.csv')
print(df.info())

# 將'date'欄位拆分成'month'和'day'兩個欄位
df[['month', 'day']] = df['date'].str.split('/', expand=True)
# 刪除原始的'date'欄位
df = df.drop(columns=['date'])
# 將日期字符串轉換為數值型態
df['month'] = pd.to_numeric(df['month'])
df['day'] = pd.to_numeric(df['day'])
# print(df.info())
# print(df[['month', 'day']])

# 'pop'欄位的所有NaN值替換為0
df['pop'] = df['pop'].fillna(0)
# 'pop'欄位轉換為數值型態
df['pop'] = df['pop'].replace('爆', 100)
df['pop'] = df['pop'].replace('XX', -100)
df['pop'] = df['pop'].replace(r'X(\d+)', r'-\1', regex=True)
df['pop'] = df['pop'].astype(int)
# print(df.info())

# 月份資料處理
month_1_data = df[df['month'] == 1]
month_2_data = df[df['month'] == 2]
month_3_data = df[df['month'] == 3]
month_4_data = df[df['month'] == 4]
month_5_data = df[df['month'] == 5]

# 個月文章數
num_rows_month_1 = len(month_1_data)
print(num_rows_month_1)
num_rows_month_2 = len(month_2_data)
print(num_rows_month_2)
num_rows_month_3 = len(month_3_data)
print(num_rows_month_3)
num_rows_month_4 = len(month_4_data)
print(num_rows_month_4)
num_rows_month_5 = len(month_5_data)
print(num_rows_month_5)

# 文章分類資料
category_news_month_1_data = len(month_1_data[df['category'] == '[新聞]'])
category_gossip_month_1_data = len(month_1_data[df['category'] == '[爆卦]'])
category_ask_month_1_data = len(month_1_data[df['category'] == '[問卦]'])

category_news_month_2_data = len(month_2_data[df['category'] == '[新聞]'])
category_gossip_month_2_data = len(month_2_data[df['category'] == '[爆卦]'])
category_ask_month_2_data = len(month_2_data[df['category'] == '[問卦]'])



#%%
import matplotlib.pyplot as plt



month = [1, 2, 3, 4, 5]
article = [num_rows_month_1, num_rows_month_2, num_rows_month_3, num_rows_month_4, num_rows_month_5]

plt.xlim(0, 6) 
plt.plot(month, article, marker = 'o', linestyle = '--')

plt.xlabel('Month', color = 'red')
plt.ylabel('Article', color = 'red')
plt.title('PTT article counts', color = 'red')
plt.show()

#%%

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

category_type = ['新聞', '爆卦', '問卦']
category_count = [category_news_month_1_data, category_gossip_month_1_data, category_ask_month_1_data]

fig = plt.figure(figsize=(5,3))

plt.xlim(-1,3)
plt.plot(category_type, category_count, marker = 'o', linestyle = '--')

plt.xlabel('文章類別', color = 'red')
plt.ylabel('文章數量（篇）', color = 'red')
plt.tick_params(axis='x', width=5, rotation=45)
plt.title('PTT八卦版 一月文章類別分布', color = 'red')

plt.show()

#%%

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

category_type = ['新聞', '爆卦', '問卦']
category_count = [category_news_month_2_data, category_gossip_month_2_data, category_ask_month_2_data]

fig = plt.figure(figsize=(5,3))

plt.xlim(-1,3)
plt.plot(category_type, category_count, marker = 'o', linestyle = '--')

plt.xlabel('文章類別', color = 'red')
plt.ylabel('文章數量（篇）', color = 'red')
plt.tick_params(axis='x', width=5, rotation=45)
plt.title('PTT八卦版 二月文章類別分布', color = 'red')

plt.show()

#%%

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

"""
 1.參數設定
"""
xmin, xmax, A, N = 0, 4*np.pi, 4, 100
x = np.linspace(xmin, xmax, N)
y = A*np.sin(x)

"""
 2.繪圖
"""
fig = plt.figure(figsize=(7, 6), dpi=100)
ax = fig.gca()
line, = ax.plot(x, y, color='blue', linestyle='-', linewidth=3)
dot, = ax.plot([], [], color='red', marker='o', markersize=10, markeredgecolor='black', linestyle='')
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)

def update(i):
    dot.set_data(x[i], y[i])
    return dot,

def init():
    dot.set_data(x[0], y[0])
    return dot,

ani = animation.FuncAnimation(fig=fig, func=update, frames=N, init_func=init, interval=1000/N, blit=True, repeat=True)
plt.show()
ani.save('MovingPointMatplotlib.gif', writer='imagemagick', fps=1/0.04)
# %%
