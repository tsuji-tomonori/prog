import math

import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn import svm
from sklearn import ensemble
from sklearn import neighbors

# 変数
x = []
y = []

# データ前処理
def preprocessing(plt_flag):

    # グローバル変数宣言
    global x,y

    # データ作成
    x = np.random.rand(1000,1)
    x = x * 20 - 10

    y = np.array([math.sin(v) for v in x])

    # 標準正規分布(平均:0,標準偏差:1)の乱数を加える
    y += np.random.randn(1000)

    # 作成したデータをグラフに表示
    if plt_flag:
        plt.scatter(x,y,marker='+')
        plt.show()
    
    return[x,y]

# 学習
def train_linear(plt_flag):

    # モデルの作成
    model = linear_model.LinearRegression()

    # 学習
    model.fit(x,y)

    print("-最小二乗法-\n R^2:",model.score(x,y))

    # 作成したデータをグラフに表示
    if plt_flag:
        plt.scatter(x,y,marker='+')
        plt.scatter(x,model.predict(x),marker='o')
        plt.show()
    return model

# 学習
def train_svm(plt_flag):

    # モデルの作成
    model = svm.SVR()

    # 学習
    model.fit(x,y)

    print("-SVM-\n R^2:",model.score(x,y))

    # 作成したデータをグラフに表示
    if plt_flag:
        plt.scatter(x,y,marker='+')
        plt.scatter(x,model.predict(x),marker='o')
        plt.show()
    return model

# 学習
def train_random_forest(plt_flag):

    # モデルの作成
    model = ensemble.RandomForestRegressor()

    # 学習
    model.fit(x,y)

    print("-Random Forest-\n R^2:",model.score(x,y))

    # 作成したデータをグラフに表示
    if plt_flag:
        plt.scatter(x,y,marker='+')
        plt.scatter(x,model.predict(x),marker='o')
        plt.show()
    return model

# 学習
def train_k_neighbors(plt_flag):

    # モデルの作成
    model = neighbors.KNeighborsRegressor()

    # 学習
    model.fit(x,y)

    print("-K 近傍法-\n R^2:",model.score(x,y))

    # 作成したデータをグラフに表示
    if plt_flag:
        plt.scatter(x,y,marker='+')
        plt.scatter(x,model.predict(x),marker='o')
        plt.show()
    return model

# main
if __name__ == '__main__':
    preprocessing(False)
    train_linear(True)
    train_svm(True)
    train_random_forest(True)
    train_k_neighbors(True)
