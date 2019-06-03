# coding:utf-8
import random
import getpass
from user import human, cpu

def div(value1,value2):
    eat = bite = 0
    for idx,vx in enumerate(value1):
        for idy, vy in enumerate(value2):
            if (idx == idy) and (vx == vy):eat += 1
            if (idx != idy) and (vx == vy):bite += 1
    return (eat,bite)

def create_num(digit=3):
    return random.sample(range(10),k=digit)

def input_num(message,digit=3,pass_flag=False):
    fin_flag = False
    while not fin_flag:
        if pass_flag :value = getpass.getpass(message)
        else :value =input(message)
        fin_flag, value = check_num(value,digit)
        if not fin_flag:print(value)
    return value

def check_num(value,digit=3,str_flag=False):
    if len(value) != digit: return (False,"not match digit")
    if not str_flag : 
        if not value.isdigit():return (False,"not integer")
        else:value = [int(i) for i in [* value]]
    if not isdouble(value): return(False,"there is duplication")
    return (True,value)

def isdouble(value):
    for idx, v1 in enumerate(value):
        for idy, v2 in enumerate(value):
            if (idx != idy) and (v1 == v2):return False
    return True

def init_game(digit=3):
    player1 = human.init_info(digit)
    player2 = cpu.init_info(digit)
    return player1 + player2

def call(info,turn,digit=3):
    value = input_num(f"{info[turn]['name']}:",digit,False)
    eb = div(info[not turn]["ans"],value)
    return (value,eb)

def isfin(eat_bite,digit=3):
    if eat_bite[0] == digit:return True
    else :return False

