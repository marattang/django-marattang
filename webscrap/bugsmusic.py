from bs4 import BeautifulSoup
import requests

class BugsMusic(object):

    url_base = 'https://music.bugs.co.kr/chart/track/realtime/total'

    url = ''
    headers = {'User-Agent': 'Mozilla/5.0'}
    title_dict = {}

    def set_url(self, date, time):
        self.url = requests.get(f'{self.url_base}?chartdate={date}&charthour={time}', headers=self.headers).text
    
    def get_raking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        for i in soup.find_all(name='tr', attrs={"rowtype":"track"}):
            self.title_dict[f'{i.find("th").select_one("a").text}'] =  f'{i.find(name="td", attrs={"class":"left"}).find(name="p", attrs={"class":"artist"}).select_one("a").text}'


    def print_ranking(self):
        for i in self.title_dict:
            print(f'title_dict의 {i} :{self.title_dict[i]}')
        print(len(self.title_dict))

    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = input("0.Exit \n 1.Input URL \n 2.get_raking \n 3.print_ranking\n")
            if menu == '0':
                break
            elif menu == '1':
                bugs.set_url(input('Input date ex : 20210526'), input('Input time ex : 08'))
            elif menu == '2':
                print(f'Input URL is {bugs}')
                bugs.get_raking()
            elif menu == '3':
                bugs.print_ranking()
            else:
                print("Wrong Number")
                continue

BugsMusic.main()