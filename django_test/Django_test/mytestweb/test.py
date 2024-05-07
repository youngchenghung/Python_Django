import requests
import bs4
import pandas as pd
import re
from fake_useragent import UserAgent
import time

try:
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
            htmal_tag = article.find('div', class_='title').text.strip('')

            title = htmal_tag.replace('[問卦]', '').replace('[新聞]', '').replace('[爆卦]', '').strip()

            match = re.search(r'\[.*?\]', htmal_tag)
            if match:
                category = match.group(0)
            
            if '[公告]' in htmal_tag or '[協尋]' in htmal_tag:
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
            # print(len(pandas_dataframe))


        # 尋找tag 'a'，並找到上一頁的網址
        prev_link = soup.find('a', string='‹ 上頁')
        if prev_link is None:
            break
        else:
            sub_url = prev_link['href']

            
        if date == 101:
            print('Break === date is 505')
            break     

except Exception as e:
    print(e)

finally:
    pandas_dataframe.to_csv(r'/Users/leo/Python_Django/Python_Django/django_test/Django_test/mytestweb/PTT_Gossiping_data.csv', 
                                    encoding='utf-8', 
                                    index=False)
    print("========Write======")
    print(sub_url)
    
        # pandas_dataframe.to_csv(r'C:\Users\USER\PTT_Gossiping_data.csv', 
        #                         encoding='utf-8', 
        #                         index=False)

            
        #     find_article = soup.find_all('div', class_='r-ent')
        #     second_article_date = find_article[1]
        #     date_str = second_article_date.find('div', class_='date').text.strip()
        #     article_month, article_day = date_str.split('/')
        #     count_date = int(str(int(article_month)) + str(int(article_day[0])) + str(int(article_day[1])))
        # #print(count_date)
        

        #     if count_date < 505:
        #         print(count_date)
        #         print("========DONE======")
        #         return


