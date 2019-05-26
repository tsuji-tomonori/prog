from module import standard_numer0n as nm

def use(old_value,digit=3):
    fin_flag = False
    while not fin_flag:
        value = input("変更後の値を入力してください:")
        fin_flag, value = nm.check_num(value,digit)
        if not fin_flag: print(value)
        elif sorted(old_value) != sorted(value):
            print("使用する数字の変更はできません")
            fin_flag = False
    return value
