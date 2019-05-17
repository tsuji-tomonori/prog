import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

# 変数
x_train = []
y_train = []
x_test = []
y_test = []
model = None

# データ前処理
def preprocessing(plt_flag):

    # グローバル変数宣言
    global x_train,y_train,x_test,y_test

    # データ作成
    x = np.random.rand(100,1)
    x = x * 2 - 1

    y = 4 * x ** 3 - 3 * x ** 2 + 2 * x - 1

    # 標準正規分布(平均:0,分散:1)の乱数を加える
    y += np.random.randn(100,1)

    # 学習データ 30個
    x_train = x[:30]
    y_train = y[:30]

    # テストデータ 70個
    x_test = x[30:]
    y_test = y[30:]
    
    # 作成したデータをグラフに表示
    if plt_flag:
        plt.subplot(2,2,1)
        plt.scatter(x,y,marker='+')
        plt.title('all')

        plt.subplot(2,2,2)
        plt.scatter(x_train,y_train,marker='+')
        plt.title('train')
        
        plt.subplot(2,2,3)
        plt.scatter(x_test,y_test,marker='+')
        plt.title('test')
    
        plt.tight_layout()
        plt.show()
    
    return[x_train,y_train,x_test,y_test]

# 学習
def train(plt_flag):

    # グローバル変数宣言
    global model

    # 9次式として学習
    X_TRAIN = np.c_[x_train**9, x_train**8, x_train**7,
                    x_train**6, x_train**5, x_train**4,
                    x_train**3, x_train**2, x_train]

    # モデルの作成
    model = linear_model.Ridge()

    # 学習
    model.fit(X_TRAIN,y_train)

    print(model.coef_)
    print(model.intercept_)
    print(model.score(X_TRAIN,y_train))

    if plt_flag:
        plt.scatter(x_train,y_train,marker='+')
        plt.scatter(x_train,model.predict(X_TRAIN))
        plt.show()
    return model

# test
def test(plt_flag):

    X_TEST = np.c_[x_test**9, x_test**8, x_test**7,
                   x_test**6, x_test**5, x_test**4,
                   x_test**3, x_test**2, x_test]
    
    print(model.score(X_TEST,y_test))

    if plt_flag:
        plt.scatter(x_test,y_test,marker='+')
        plt.scatter(x_test,model.predict(X_TEST))
        plt.show()


# main
if __name__ == '__main__':
    preprocessing(False)
    train(False)
    test(True)

