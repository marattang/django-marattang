from bs4 import BeautifulSoup
import requests

class BugsMusic(object):

    url_base = 'https://music.bugs.co.kr/chart/track/realtime/total'

    url = ''
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []

    def set_url(self, date, time):
        self.url = requests.get(f'{self.url_base}?chartdate={date}&charthour={time}', headers=self.headers).text
    
    #리스트를 출력하기
    def printRanking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        for j in self.class_name:
            count = 0
            print(f'-------------------{j} Ranking----------------------')
            for i in soup.find_all(name='p', attrs=({"class": j})):
                count += 1
                print(f'{str(count)} RANKING')
                print(f'{j}: {i.find("a").text}')
    
    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = input("0.Exit \n 1.Input URL \n 2.get Ranking \n 3.Update \n 4.Delete \n")
            if menu == '0':
                break
            elif menu == '1':
                bugs.set_url(input('Input date ex : 20210526'), input('Input time ex : 08'))
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