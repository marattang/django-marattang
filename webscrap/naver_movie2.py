import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
class NaverMovie(object):

    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
    classes = ''
    driver_path = 'C:/Program Files/Google/Chrome/chromedriver'
    df = None
    rank_dict = {}

    def scrap(self):

        chromedriver = webdriver.Chrome(executable_path=self.driver_path)
        chromedriver.get(self.url) #url을 드라이버에 넣어버림 크롬 드라이버는 들어주게 도와줄 뿐

        soup = BeautifulSoup(chromedriver.page_source, 'html.parser')
        data = soup.find_all(name='div', attrs={"class":self.classes})
        self.rank_dict = {i:j.a.text for i, j in enumerate(data)}
        chromedriver.close()

    def dict_to_df(self):
        self.df = pd.DataFrame(data=self.rank_dict.values(), index=self.rank_dict.keys())

    def print_df(self):
        print(self.df)

    def df_to_csv(self):
        url = './data/movieRanking.csv'
        self.df.to_csv(url, na_rep='NaN')

if __name__ == '__main__':
    naver = NaverMovie()
    # tit3
    naver.classes = 'tit3'
    naver.scrap() # 생성자 호출해서 함수 실행하기.
    naver.dict_to_df()
    naver.print_df()
    naver.df_to_csv()
