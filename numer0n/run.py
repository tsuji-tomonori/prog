# coding:utf-8
from module import standard_numer0n as nm
from items import attack_item

def game(digit=3):
    info = nm.init_game(digit)
    turn = False
    while True:
        while True:
            attack_item.AttackItem.print_list()
            comment = f"{info[turn]['name']}:攻撃用アイテムのコマンドを入力してください:"
            flag ,item_object = attack_item.AttackItem.return_item(input(comment))
            if flag:break
            print("コマンドに間違いがあります")
        info, turn, fin_flag = item_object.use_attack(info,turn,digit)
        if fin_flag:return info[turn]["name"]
        value, eb = nm.call(info,turn,digit)
        print("{} -> {} : {} ({})".format(
                                    info[turn]["name"],
                                    info[not turn]["name"],
                                    eb,
                                    value))
        if nm.isfin(eb,digit):
            return (info[turn]["name"],info)
        else:
            turn = not turn

if __name__ == "__main__":
    DIGIT = 3
    print("-"*4 + "game start!" ,"-"*4)
    win_name,info = game(DIGIT)
    print("-"*4 + "game fin:" ,"-"*4)
    print(f"winner : {win_name}")
    print(info)
