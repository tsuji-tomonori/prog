import sys; sys.path.append('../module')
import standard_numer0n as nm
import high_low

def use(old_value,digit=3):
    while True:
        index = input("変更する桁を入力してください:")
        fin_flag, index = check_digit_index(index,digit)
        if fin_flag:break
        print(index)
    while True:
        num = input("変更する値を入力してください:")
        fin_flag, new_value = check_digit_num(index,num,old_value)
        if fin_flag:break
        print(new_value)
    return new_value

def check_digit_index(index,digit=3):
    if not index.isdigit():
        return (False,"整数値ではありません")
    index = int(index) - 1
    if not (0 <= index < digit):
        return (False,"値の範囲が不正です")
    return (True,index)

def check_digit_num(index,num,old_value):
    if not num.isdigit():
        return (False,"整数値ではありません")
    old_num = old_value[index]
    new_num = int(num)
    new_value = old_value.copy()
    new_value[index] = new_num
    old_high_low = high_low.use(old_value)[index]
    new_high_low = high_low.use(new_value)[index]
    if not old_high_low == new_high_low:
        return (False,f"{old_high_low}の中から数字を選んでください")
    if old_num == new_num:
        return (False,"前回と違う数字を選択してください")
    if not nm.isdouble(new_value):
        return (False,"重複があります")
    return (True,new_value)

