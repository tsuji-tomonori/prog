import glob
import os
import sys
import numpy as np
from skimage import io
from sklearn import datasets

from sklearn import svm,metrics

# 変数
IMAGE_SIZE = 40
COLOR_BYTE = 3
CATEGORY_NUM = 6

def load_handimage(path):
    
    # ファイル一覧を取得
    files = glob.glob(os.path.join(path,'*/*.png'))

    # イメージとラベル領域を確保
    images = np.ndarray((len(files),IMAGE_SIZE,IMAGE_SIZE,
                            COLOR_BYTE), dtype = np.uint8)
    labels = np.ndarray(len(files),dtype = np.int)

    # イメージとラベルを読み込む
    for idx, file in enumerate(files):
        # イメージ読み込み
        image = io.imread(file)
        images[idx] = image

        # ディレクトリ名よりラベルを取得
        label = os.path.split(os.path.dirname(file))[-1]
        labels[idx] = int(label)

    # scikit-learn の他のデータセットの形式に合わせる
    flat_data = images.reshape((-1,IMAGE_SIZE * IMAGE_SIZE * COLOR_BYTE))
    images = flat_data.view()

    return datasets.base.Bunch(data=flat_data, # データ
                                target=labels.astype(np.int), # データ属性
                                target_names=np.arange(CATEGORY_NUM), # 属性名
                                images=images, # 画像データ(=データ)
                                DESCR=None)

# main
if __name__ == '__main__':

    # 変数
    train_path = '../data/my_learn10'
    test_path = '../data/other_test2'

    # 学習データの読み込み
    train = load_handimage(train_path)

    # 手法:SVM
    classifier = svm.LinearSVC()

    # 学習
    classifier.fit(train.data, train.target)

    # テストデータの読み込み
    test = load_handimage(test_path)

    # テスト
    predicted = classifier.predict(test.data)

    # 結果表示
    print("正答率:",metrics.accuracy_score(test.target,predicted))
