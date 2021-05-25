from bs4 import BeautifulSoup
import urllib.request

class Melon(object):

    url = ''
    hdr = {'User-Agent': 'Mozilla/5.0'}

    def __str__(self):
        return f'입력된 URL은 {self.url}입니다.'

    @staticmethod
    def printRanking(soup, value, type):
        count = 0
        for i in soup.find_all(name='div', attrs=({"class":value})):
            count += 1
            print(f'{str(count)} RANKING')
            print(f'{type}: {i.find("a").text}')

# https://www.melon.com/chart/index.htm
    @staticmethod
    def main():
        mel = Melon()
        while 1:
            menu = input('0.Exit 1.Input URL 2.Print Rank ')
            if menu == '0':
                break
            elif menu == '1':
                mel.url = input("Input URL")
            elif menu == '2':
                print(f'Input URL is {mel.url} 입니다.')
                req = urllib.request.Request(mel.url, headers=mel.hdr)
                soup = BeautifulSoup(urllib.request.urlopen(req).read(), 'lxml')

                Melon.printRanking(soup, "ellipsis rank01", 'title')
                Melon.printRanking(soup, "ellipsis rank02", 'artist')
            else:
                print('Wrong Number')
                continue

Melon.main()