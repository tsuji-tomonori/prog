from enum import Enum,auto
import sys
from items import double,high_low,slash,target 
from module import standard_numer0n as nm
class AttackItem(Enum):
    DOUBLE = "d" 
    HIGH_LOW = "hl"
    SLASH = "sl"
    TARGET = "t"
    NONE = "n"

    def use_attack(self,info,turn,digit=3):
        fin_flag = False
        if self == AttackItem.DOUBLE:
            fin_flag, turn = double.use(info,turn,digit)
        elif self == AttackItem.HIGH_LOW:
            high_low_list = high_low.use(info[not turn]["ans"])
            print(f"HIGH_LOW > {info[not turn]['name']} : {high_low_list}")
        elif self == AttackItem.SLASH:
            slash_value = slash.use(info[not turn]["ans"])
            print(f"SLASH > {info[not turn]['name']} : {slash_value}")
        elif self == AttackItem.TARGET:
            idx = target.use(info[not turn]["ans"],info[not turn]["name"])
        elif self == AttackItem.NONE:
            pass
        else:
            print("コマンドが見つかりません")
        return (info,turn,fin_flag)
    
    @classmethod
    def return_item(cls,item_command):
        try:
            item_object = cls(item_command)
            return (True,item_object)
        except:
            return (False,None)

    
    @classmethod
    def print_list(cls):
        print(list(cls))
