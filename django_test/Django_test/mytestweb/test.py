import requests
import bs4
import pandas as pd
import re
# from fake_useragent import UserAgent
import time


# 預設爬蟲參數
base_url = 'https://www.ptt.cc'
sub_url = '/bbs/Gossiping/index.html'
# ua = UserAgent()
# user_agent = ua.random
my_headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0','cookie': 'over18=1'}

# 迴圈重複抓取PPT文章
data = {"category":[], "title":[], "pop":[], "author":[], "date":[]}
try:
    while True:
        full_url = base_url + sub_url
        response_url = requests.get(full_url, headers = my_headers)
        soup = bs4.BeautifulSoup(response_url.text, 'html.parser')
        ppt_articles = soup.find_all('div', class_='r-ent')
        # time.sleep(2)

        # 迴圈文字處理各項欄位
        for article in ppt_articles:
            htmal_tag = article.find('div', class_='title').text.strip('')
    
            # 取得文章標題
            title = htmal_tag.replace('[問卦]', '').replace('[新聞]', '').replace('[爆卦]', '').strip()
    
            # 取得文章類別
            match = re.search(r'\[.*?\]', htmal_tag)
            if match:
                category = match.group(0)
            
            # 過濾公告或協尋文章
            if '[公告]' in htmal_tag or '[協尋]' in htmal_tag:
                continue
    
            # 取得回文數
            pop = article.find('div', class_='nrec').text.strip()
            
            # 取得作者ID
            author = article.find('div', class_='author').text.strip()
            
            # 日期字串拆分處理
            date_str = article.find('div', class_='date').text.strip()
            month, day  = date_str.split('/')
            date = int(str(int(month)) + str(int(day[0])) + str(int(day[1])))
            # print(date)
            
            # 資料回填到data字典,並轉pandas df格式
            data["category"].append(category)
            data["title"].append(title)
            data["pop"].append(pop)
            data["author"].append(author)
            data["date"].append(date_str)
            pandas_dataframe = pd.DataFrame(data)
            # print(pandas_dataframe)
            print("Date: ",date, "Index: ", len(pandas_dataframe))
                
    
            # 尋找tag 'a'，並找到上一頁的網址
            prev_link = soup.find('a', string='‹ 上頁')
            if prev_link is None:
                break
            else:
                sub_url = prev_link['href']
    
            # 判斷日期是101時則結束迴圈
            if date == 506:
                print(f'Break === date is {date}')
                break



        pandas_dataframe.to_csv(r'C:/Users/USER/Desktop/PTT_Gossiping_data.csv', 
                                        encoding='utf-8', 
                                        index=False)
        print("========Write======")
        print(sub_url)
        
    
# 異常發生回傳full_url並在嘗試執行迴圈
except Exception as e:
    print("while True error: ",e)
    print(f"Current sub_url: {sub_url}")
    full_url = base_url + sub_url
    
    
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
