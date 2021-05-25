from bs4 import BeautifulSoup
import urllib.request

class Melon(object):

    url = ''
    hdr = {'User-Agent': 'Mozilla/5.0'}
    class_name = []

    def __str__(self):
        return f'입력된 URL은 {self.url}입니다.'

    def set_class_name(self, class_name):
        self.class_name = class_name

    def printRanking(self):
        req = urllib.request.Request(self.url, headers=self.hdr)
        soup = BeautifulSoup(urllib.request.urlopen(req).read(), 'lxml')

        count = 0
        for i in soup.find_all(name='div', attrs=({"class":self.class_name[0]})):
            count += 1
            print(f'{str(count)} RANKING')
            print(f'title: {i.find("a").text}')

        count = 0
        for i in soup.find_all(name='div', attrs=({"class":self.class_name[1]})):
            count += 1
            print(f'{str(count)} RANKING')
            print(f'artist: {i.find("a").text}')

    def set_url(self):
        self.url = f'https://www.melon.com/chart/index.htm?dayTime={time}'

# https://www.melon.com/chart/index.htm?dayTime={time}
    @staticmethod
    def main():
        mel = Melon()
        while 1:
            menu = input('0.Exit 1.Input URL 2.Print Rank ')
            if menu == '0':
                break
            elif menu == '1':
                mel.url = input("Input URL")
                mel.time = input('time 예 : 2020122414')
            elif menu == '2':
                mel.class_name.append('ellipsis rank01')
                mel.class_name.append('ellipsis rank02')
                mel.printRanking()
            else:
                print('Wrong Number')
                continue

Melon.main()