
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

    # 創建畫布(寬8, 高5)
fig, ax = plt.subplots(figsize=(8,5))


def aaaa(num,category_news_month_1_data,category_gossip_month_1_data,category_ask_month_1_data, category_news_month_2_data, category_gossip_month_2_data, category_ask_month_2_data, category_news_month_3_data, category_gossip_month_3_data, category_ask_month_3_data, category_news_month_4_data, category_gossip_month_4_data, category_ask_month_4_data, category_news_month_5_data, category_gossip_month_5_data, category_ask_month_5_data):
    
    category_type = ['新聞', '爆卦', '問卦']
    category_count_1 = [category_news_month_1_data, category_gossip_month_1_data, category_ask_month_1_data]
    category_count_2 = [category_news_month_2_data, category_gossip_month_2_data, category_ask_month_2_data]
    category_count_3 = [category_news_month_3_data, category_gossip_month_3_data, category_ask_month_3_data]
    category_count_4 = [category_news_month_4_data, category_gossip_month_4_data, category_ask_month_4_data]
    category_count_5 = [category_news_month_5_data, category_gossip_month_5_data, category_ask_month_5_data]
    category_count_list = [category_count_1, category_count_2, category_count_3, category_count_4, category_count_5]
    # print(category_count_list)


    ax.clear()
    ax.bar(category_type, category_count_list[num % len(category_count_list)])
    ax.set_title('PTT八卦版 2024-1月到5月文章類別分布', color = 'red')

    ax.set_xlabel('文章類別', color = 'red')
    ax.set_ylabel('文章數量（篇）', color = 'red')
    ax.set_title(f'PTT八卦版 2024-{num+1}月文章類別分布', color = 'red')

    # 設定 x 軸的文字刻度間距為 5 個單位
    ax.tick_params(axis='x', width=5, rotation=0)
    # 設定 x 軸的刻度間距為 1
    ax.set_xlim(-1,3)
    # 設定 y 軸的範圍
    ax.set_ylim(0, 40000)
    # 設定 y 軸的刻度間距為 5000
    ax.set_yticks(np.arange(0, 40000, 5000))
    plt.rcParams["font.family"] = 'Arial Unicode MS'
    plt.show()

ani = animation.FuncAnimation(fig, aaaa, frames=range(5), repeat=True)
ani.save('movechart.gif', writer='imagemagick', fps=1/1)