'''
구구단 프로그램은 단을 입력받아서 입력받은 단위 1~ 9의 곱을 출력하는 어플이다.
'''
class Gugudan(object):

    dan = 0
    dict = {}

    def multi(self):

        self.dan = int(input('숫자를 입력해주세요.'))

        for i in range(1, 10):
            print(f'{self.dan} * {i} = {self.dan*i}')

    def all_dan(self):

        for i in range(2, 10):
            print(f'******{i}단******')
            for j in range(1, 10):
                print(f'{i} * {j} = {i * j}')

    def print_dict_dan(self):
        for i in range(1, 10):
            self.dict[i] = self.dan * i
        print('딕셔너리 출력')
        print(self.dict)
        d = self.dict
        for k in d.keys():
            print(f'{self.dan} * {k} = {d.get(k)}')

    @staticmethod
    def main():
        gugudan = Gugudan()
        while 1:
            menu = input('0.Exit 1.구구단 2.all dan 3.input dan with dict')
            if menu == '0':
                break
            elif menu == '1':
                #gugudan.dan = int(input('숫자 입력'))
                gugudan.multi()
            elif menu == '2':
                gugudan.all_dan()
            elif menu == '3':
                gugudan.dan = int(input('단 입력'))
                gugudan.print_dict_dan()

Gugudan.main()