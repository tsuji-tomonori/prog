import random
import getpass

def div(value1,value2):
    eat = bite = 0
    for idx,vx in enumerate(value1):
        for idy, vy in enumerate(value2):
            if (idx == idy) and (vx == vy):eat += 1
            if (idx != idy) and (vx == vy):bite += 1
    return (eat,bite)

def create_num(digit):
    return random.sample(range(10),k=digit)

def input_num(message,digit,pass_flag):
    fin_flag = False
    while not fin_flag:
        if pass_flag :value = getpass.getpass(message)
        else :value =input(message)
        fin_flag, value = check_num(value,digit)
        if not fin_flag:print(value)
    return value

def check_num(value,digit):
    if not value.isdigit():return (False,"整数値ではありません")
    if len(value) != digit: return (False,"指定された桁と一致しません")
    value_list = [int(i) for i in [* value]]
    for idx, v1 in enumerate(value_list):
        for idy, v2 in enumerate(value_list):
            if (idx != idy) and (v1 == v2):return (False,"重複があります")
    return (True,value_list)

def game(digit):
    info = [{"name": input("プレイヤー名を入力してください:"),
            "ans": input_num('ans:',3,True)},
            {"name": input("プレイヤー名を入力してください:"),
            "ans": input_num('ans:',digit,True)}]
    print("---- game start!! ----")
    fin_flag = False
    turn  = False
    while not fin_flag:
        value = input_num("call:",digit,False)
        eb = div(info[not turn]["ans"],value)
        print("{} -> {} :  {} ({})".format(info[turn]["name"],
            info[not turn]["name"],eb,value))
        if eb[0] == digit: fin_flag = True
        else :turn = not turn
        
if __name__ == '__main__':
    DIGIT = 3
    game(DIGIT)
