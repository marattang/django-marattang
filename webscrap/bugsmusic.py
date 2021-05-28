import pandas as pd
from bs4 import BeautifulSoup
import requests

class BugsMusic(object):

    url_base = 'https://music.bugs.co.kr/chart/track/realtime/total'

    url = ''
    headers = {'User-Agent': 'Mozilla/5.0'}
    dict = {}
    df = None

    def set_url(self, date, time):
        self.url = requests.get(f'{self.url_base}?chartdate={date}&charthour={time}', headers=self.headers).text
    
    def get_raking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        for i in soup.find_all(name='tr', attrs={"rowtype":"track"}):
            self.dict[f'{i.find("th").a.text}'] =  f'{i.find(name="td", attrs={"class":"left"}).find(name="p", attrs={"class":"artist"}).a.text}'

    def print_ranking(self):
        for i in self.dict:
            print(f'title_dict의 {i} :{self.dict[i]}')
        print(len(self.dict))

    def dict_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dict, orient='index')
        print(self.df)

    def data_to_csv(self):
        path = './data/bugs.csv'
        self.df.to_csv(path, sep=',', encoding='utf-8-sig', na_rep='NaN')

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
                bugs.get_raking()
            elif menu == '3':
                bugs.print_ranking()
            elif menu == '4':
                bugs.dict_to_dataframe()
            elif menu == '5':
                bugs.data_to_csv()
            else:
                print("Wrong Number")
                continue

BugsMusic.main()