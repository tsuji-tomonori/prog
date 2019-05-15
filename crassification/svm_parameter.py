# coding: UTF-8
import numpy as np
from sklearn import datasets
from sklearn import svm
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

    return [images,labels,flag_3_8]

# 学習
def train(C,gamma):
    
    # グローバル変数宣言
    global train_size,classifier

    # 学習データの選択
    n_samples = len(flag_3_8[flag_3_8])
    train_size = int(n_samples * 3 / 5)

    # 分類器の生成
    # 違う分類器を試す場合, 以下を変更する
    classifier = svm.SVC(C=C,gamma=gamma)

    # 学習
    classifier.fit(images[:train_size],labels[:train_size])
    return [classifier,train_size]

# 評価
def evaluation():

    # 正解ラベルの呼び出し
    expected = labels[train_size:]

    # 分類
    predicted = classifier.predict(images[train_size:])

    # 混合行列の計算
    confusion_matrix = metrics.confusion_matrix(expected,predicted)

    # 正答率の計算
    accuracy_score = metrics.accuracy_score(expected,predicted)

    # 適合率の計算
    precision_score = metrics.precision_score(expected,predicted,pos_label=3)

    # 再現率の計算
    recall_score = metrics.recall_score(expected,predicted,pos_label=3)

    # F値の計算
    f1_score = metrics.f1_score(expected,predicted,pos_label=3)
    
    print('混合行列:\n',confusion_matrix)
    print('正答率:',accuracy_score)
    print('適合率:',precision_score)
    print('再現率:',recall_score)
    print('F値:',f1_score)
    return [confusion_matrix,accuracy_score,precision_score,recall_score,f1_score]

# main
if __name__ == '__main__':

    for i in range(1,20):
        print("パラメータC:",i)
        preprocessing()
        train(i,0.001)
        evaluation()
