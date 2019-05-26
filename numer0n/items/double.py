from module import standard_numer0n as nm

def use(info,turn,digit=3):
    while True:
        idx = input(f"{info[not turn]['name']}:表示させたい桁を指定してください")
        fin_flag, idx = check_idx(idx)
        if fin_flag: break
        else: print(idx)
    print("{0}さんの[{1}]桁目の数値は[{2}]です".format(
                info[turn]["name"],
                idx,info[turn]["ans"][idx-1]))
    
    value, eb = nm.call(info,turn)
    print("{} -> {} : {} ({})".format(info[turn]["name"],
                info[not turn]["name"],eb,value))
    if nm.isfin(eb,digit):
        return (True,turn)
    else: return (False,turn)

def check_idx(idx):
    if not idx.isdigit():
        return (False,"整数値ではありません")
    idx = int(idx) 
    if not (1 <= idx <= 3):
        return (False,"範囲外の数値を入力しています")
    return (True ,idx)
