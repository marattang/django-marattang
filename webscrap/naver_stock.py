import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup


class Naverstock(object):
    url = "https://finance.naver.com/sise/sise_market_sum.nhn"
    driver_path = 'C:/Program Files/Google/Chrome/chromedriver'
    classes = ''
    corp_nm = []
    corp_cd = []
    realtime_price = []
    realtime_rate = []
    market_cap = []
    df = None

    def get_data(self):
        chrome_driver = webdriver.Chrome(executable_path=self.driver_path)
        chrome_driver.get(self.url)
        soup = BeautifulSoup(chrome_driver.page_source, 'html.parser')
        data = soup.find_all('tr', attrs=({"onmouseover":"mouseOver(this)"}))

        for i in data:
            self.corp_nm.append(i.find_all("td")[1].a.text)
            self.corp_cd.append(i.find_all("td")[1].a['href'].split('=')[1])
            self.realtime_price.append(i.find_all("td")[2].text)
            self.realtime_rate.append(i.find_all("td")[4].span.text.replace('\t', '').replace('\n', ''))
            self.market_cap.append(i.find_all("td")[6].text)

        chrome_driver.close()

    def to_dataframe(self):
        self.df = pd.DataFrame(data={'corp_cd':self.corp_cd,'corp_nm':self.corp_nm,'realtime_price':self.realtime_price,'realtime_rate':self.realtime_rate,'market_cap':self.market_cap})
        print(self.df)

    def df_to_csv(self):
        path = './data/naver_stock.csv'

        self.df.to_csv(path, na_rep='NaN', sep=',')

    @staticmethod
    def main():
        naver = Naverstock()
        while 1:
            menu = input('0.Exit 1.get_data 2.to_dataframe 3.to_csv')
            if menu == '0':
                break
            elif menu == '1':
                naver.get_data()
            elif menu == '2':
                naver.to_dataframe()
            elif menu == '3':
                naver.df_to_csv()
            else:
                print("wrong number")
                continue

Naverstock.main()