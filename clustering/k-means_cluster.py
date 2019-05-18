import matplotlib.pyplot as plt
from sklearn import cluster
from sklearn import datasets

# 変数
data = []
iris = None
model = None

# データ前処理
def preprocessing():

    # global 変数宣言
    global iris,data
    # irisデータセットの読み込み
    iris = datasets.load_iris()
    # あやめの測定値を取得
    data = iris['data']
    
    return [iris,data]

# 学習
def train():

    # global 変数宣言
    global model

    # モデルの作成
    model = cluster.KMeans(n_clusters=3)
    # クラスタ化
    model.fit(data)

    return model

# 結果の表示
def print_result():

    # 学習結果のラベル取得
    labels = model.labels_

    # クラスタリング結果の表示
    print('クラスタリング結果\n', labels)

    # グラフの描画
    mark = ['o','^','*'] # グラフのマーク
    X_INDEX = 2 # x軸 (花弁の長さ)
    Y_INDEX = 3 # y軸 (花弁の幅)

    for i in range(3):
        ldata = data[labels == i]
        plt.scatter(ldata[:,X_INDEX],ldata[:,Y_INDEX],
                    c='black', alpha=0.3, s=100, marker=mark[i])

    plt.xlabel(iris['feature_names'][X_INDEX])
    plt.ylabel(iris['feature_names'][Y_INDEX])

    plt.show()

# main
if __name__ == '__main__':
    preprocessing()
    train()
    print_result()
