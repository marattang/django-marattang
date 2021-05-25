from bs4 import BeautifulSoup
from urllib.request import urlopen

class BugsMusic(object):

    url = ''

    def __str__(self):
        return f'입력된 URL은 {self.url}입니다.'
    
    #리스트를 출력하기
    @staticmethod
    def printRanking(soup, pattern):
        for j in pattern:
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
                soup = BeautifulSoup(urlopen(bugs.url), 'lxml')
                pattern = ['title', 'artist']
                BugsMusic.printRanking(soup, pattern)
            elif menu == '3':
                pass
            elif menu == '4':
                pass
            else:
                print("Wrong Number")
                continue

BugsMusic.main()