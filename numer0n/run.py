# coding:utf-8
from module import standard_numer0n as nm

def game(digit=3):
    info = nm.init_game(digit)
    turn = False
    while True:
        value, eb = nm.call(info,turn)
        print("{} -> {} : {} ({})".format(info[turn]["name"],
                info[not turn]["name"],eb,value))
        if nm.isfin(eb,digit):
            return info[turn]["name"]
        else:
            turn = not turn

if __name__ == "__main__":
    DIGIT = 3
    print("-"*4 + "game start!" ,"-"*4)
    win_name = game(DIGIT)
    print("-"*4 + "game fin:" ,"-"*4)
    print(f"winner : {win_name}")
