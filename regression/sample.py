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

    # 作成したデータをグラフに表示
    if plt_flag:
        plt.scatter(x,y,marker='+')
        plt.show()
    
    return[x,y]

# 学習
def train():

    # グローバル変数宣言
    global model

    # モデルの作成
    model = linear_model.LinearRegression()

    # 学習
    model.fit(x,y)

    print(model.coef_)
    print(model.intercept_)

    return model


if __name__ == '__main__':
    preprocessing(True)
    train()

