# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 09:14:14 2024

@author: USER
"""


import requests
import bs4
import pandas as pd


def search_data():
    base_url = 'https://www.ptt.cc'
    sub_url = '/bbs/Gossiping/index.html'
    my_headers = {'cookie': 'over18=1'}

    data = {"title":[], "pop":[], "author":[], "date":[]}
    while True:
        full_url = base_url + sub_url
        response_url = requests.get(full_url, headers = my_headers)
        soup = bs4.BeautifulSoup(response_url.text, 'html.parser')
        ppt_articles = soup.find_all('div', class_='r-ent')


        for article in ppt_articles:
            title = article.find('div', class_='title').text.strip()
            
            if '[公告]' in title or '[協尋]' in title:
                continue
            pop = article.find('div', class_='nrec').text.strip()
            
            author = article.find('div', class_='author').text.strip()
            
            date_str = article.find('div', class_='date').text.strip()
            month, day = date_str.split('/')
            date = int(str(int(month)) + str(int(day)))
            
            data["title"].append(title)
            data["pop"].append(pop)
            data["author"].append(author)
            data["date"].append(date_str)
            pandas_dataframe = pd.DataFrame(data)
            #print(pandas_dataframe)
        
        pandas_dataframe.to_csv(r'C:/Users/USER/Documents/file.csv', 
                                encoding='utf-8', 
                                index=False)

            
        find_article = soup.find_all('div', class_='r-ent')
        second_article_date = find_article[1]
        date_str = second_article_date.find('div', class_='date').text.strip()
        article_month, article_day = date_str.split('/')
        count_date = int(str(int(article_month)) + str(int(article_day)))
        #print(count_date)
        
        if count_date < 429:
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

df = pd.read_csv('C:/Users/USER/Documents/file.csv')
word_1 = df['title'][0]
word_2 = df['title'][0]
word_3 = word_1 + word_2
#print(word_3)


words = [i for i in word_3]
dict_words = {i:word_3.count(i) for i in word_3}
print(dict_words)

#%%
df = pd.read_csv('C:/Users/USER/Documents/file.csv')
words = df['title']
#print(words)
x = []
for i in words:
    for z in i:
        x.append(z)
    
#print(x)

x = [i for i in x]
dict_words = {i:x.count(i) for i in x}
print(dict_words)

aaa = pd.DataFrame(dict_words.items(), columns=['Word', 'Pop', 'Authour', 'Date'])
print(aaaa)
sort = aaa.sort_values(by='Pop', ascending=False)
print(sort.head(50))

