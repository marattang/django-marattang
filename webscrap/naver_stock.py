from selenium import webdriver
from bs4 import BeautifulSoup

class Naverstock(object):
    url = "https://finance.naver.com/sise/sise_market_sum.nhn"
    driver_path = 'C:/Program Files/Google/Chrome/chromedriver'
    classes = ''
    corp_nm = []
    crop_cd = []
    realtime_price = []
    realtime_rate = []
    market_cap = []
    df = None

    def get_data(self):
        chrome_driver = webdriver.Chrome(executable_path=self.driver_path)
        chrome_driver.get(self.url)
        soup = BeautifulSoup(chrome_driver.page_source, 'html.parser')
        data = soup.find_all('tr', attrs=({"onmouseover":"mouseOver(this)"}))
        # print(data)
        # corp_nm
        for i in data:
            print(i.find_all("td")[1].a.text)
        # corp_cd

        # realtime_price
        for i in data:
            print(i.find_all("td")[2].text)
        # realtime_rate
        for i in data:
            print(i.find_all("td")[3].span.text)
        # market_cap
        for i in data:
            print(i.find_all("td")[5].text)
        chrome_driver.close()
    def to_dataframe(self):
        pass

    def to_csv(self):
        pass

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
                pass
            elif menu == '3':
                pass
            else:
                print("wrong number")
                continue

Naverstock.main()