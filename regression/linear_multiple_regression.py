import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

# 変数
x1 = []
x2 = []
x1_x2 = []
y = []
model = None

# データ前処理
def preprocessing(plt_flag):

    # グローバル変数宣言
    global x1,x2,x1_x2,y

    # データ作成
    x1 = np.random.rand(100,1)
    x1 = x1 * 4 - 2

    x2 = np.random.rand(100,1)
    x2 = x2 * 4 - 2
    
    # [[x1_1,x2_1],[x1_2,x2_2],...
    x1_x2 = np.c_[x1,x2]

    y = 3 * x1 - 2 * x2 + 1

    # 標準正規分布(平均:0,標準偏差:1)の乱数を加える
    y += np.random.randn(100,1)

    # 作成したデータをグラフに表示
    if plt_flag:
        plt.subplot(1,2,1)
        plt.scatter(x1,y,marker='+')
        plt.xlabel('x1')
        plt.ylabel('y')

        plt.subplot(1,2,2)
        plt.scatter(x2,y,marker='+')
        plt.xlabel('x2')
        plt.ylabel('y')

        plt.tight_layout()
        plt.show()
    
    return[x1_x2,y]

# 学習
def train(plt_flag):

    # グローバル変数宣言
    global model

    # モデルの作成
    model = linear_model.LinearRegression()

    # 学習
    model.fit(x1_x2,y)

    # 求めた回帰式で予測
    y_ = model.predict(x1_x2)
    # 学習データをグラフに表示
    if plt_flag:
        plt.subplot(1,2,1)
        plt.scatter(x1,y,marker='+')
        plt.scatter(x1,y_,marker='o')
        plt.xlabel('x1')
        plt.ylabel('y')

        plt.subplot(1,2,2)
        plt.scatter(x2,y,marker='+')
        plt.scatter(x2,y_,marker='o')
        plt.xlabel('x2')
        plt.ylabel('y')

        plt.tight_layout()
        plt.show()

    print('y = {:.5f}x1 + {:.5f}x2 + {:.5f}'.format(model.coef_[0][0],model.coef_[0][1],model.intercept_[0]))

    return model

# 評価
def evaluation():

    # R^2を計算
    r2 = model.score(x1_x2,y)

    print('R^2:{:.5f}'.format(r2))
    
    return r2

# main
if __name__ == '__main__':
    preprocessing(False)
    train(True)
    evaluation()
