def use(ans,name):
    while True:
        num = input("数字を指定してください:")
        fin_flag ,num = check_num(num)
        if fin_flag:break
        print(num)
    try:
        idx = ans.index(num)
        print(f"{name}さんは[{num}]を[{idx+1}]桁目にて使用しています")
        return idx
    except:
        print(f"{name}さんは[{num}]を使用していません")
        return -1

def check_num(num):
    if not num.isdigit():
        return (False,"整数ではありません")
    num = int(num)
    if not (0 <= num <= 9):
        return (False,"範囲外の数値を入力しています")
    return (True,num)
