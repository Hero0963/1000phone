import re


def get_email():
    pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
    p = re.compile(pattern)
    while True:
        email = input('請輸入你的電子信箱：')

        # if re.match(pattern, email):
        if p.match(email):
            print("你的電子信箱為: ", email)
            return email
        else:
            print('檢查有誤，請重新輸入電子信箱')


get_email()
