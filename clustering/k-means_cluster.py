import matplotlib.pyplot as plt
from sklearn import cluster
from sklearn import datasets
from sklearn import metrics

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

    # データ属性の表示
    print(iris['target_names'])

    # 混合行列の表示
    print('混合行列\n',metrics.confusion_matrix(iris['target'], model.labels_))
    
    # グラフの描画
    count = 1 # カウント変数
    for x_index in range(labels.max() + 1):
        for y_index in range(labels.max() + 1):
            if x_index != y_index:
                plt.subplot(3,2,count)
                scatter_by_features(x_index,y_index,labels)
                count += 1
    
    plt.tight_layout()
    plt.show()

    return labels

# 指定されたインデックスの feature 値で散布図を作成する関数
def scatter_by_features(X_INDEX,Y_INDEX,labels):
    
    # グラフの描画
    mark = ['o','^','*'] # グラフのマーク

    for i in range(labels.max() + 1):
        ldata = data[labels == i]
        plt.scatter(ldata[:,X_INDEX],ldata[:,Y_INDEX],
                    c='black', alpha=0.3, s=100, marker=mark[i])

    plt.xlabel(iris['feature_names'][X_INDEX])
    plt.ylabel(iris['feature_names'][Y_INDEX])

# main
if __name__ == '__main__':
    preprocessing()
    train()
    print_result()
