import requests
import bs4


def search_data():
    base_url = 'https://www.ptt.cc'
    sub_url = '/bbs/Gossiping/index.html'
    my_headers = {'cookie': 'over18=1'}

    while True:
        full_url = base_url + sub_url
        response_url = requests.get(full_url, headers = my_headers)
        soup = bs4.BeautifulSoup(response_url.text, 'html.parser')
        ppt_articles = soup.find_all('div', class_='r-ent')

        for article in ppt_articles:
            title = article.find('div', class_='title').text.strip()
            
            if '[公告]' in title or '[協尋]' in title:
                continue
            
            date_str = article.find('div', class_='date').text.strip()
            month, day = date_str.split('/')
            date = int(str(int(month)) + str(int(day)))
            
            print(f"Title: {title}, Date: {date}")

        find_article = soup.find_all('div', class_='r-ent')
        second_article_date = find_article[1]
        date_str = second_article_date.find('div', class_='date').text.strip()
        article_month, article_day = date_str.split('/')
        count_date = int(str(int(article_month)) + str(int(article_day)))
        print(count_date)
        
        if count_date < 429:
            return

        # Find the link to the previous page
        prev_link = soup.find('a', string='‹ 上頁')
        if prev_link is None:
            return
        sub_url = prev_link['href']

if __name__ == '__main__':
    search_data()