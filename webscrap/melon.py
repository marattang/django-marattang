from bs4 import BeautifulSoup
import urllib.request

class Melon(object):

    url = ''
    url_base = 'https://www.melon.com/chart/index.htm'
    hdr = {'User-Agent': 'Mozilla/5.0'}
    rank_dict = {}

    def __str__(self):
        return f'입력된 URL은 {self.url}입니다.'

    def set_url(self):
        self.url = f'{self.url_base} + ?dayTime={(input("Time ex 2021052616:"))}'

    def get_raking(self):
        req = urllib.request.Request(self.url, headers=self.hdr)
        soup = BeautifulSoup(urllib.request.urlopen(req).read(), 'lxml')

        for i in soup.findAll(name="table")[0].tbody.findAll('tr'):

            self.rank_dict[i.findAll("td")[3].div.div.find(name="a").text] = i.findAll("td")[3].div.findAll("div")[2].find(name="a").text

    def set_url(self):

        self.url = f'https://www.melon.com/chart/index.htm?dayTime={input("INPUT URL")}'

    def print_raking(self):
        for key in self.rank_dict:
            print(f'rank_dict의 {key} : {self.rank_dict[key]}')

# https://www.melon.com/chart/index.htm?dayTime={time}
    @staticmethod
    def main():
        mel = Melon()
        while 1:
            menu = input('0.Exit 1.Input URL 2.Print Rank ')
            if menu == '0':
                break
            elif menu == '1':
                mel.set_url()
            elif menu == '2':
                # pass
                mel.get_raking()
            elif menu == '3':
                mel.print_raking()
            else:
                print('Wrong Number')
                continue

Melon.main()