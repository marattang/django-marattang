from bs4 import BeautifulSoup
from urllib.request import urlopen


class BugsMusic(object):
    url = ''
    class_name = []

    def __str__(self):
        return f'입력된 URL은 {self.url}입니다.'

    # 리스트를 출력하기
    def printRanking(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        for j in self.class_name:
            count = 0
            print(f'-------------------{j} Ranking----------------------')
            for i in soup.find_all(name='p', attrs=({"class": j})):
                count += 1
                print(f'{str(count)} RANKING')
                print(f'{j}: {i.find("a").text}')

    ## https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01
    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = input("0.Exit \n 1.Input URL \n 2.get Ranking \n 3.Update \n 4.Delete \n")
            if menu == '0':
                break
            elif menu == '1':
                bugs.url = input('Input URL')
            elif menu == '2':
                print(f'Input URL is {bugs}')
                bugs.class_name.append("artist")
                bugs.class_name.append('title')
                bugs.printRanking()
            elif menu == '3':
                pass
            elif menu == '4':
                pass
            else:
                print("Wrong Number")
                continue


BugsMusic.main()