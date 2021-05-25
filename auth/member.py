#리스트 없이 클래스만으로 사용하기

class Member(object):

    def __init__(self, user_id='', user_pw='', name='', email=''):
        self.user_id = user_id
        self.user_pw = user_pw
        self.name = name
        self.email = email

    def __str__(self):
        return f'user_id : {self.user_id}' \
               f'user_id : {self.user_pw}' \
               f'user_id : {self.name}' \
               f'user_id : {self.email}'

    def login(self):
        if input('user_id') == self.user_id:
            if input('user_pw') == self.user_pw:
                print('로그인 성공')
            else:
                print('비밀번호를 잘못입력하셨습니다.')
        else:
            print('아이디를 잘못입력하셨습니다.')

    def mypage(self):

        print(self)

    def join(self):
        self.user_id = input('user_id : ')
        self.user_pw = input('user_pw : ')
        self.name = input('name : ')
        self.email = input('email : ')

    def update_remove(self, menu):
        if self.user_id != '' and str(len(self.user_id)) != '0':
            if input('user_id') == self.user_id:
                if input('user_pw') == self.user_pw:
                    self.user_id = ''
                    self.user_pw = ''
                    self.name = ''
                    self.email = ''
                    print('삭제되었습니다.')
                else :
                    print('비밀번호를 잘못입력하셨습니다.')
            else :
                print('아이디를 잘못입력하셨습니다.')
            if menu == '4':
                self.join()
        else :
            print('사용자가 없습니다.')


    @staticmethod
    def main():
        member = Member()
        while 1:
            menu = input('0.Exit 1.회원가입 2.로그인 3.MYPAGE 4.회원정보수정 5.회원탈퇴')

            if menu == '0':
                break

            elif menu == '1':
                member.join()

            elif menu == '2':
                member.login()

            elif menu == '3':
                member.mypage()

            elif menu == '4':
                member.update_remove(menu)

            elif menu == '5':
                member.update_remove(menu)
            else:
                print('wrong number')

Member.main()