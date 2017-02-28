USER_INFO = {'blx': '123'}
AUTH_DIC={
    'AUTH_FLAG': False
}
pre = '''
1:login
2:change password'''


def test(func):
    def prvi():
        if AUTH_DIC['AUTH_FLAG']==False:
            print('login first!')
        else:
            func()
    return prvi


def login(username, password):
    if username == 'blx'and password == '123':
        print('login successful!')
        return True
    else:
        print('login fail')


@test
def chpass():
    new_password=input('entre new password:')
    USER_INFO['evil']=new_password


def login_main():
    while True:
        print(pre)
        choice=input('entre your choice:')
        if choice=='1':
            username=input('entre your login username:')
            password=input('entre your login password:')
            res=login(username,password)
            if res:
                AUTH_DIC['AUTH_FLAG']=True
                continue
            else:
                AUTH_DIC['AUTH_FLAG']=False
                continue
        elif choice=='2':
            chpass()
            print(USER_INFO)


if __name__ == '__main__':
    login_main()

