#### 日份動態圖 ####

import matplotlib.pyplot as plt
import matplotlib.animation as animation


def ptt_jan_days_category_type(total_1_category_count):
    
    category_type = ['新聞', '爆卦', '問卦']

    # 創建畫布(寬8, 高5)
    fig, ax = plt.subplots(figsize=(8,5))


    def update(num):
        
        ax.clear()
        
        ax.bar(category_type, total_1_category_count[num % len(total_1_category_count)])
        ax.set_title('PTT八卦版 1月文章類別分布', color = 'red')

        ax.set_xlabel('文章類別', color = 'red')
        ax.set_ylabel('文章數量（篇）', color = 'red')
        ax.set_title(f'PTT八卦版 1月 / {num+1}日 文章類別分布', color = 'red')

        # 設定 x 軸的文字刻度間距為 5 個單位
        ax.tick_params(axis='x', width=5, rotation=0)
        # 設定 x 軸的刻度間距為 1
        ax.set_xlim(-1,3)
        # 設定 y 軸的範圍
        ax.set_ylim(0, 35000)
        # 設定 y 軸的刻度間距為 5000
        ax.set_yticks(np.arange(0, 35000, 5000))

    ani = animation.FuncAnimation(fig, update, frames=range(31), repeat=True)
    plt.rcParams["font.family"] = 'Arial Unicode MS'
    plt.show()

    ani.save('movechart_month_1_category.gif', writer='imagemagick', fps=1/0.2)