from enum import Enum,auto
import sys
from items import change,shuffle 
from module import standard_numer0n as nm
class DefenceItem(Enum):
    CHANGE = "c"
    SHUFFLE = "sh"
    NONE = "n"

    def use_defence(self,info,turn,digit=3):
        fin_flag = False
        if self == DefenceItem.CHANGE:
            info[not turn]["ans"] = change.use(info[not turn]["ans"],digit)
        elif self == DefenceItem.SHUFFLE:
            info[not turn]["ans"] = shuffle.use(info[not turn]["ans"],digit)
        elif self == DefenceItem.NONE:
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
