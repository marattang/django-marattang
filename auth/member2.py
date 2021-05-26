#리스트 사용하기

class Member(object):

# 멤버 리스트
    memberList = []
#비밀번호 체크 5번 걸릴때마다 잠금.
    pw_check = {}

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
        user_id = input('user_id : ')
        self.memberList.append(user_id, input('user_pw : '), input('name : '), input('email : '))
        self.pw_check[f'{user_id}'] = 0
    def id_check(self):

        user_id = input('user id')
        for i in self.memberList:
            if i.user_id == input('user id') || self.pw_check[f'{i.user_id}' % 5 == 0:

                if i.user_pw == input('user pw'):
                    print('로그인 되었습니다.')

                else:
                    print('비밀번호를 틀리셨습니다.')
                    self.pw_check[f'{i.user_id}'] += 1

                    if self.pw_check[f'{i.user_id}' % 5 == 0]:
                        print('계정이 잠깁니다.')
            else:
                print('없는 아이디입니다.')
                break

    def update_remove(self, menu):
        for i in self.memberList:
            if self.memberList.user_id != '' and str(len(self.memberList.user_id)) != '0':
                if input('user_id') == self.memberList.user_id:
                    if input('user_pw') == self.memberList.user_pw:
                        self.memberList.user_id = ''
                        self.memberList.user_pw = ''
                        self.memberList.name = ''
                        self.memberList.email = ''
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