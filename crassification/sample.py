# coding: UTF-8
import numpy as np
from sklearn import datasets
from sklearn import tree
from sklearn import metrics

# 変数
images = [] # 画像データ
labels = [] # 正解ラベル
flag_3_8 = np.array([]) # 3 と 8 の位置を示す
train_size = 0 # 学習データ数
classifier = None # 分類器

# データ前処理
def preprocessing():
    
    # グローバル変数宣言
    global flag_3_8,images,labels

    # 手書き数字データの読み込み
    digits = datasets.load_digits()

    # 3 と 8 のデータの位置を求める(bool)
    flag_3_8 = (digits.target == 3) +  (digits.target == 8)

    # 3 と 8 のデータ読み込み
    images = digits.images[flag_3_8]
    labels = digits.target[flag_3_8]

    # 画像データの一次元化
    images = images.reshape(images.shape[0],-1)

    return [images,labels]

# 学習
def train():
    
    # グローバル変数宣言
    global train_size,classifier

    # 学習データの選択
    n_samples = len(flag_3_8[flag_3_8])
    train_size = int(n_samples * 3 / 5)

    # 分類器の生成
    classifier = tree.DecisionTreeClassifier()

    # 学習
    classifier.fit(images[:train_size],labels[:train_size])
    return [classifier,train_size]

# 評価
def evaluation():

    # 正解ラベルの呼び出し
    expected = labels[train_size:]

    # 分類
    predicted = classifier.predict(images[train_size:])

    # 正答率の計算
    accuracy_score = metrics.accuracy_score(expected,predicted)
    print('正答率:',accuracy_score)
    return accuracy_score

# main
if __name__ == '__main__':
    
    preprocessing()
    train()
    evaluation()
