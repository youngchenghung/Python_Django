# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:27:07 2024

@author: USER
"""

import pandas as pd
import matplotlib.pyplot as plt
    
df = pd.read_csv('/Users/USER/Downloads/Python_Django-main/django_test/Django_test/mytestweb/PTT_Gossiping_data.csv')
# print(df)

category_counts =  df.groupby(["category","date"]).size().reset_index(name='category count').sort_values(by='category count', ascending=False)
category_counts_top10 = category_counts.head(10)
# print(category_counts_top10)

# 前10的分類排行
category =  df.groupby(["category"]).size().reset_index(name='category count').sort_values(by='category count', ascending=False)
category_top10 = category.head(10)
print(category_top10)

with (open('/Users/USER/Downloads/Python_Django-main/django_test/Django_test/mytestweb/Category_top10.csv', 'w', encoding='utf-8')) as f:
        f.write(category_top10)


plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] # 修改中文字體
plt.rcParams['axes.unicode_minus'] = False # 顯示負號

category = ['[問卦]','[新聞]','[爆掛]','[地震]','[問題]']
count = [1, 2, 3, 4, 5]

plt.figure(figsize=(5,3))

plt.subplot(111)
plt.bar(category, count)
plt.show

#%%
import pandas as pd
import matplotlib.pyplot as plt

    
df = pd.read_csv('/Users/USER/Downloads/Python_Django-main/django_test/Django_test/mytestweb/PTT_Gossiping_data.csv')

df_dropna = df.dropna()
print(df_dropna)
df_isnull = df_dropna['pop'].isnull()
print(df_isnull)


chart_df = df_dropna[["category","pop","date"]]
print(chart_df.info())

chart_df['pop'] = chart_df['pop'].replace('爆', 100)
chart_df['pop'] = chart_df['pop'].replace('XX', -100)
chart_df['pop'] = chart_df['pop'].replace(r'X(\d+)', r'-\1', regex=True)
chart_df['date'] = pd.to_datetime(df['date'], format='%m/%d')
print(chart_df)
int_pop = chart_df['pop'].astype(int)



print(int_pop.info())
print(int_pop)
chart_df.to_csv('/Users/USER/Downloads/Python_Django-main/django_test/Django_test/mytestweb/int_pop.csv', index=False)


df = pd.read_csv('/Users/USER/Downloads/Python_Django-main/django_test/Django_test/mytestweb/int_pop.csv')
print(df.info())
chart = chart_df.plot(xlabel='pop', ylabel='date', title='123', legend=True)
plt.grid()
plt.show()

#%%
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/USER/Downloads/Python_Django-main/django_test/Django_test/mytestweb/PTT_Gossiping_data.csv')
print(data['pop'])

# 創建一個範例DataFrame
# data = {'category': ['[問卦]', '[新聞]', '[問卦]', '[問卦]', '[新聞]'],
#         'pop': ['3', '10', '3', '3', '5'],
#         'date': ['5/06', '5/07', '5/08', '5/09', '5/10']}


df = data.dropna()
df['pop'] = df['pop'].fillna(0)
print(df['pop'])

# 將'pop'欄位轉換為數值型態
df['pop'] = df['pop'].replace('爆', 100)
df['pop'] = df['pop'].replace('XX', -100)
df['pop'] = df['pop'].replace(r'X(\d+)', r'-\1', regex=True)
df['pop'] = df['pop'].astype(int)

# 將日期字符串轉換為日期格式
df['date'] = pd.to_datetime(df['date'] + '/2024', format='%m/%d/%Y')

# 根據日期對'pop'求和
# df = df.groupby('date')['pop'].sum().reset_index()

print(df['pop'])

# 繪製圖表
plt.plot(df['date'], df['pop'])
plt.xlabel('Date')
plt.ylabel('Popularity')
plt.title('Popularity Over Time')
plt.xticks(rotation=45)

plt.show()

#%%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/USER/Downloads/Python_Django-main/django_test/Django_test/mytestweb/PTT_Gossiping_data.csv')
# print(data['pop'])


df = data.dropna()
df['pop'] = df['pop'].fillna(0)
# print(df['pop'])

# 將'pop'欄位轉換為數值型態
df['pop'] = df['pop'].replace('爆', 100)
df['pop'] = df['pop'].replace('XX', -100)
df['pop'] = df['pop'].replace(r'X(\d+)', r'-\1', regex=True)
df['pop'] = df['pop'].astype(int)

# 將日期字符串轉換為日期格式
df['date'] = pd.to_datetime(df['date'] + '/2024', format='%m/%d/%Y')

# 繪製scatter圖表
plt.scatter(df['date'], df['pop'], marker='o')
plt.xlabel('Date')
plt.ylabel('Popularity')
plt.title('Popularity Over Time')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
