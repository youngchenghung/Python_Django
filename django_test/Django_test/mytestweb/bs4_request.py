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


def search_data():
    base_url = 'https://www.ptt.cc'
    sub_url = '/bbs/Gossiping/index.html'
    my_headers = {'cookie': 'over18=1'}

    data = {"category":[], "title":[], "pop":[], "author":[], "date":[]}
    while True:
        full_url = base_url + sub_url
        response_url = requests.get(full_url, headers = my_headers)
        soup = bs4.BeautifulSoup(response_url.text, 'html.parser')
        ppt_articles = soup.find_all('div', class_='r-ent')


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
            print(pandas_dataframe)
        
        pandas_dataframe.to_csv(r'/Users/leo/Python_Django/django_test/Django_test/PTT_Gossiping_data.csv', 
                                encoding='utf-8', 
                                index=False)

            
        find_article = soup.find_all('div', class_='r-ent')
        second_article_date = find_article[1]
        date_str = second_article_date.find('div', class_='date').text.strip()
        article_month, article_day = date_str.split('/')
        count_date = int(str(int(article_month)) + str(int(article_day[0])) + str(int(article_day[1])))
        #print(count_date)
        
        if count_date < 501:
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

df = pd.read_csv('/Users/leo/Python_Django/django_test/Django_test/PTT_Gossiping_data.csv')
select = df[['title','pop']]
print(select.sort_values(by='pop', ascending=False))
#%%

# 讀取爬蟲資料
df = pd.read_csv('/Users/leo/Python_Django/django_test/Django_test/PTT_Gossiping_data.csv')
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
# print(x)

# 將 x list中的資料寫入檔案
with (open('/Users/leo/Python_Django/django_test/Django_test/PTT_title_list.txt', 'w', encoding='utf-8')) as f:
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

# 讀取 title 資料檔案 title_list.txt
with (open('/Users/leo/Python_Django/django_test/Django_test/PTT_title_list.txt', 'r', encoding='utf-8')) as f:
    data = f.read()
    print(data)

# 讀取停用字檔案 stopwords.txt
stop_words_file = '/Users/leo/Python_Django/django_test/Django_test/stopwords.txt'

# 停用字轉串列
stop_words_list = []
with (open(stop_words_file, 'r', encoding='utf-8')) as f:
    for line in f:
        stop_words_list.append(line.replace('\n',''))
# print(stop_words_list)

# 將 title_list.txt 中有停用字去除
filter_words = []
for k in data:
    if k not in stop_words_list:
        filter_words.append(k)
print(filter_words)

words = jieba.cut(data)
words_list = list(words)
print(words_list)

kywords = jieba.analyse.extract_tags(data, topK=20)
print(kywords)

words_count = Counter(words_list)
print(words_count)

df = pd.DataFrame(list(words_count.items()), columns=['word', 'count'])

df.to_csv('/Users/leo/Python_Django/django_test/Django_test/PTT_words_count.csv', 
          encoding='utf-8', 
          index=False)


# %%
