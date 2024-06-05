import requests
import bs4
import pandas as pd
import re
import concurrent.futures
import time


base_url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
my_headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
              'cookie': 'over18=1'}
response_url = requests.get(base_url, headers = my_headers)
soup = bs4.BeautifulSoup(response_url.text, 'html.parser')


# 尋找tag 'a'，並找到上一頁的網址
prev_link = soup.find('a', string='‹ 上頁')
prev_link_url = prev_link['href']
# print(prev_link_url)
match = re.search(r'index(\d+)', prev_link_url)
current_index_num = (int(match.group(1)))+1
# print(current_index_num)

range10_index_num = []
for i in range(current_index_num, current_index_num-10, -1):
    range10_index_num.append(i)
# print(range10_index_num)

urls = ["https://www.ptt.cc/bbs/Gossiping/index{}.html".format(i) for i in range10_index_num]
# print(urls)
# urls = [
#     "https://www.example.com/1",
#     "https://www.example.com/2",
#     # ... 100 more URLs
# ]

def fetch_url(url):
    # Simulate fetching data from a URL
    time.sleep(1)
    print(f"Fetched: {url}")
    return url

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    future_to_url = {executor.submit(fetch_url, url): url for url in urls}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
            # Process data
        except Exception as e:
            print(f"Error fetching {url}: {e}")

#%%
import requests
from bs4 import BeautifulSoup
import concurrent.futures
import time  # for simulated delay (optional)

# Base URL (replace with desired PTT Gossip board URL)
base_url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

# Headers to mimic a web browser and comply with PTT's robots.txt
my_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    'cookie': 'over18=1'  # Required for PTT access
}


def fetch_ptt_titles(url):
    """Fetches PTT titles from a given URL.

    Args:
        url (str): The URL of the PTT page to scrape.

    Returns:
        list: A list of PTT article titles extracted from the page,
              or an empty list if errors occur.
    """

    try:
        response = requests.get(url, headers=my_headers)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract titles using appropriate selectors based on PTT's HTML structure
        ppt_articles = soup.find_all('div', class_='r-ent')  # Customize selector as needed
        for article in ppt_articles:
            htmal_tag = article.find('div', class_='title').text.strip('')
        
        return htmal_tag
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []


def main():
    """Main function to orchestrate parallel title fetching."""

    response_url = requests.get(base_url, headers=my_headers)
    soup = BeautifulSoup(response_url.text, 'html.parser')

    # Find the previous page link (logic might need adjustment based on PTT's HTML structure)
    prev_link = soup.find('a', string='‹ 上頁')
    if prev_link:
        prev_link_url = prev_link['href']
        match = re.search(r'index(\d+)', prev_link_url)
        current_index_num = int(match.group(1)) + 1

    # Generate a range of URLs for the desired number of pages
    num_pages_to_fetch = 10  # Adjust as needed
    range10_index_num = range(current_index_num, current_index_num - num_pages_to_fetch, -1)

    urls = ["https://www.ptt.cc/bbs/Gossiping/index{}.html".format(i) for i in range10_index_num]
    print(urls)
    # Use a thread pool executor for parallel fetching
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        future_to_url = {executor.submit(fetch_ptt_titles, url): url for url in urls}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                titles = future.result()
                # Process the fetched titles (e.g., print, store in a list)
                for title in titles:
                    print(title)
            except Exception as e:
                print(f"Error fetching {url}: {e}")


if __name__ == '__main__':
    main()
# %%
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import concurrent.futures
import time  # for simulated delay (optional)

# Base URL (replace with desired PTT Gossip board URL)
base_url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

# Headers to mimic a web browser and comply with PTT's robots.txt
my_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    'cookie': 'over18=1'  # Required for PTT access
}


def fetch_ptt_titles(url):
    # time.sleep(1)
    """Fetches PTT titles from a given URL.

    Args:
        url (str): The URL of the PTT page to scrape.

    Returns:
        list: A list of PTT article titles extracted from the page,
              or an empty list if errors occur.
    """

    try:
        response = requests.get(url, headers=my_headers)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract titles using appropriate selectors based on PTT's HTML structure

        data = []
        articles = soup.find_all('div', class_='r-ent')
        for article in articles:
            htmal_tag = article.find('div', class_='title').text.strip('')
    
            # 取得文章標題
            title = htmal_tag.replace('[問卦]', '').replace('[新聞]', '').replace('[爆卦]', '').strip()
    
            # 取得文章類別
            match = re.search(r'\[.*?\]', htmal_tag)
            if match:
                category = match.group(0)
            else:
                category = 'None'
            
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
            
            # 取得當前index number
            prev_link = soup.find('a', string='‹ 上頁')
            prev_link_url = prev_link['href']
            match = re.search(r'index(\d+)', prev_link_url)
            current_index_num = int(match.group(1)) + 1

            # 資料回填到data字典,並轉pandas df格式
            data.append({'category':category, 
                         'title':title, 
                         'pop':pop, 
                         'author':author, 
                         'date':date, 
                         'current_index_num':current_index_num})
            
        # print(data)
            
        # print(pandas_dataframe)
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")


def main():
    try:
        """Main function to orchestrate parallel title fetching and writing to a text file."""

        response_url = requests.get(base_url, headers=my_headers)
        soup = BeautifulSoup(response_url.text, 'html.parser')

        # Find the previous page link (logic might need adjustment based on PTT's HTML structure)
        prev_link = soup.find('a', string='‹ 上頁')
        if prev_link:
            prev_link_url = prev_link['href']
            match = re.search(r'index(\d+)', prev_link_url)
            current_index_num = int(match.group(1)) + 1
        else:
            # Handle cases where there's no previous page link (e.g., first page)
            current_index_num = 1

        # Generate a range of URLs for the desired number of pages
        num_pages_to_fetch = 100000  # Adjust as needed
        range10_index_num = range(current_index_num, current_index_num - num_pages_to_fetch, -1)

        urls = ["https://www.ptt.cc/bbs/Gossiping/index{}.html".format(i) for i in range10_index_num]


        # Use a thread pool executor for parallel fetching
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            future_to_url = {executor.submit(fetch_ptt_titles, url): url for url in urls}
            # print(future_to_url)

            merged_data = []  # Create an empty list to store all data

            for future in concurrent.futures.as_completed(future_to_url):
                url = future_to_url[future]
                data = future.result()
                # print(data)

                merged_data.extend(data)  # Add data to the merged_data list

                # Combine all fetched data into a single DataFrame
                df = pd.DataFrame(merged_data)

                # Write DataFrame to CSV file (replace 'ptt_data.csv' with your desired filename)
                df.to_csv('ptt_data_1.csv',index=False)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")


if __name__ == '__main__':
    main()