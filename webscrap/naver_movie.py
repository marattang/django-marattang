import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
class NaverMovie(object):
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
    rank_dict = {}
    df = None

    def get_ranking(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        count = 1
        for i in soup.find(name="table", attrs=({"class":"list_ranking"})).find_all(name='tr'):

            if i.find(name="td", attrs=({"class":"title"})) != None:
                self.rank_dict[count] = i.find(name="td", attrs=({"class":"title"})).div.a.text
                count += 1

    def print_ranking(self):
        for key in self.rank_dict:
            print(f'{key}위 : {self.rank_dict[key]}')

    def to_data_frame(self):
        self.df = pd.DataFrame.from_dict(self.rank_dict, orient='index')
        print(self.df)

    def to_csv_save(self):
        pass

    @staticmethod
    def main():
        movie = NaverMovie()
        while 1:
            menu = input('0.Exit 1.get_ranking 2.print_ranking 3.to_data_frame 4.to_csv_save')
            if menu == '0':
                break
            elif menu == '1':
                movie.get_ranking()
            elif menu == '2':
                movie.print_ranking()
            elif menu == '3':
                movie.to_data_frame()
            elif menu == '4':
                movie.to_csv_save()
            else:
                print("wrong number")

NaverMovie.main()