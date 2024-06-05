import matplotlib.pyplot as plt


#### 一月PTT文章類型比重 ####
def ptt_jan_category_type(category_news_month_1_data, category_gossip_month_1_data, category_ask_month_1_data):

    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

    category_type = ['新聞', '爆卦', '問卦']
    category_count = [category_news_month_1_data, category_gossip_month_1_data, category_ask_month_1_data]

    fig = plt.figure(figsize=(8,5))

    plt.xlim(-1,3)
    plt.plot(category_type, category_count, marker = 'o', linestyle = '--')

    plt.xlabel('文章類別', color = 'red')
    plt.ylabel('文章數量（篇）', color = 'red')
    plt.tick_params(axis='x', width=5, rotation=45)
    plt.title('PTT八卦版 一月文章類別分布', color = 'red')
    plt.savefig('ptt_jan_category_type.png')
    plt.show()