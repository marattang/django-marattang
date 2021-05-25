import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from requests_html import HTMLSession

class Stock(object):
    url = ''
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    keyword = []
    rate = []

    def printRanking(self):

        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        count = 1
        for i in soup.find_all(name='tr'):
            if i.find("a") == None :
                pass
            else :
                self.keyword.append(i.find("a").text)
                count += 1
            if i.find("span", class_="tah p11 red01") == None:
                pass
            else :
                self.rate.append(i.find("span", class_="tah p11 red01").text.replace("\t", "\n").replace("\n", ""))

        return self.keyword, self.rate

# https://finance.naver.com/sise/lastsearch2.nhn
    @staticmethod
    def main():

        stock = Stock()

        while 1:
            menu = input('0.Exit 1.Input URL 2. PrintRanking')

            if menu == '0':
                break

            elif menu == '1':
                stock.url = input('Input URL')

            elif menu == '2':
                stock.search.append('stock_name')
                stock.search.append('rate')
                print(stock.printRanking())

            else:
                input('Wrong Number')

Stock.main()