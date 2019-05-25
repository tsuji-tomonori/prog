from enum import Enum,auto
import sys
from items import double,high_low,slash,target 
from module import standard_numer0n as nm
class Item(Enum):
    DOUBLE = auto()
    HIGH_LOW = auto()
    SLASH = auto()
    TARGET = auto()

    def use_attack(item,info,turn,digit=3):
        fin_flag = False
        if item == Item.DOUBLE:
            fin_flag, turn = double.use(info,turn,digit)
        elif item == Item.HIGH_LOW:
            high_low_list = high_low.use(info[not turn]["ans"])
            print(f"HIGH_LOW > {info[not turn]['name']} : {high_low_list}")
        elif item == Item.SLASH:
            slash_value = slash.use(info[not turn]["ans"])
            print(f"SLASH > {info[not turn]['name']} : {slash_value}")
        elif item == Item.TARGET:
            idx = target.use(info[not turn]["ans"],info[not turn]["name"])
        else:
            print("コマンドが見つかりません")
        return (info,turn,fin_flag)

