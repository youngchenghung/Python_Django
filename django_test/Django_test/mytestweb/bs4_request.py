# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 09:14:14 2024

@author: USER
"""

#%%
import requests
import bs4
import pandas as pd
import re
from fake_useragent import UserAgent
import time


def search_data():
    base_url = 'https://www.ptt.cc'
    sub_url = '/bbs/Gossiping/index.html'
    ua = UserAgent()
    user_agent = ua.random
    my_headers = {'user-agent':user_agent,'cookie': 'over18=1'}

    data = {"category":[], "title":[], "pop":[], "author":[], "date":[]}
    while True:
        full_url = base_url + sub_url
        response_url = requests.get(full_url, headers = my_headers)
        soup = bs4.BeautifulSoup(response_url.text, 'html.parser')
        ppt_articles = soup.find_all('div', class_='r-ent')
        # time.sleep(2)


        for article in ppt_articles:
            full_title = article.find('div', class_='title').text.strip('')

            title = full_title.replace('[問卦]', '').replace('[新聞]', '').replace('[爆卦]', '').strip()

            match = re.search(r'\[.*?\]', full_title)
            if match:
                category = match.group(0)
            
            if '[公告]' in full_title or '[協尋]' in full_title:
                continue

            pop = article.find('div', class_='nrec').text.strip()
            
            author = article.find('div', class_='author').text.strip()
            
            date_str = article.find('div', class_='date').text.strip()
            month, day  = date_str.split('/')
            date = int(str(int(month)) + str(int(day[0])) + str(int(day[1])))
            # print(date)
            
            
            data["category"].append(category)
            data["title"].append(title)
            data["pop"].append(pop)
            data["author"].append(author)
            data["date"].append(date_str)
            pandas_dataframe = pd.DataFrame(data)
            # print(pandas_dataframe)
            indexnum = (list(pandas_dataframe.index))
            

         
        print(indexnum[-1])
        x=100
        if indexnum[-1] >= int(x):
            print(x)
            pandas_dataframe.to_csv(r"C:/Users/USER/Desktop/PTT_Gossiping_data.csv", 
                                encoding='utf-8', 
                                index=False)
            print("done")
            x =+ 100
            time.sleep(5)
            
            
            
            
        # pandas_dataframe.to_csv(r'C:\Users\USER\PTT_Gossiping_data.csv', 
        #                         encoding='utf-8', 
        #                         index=False)

            
            find_article = soup.find_all('div', class_='r-ent')
            second_article_date = find_article[1]
            date_str = second_article_date.find('div', class_='date').text.strip()
            article_month, article_day = date_str.split('/')
            count_date = int(str(int(article_month)) + str(int(article_day[0])) + str(int(article_day[1])))
        #print(count_date)
        

            if count_date < 505:
                print(count_date)
                print("========DONE======")
                return


        # Find the link to the previous page
        prev_link = soup.find('a', string='‹ 上頁')
        if prev_link is None:
            return
        sub_url = prev_link['href']


if __name__ == '__main__':
    search_data()
    
#%%
import pandas as pd

df = pd.read_csv('/Users/kohakudaitoku/Documents/聯成/Python_Django-main/django_test/Django_test/PTT_Gossiping_data.csv')
select = df[['title','pop']]
print(select.sort_values(by='pop', ascending=False))
#%%
import pandas as pd
import os

# 讀取raw data
current_path = os.getcwd()
df = pd.read_csv(os.path.join(current_path, 'PTT_Gossiping_data.csv'))


x = []
# for index, row in df.iterrows():
#     title = row['title']
#     pop = row['pop']
#     author = row['author']
#     date = row['date']

#     print(f'title: {title}, pop: {pop}, author: {author}, date: {date}')

#     for z in i:
#         x.append(z)
    
# print(x)

# 迴圈取出title欄位中的資料，並存入 x list中
for i in df['title']:
    x.append(i)
print(x)

# 將 x list中的資料寫入檔案
with (open('/Users/kohakudaitoku/Documents/聯成/Python_Django/django_test/Django_test/mytestweb/PTT_title_list.txt', 'w', encoding='utf-8')) as f:
    for i in x:
        f.write(i + '\n')

    # for z in i:
    #     x.append(z)
# print(x)


# x = [i for i in x]
# dict_words = {i:x.count(i) for i in x}
# print(dict_words)

# aaa = pd.DataFrame(dict_words.items(), columns=['title', 'Pop'])
# print(aaa)
# sort = aaa.sort_values(by='Pop', ascending=False)
# print(sort.head(50))


# %%

import jieba
import jieba.analyse
from collections import Counter
import pandas as pd
import os

# 讀取raw data
current_path = os.getcwd()
df = pd.read_csv(os.path.join(current_path, 'PTT_Gossiping_data.csv'))

# 讀取 title 資料檔案 title_list.txt
with (open('/Users/leo/Python_Django-2/django_test/Django_test/mytestweb/PTT_title_list.txt', 'r', encoding='utf-8')) as f:
    data = f.read()
    # print(data)

# 官方預設詞庫
jieba.set_dictionary('dict.txt.big')

# 讀取停用字檔案 stopwords.txt
stop_words_file = '/Users/leo/Python_Django-2/django_test/Django_test/mytestweb/stop_words.txt'
stop_words_list = []
for line in open(stop_words_file, 'r', encoding='utf-8'):
    stop_words_list.append(line.strip('\n'))
# print(stop_words_list)

# 停用字轉串列格式,並將title資料做停用字過濾
filter_words = []
# stop_words_list = stop_words_file
for word_list in data:
    if all(filter_words not in word_list for filter_words in stop_words_list):
        filter_words.append(word_list.strip('\n'))
# print(filter_words)

# 將list 轉字串型態
join_filter_words = ''.join(filter_words)
# print(join_filter_words)
# jieba sjieba.analyse.extract_tags() 取出前20個關鍵字
# keywords = jieba.analyse.extract_tags(join_stop_words, topK=20)
# print(keywords)

# jieba處理字轉詞
jieba_words = jieba.lcut(join_filter_words)
# print(jieba_words)
keywords = []
for i in jieba_words:
    # 過濾字當只有一個字
    if len(i) == 1:
        continue
    else:
        keywords.append(i)
# print(keywords)

# 使用 Counter 計算每個詞的出現次數
keywords_counts = Counter(keywords)
# print(keywords_counts)

# 將結果存入 DataFrame, 並依照 count 排序
df = pd.DataFrame(list(keywords_counts.items()), columns=['Word', 'Counts'])
x = df.sort_values(by='Counts', ascending=False)
print(x.head(50))

df.to_csv('/Users/leo/Python_Django-2/django_test/Django_test/mytestweb//PTT_words_count.csv', 
          encoding='utf-8', 
          index=False)

with (open('/Users/leo/Python_Django-2/django_test/Django_test/mytestweb/PTT_words_count.csv', 'r', encoding='utf-8')) as f:
    PTT_words_count = pd.read_csv(f)
    print(PTT_words_count)


# 排序欄位Counts從大到小
sort_counts = PTT_words_count.sort_values(by='Counts', ascending=False)
print(sort_counts)

#%%
import jieba
import jieba.analyse
from collections import Counter
import pandas as pd


df = pd.read_csv('/Users/leo/Python_Django-2/django_test/Django_test/mytestweb/PTT_Gossiping_data.csv')
print(df)

category_counts =  df.groupby(["category","date"]).size().reset_index(name='category count').sort_values(by='category count', ascending=False)
category_counts_top10 = category_counts.head(10)
print(category_counts_top10)

category =  df.groupby(["category"]).size().reset_index(name='category count').sort_values(by='category count', ascending=False)
category_top10 = category.head(10)
print(category_top10)

date =  df.groupby(["date"]).size().reset_index(name='date count').sort_values(by='date count', ascending=False)
date_top10 = date.head(10)
print(date_top10)

author_counts =  df.groupby("author").size().reset_index(name='author count').sort_values(by='author count', ascending=False)
author_counts_top10 = author_counts.head(10)
print(author_counts_top10)

author_counts =  df["author"] == "words2012"
print(df[author_counts])

author2_counts =  df["author"] == "xzcb2008"
print(df[author2_counts])

author3_counts =  df["author"] == "felixden"
print(df[author3_counts])

author4_counts =  df["author"] == "ianlin1216"
print(df[author4_counts])

# %%
