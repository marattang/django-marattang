from bs4 import BeautifulSoup

class Bs_Demo(object):

    html_doc = '' #3번째 줄 때문에 init이 존재.

    # def __init__(self, html_doc=''):
    #     self.html_doc = html_doc

    def __str__(self):

        return self.html_doc

    @staticmethod
    def main():

        bs_Demo = Bs_Demo()

        while 1:

            menu = input('0.Exit 1.Input html_doc 2. all html print 3. print title')

            if menu == '0':
                break
            elif menu == '1':
                bs_Demo.html_doc = """<html><head><title>The Dormouse's story</title></head>
                                    <body>
                                    <p class="title"><b>The Dormouse's story</b></p>
                                    
                                    <p class="story">Once upon a time there were three little sisters; and their names were
                                    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
                                    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
                                    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
                                    and they lived at the bottom of a well.</p>
                                    
                                    <p class="story">Test Value</p>
                                    """
            elif menu == '2':
                soup = BeautifulSoup(bs_Demo.html_doc, 'html.parser')
                print(soup.prettify())
            elif menu == '3':
                soup = BeautifulSoup(bs_Demo.html_doc, 'html.parser')
                print(soup.title.string)
            else:
                print('Wrong Number')
                continue

Bs_Demo.main()