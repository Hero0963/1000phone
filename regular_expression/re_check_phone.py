import re


def get_phone():
    while True:
        phone = input('請輸入手機號碼：')
        if len(phone) == 10 and re.match(r'09\d{8}', phone):
            print('號碼正確')
            return phone
        else:
            print('號碼有誤，請重新輸入手機號碼')


get_phone()
