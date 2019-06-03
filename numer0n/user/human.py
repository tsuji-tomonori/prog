from module import standard_numer0n as nm

def init_info(digit=3):
    info = [{"name": input("プレイヤー名を入力してください"),
            "ans": nm.input_num(message='ans',
                                digit=digit,
                                pass_flag=True)}]
    return info
