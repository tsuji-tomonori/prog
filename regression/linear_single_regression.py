import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

# 変数
x = []
y = []
model = None

# データ前処理
def preprocessing(plt_flag):

    # グローバル変数宣言
    global x,y

    # データ作成
    x = np.random.rand(100,1)
    x = x * 4 - 2

    y = 3 * x - 2

    # 標準正規分布(平均:0,標準偏差:1)の乱数を代入
    y += np.random.randn(100,1)

    # 作成したデータをグラフに表示
    if plt_flag:
        plt.scatter(x,y,marker='+')
        plt.show()
    
    return[x,y]

# 学習
def train(plt_flag):

    # グローバル変数宣言
    global model

    # モデルの作成
    model = linear_model.LinearRegression()

    # 学習
    model.fit(x,y)

    # 学習データをグラフに表示
    if plt_flag:
        plt.scatter(x,y,marker='+')
        plt.scatter(x,model.predict(x),marker='o')
        plt.show()
    
    print('y = {:.5f}x + {:.5f}'.format(model.coef_[0][0],model.intercept_[0]))

    return model

# 評価
def evaluation():

    # R^2を計算
    r2 = model.score(x,y)

    print('R^2:{:.5f}'.format(r2))
    
    return r2

# main
if __name__ == '__main__':
    preprocessing(False)
    train(True)
    evaluation()
