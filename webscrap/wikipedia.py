class Wikipedia(object):

    def __init__(self, url):
        self.url = url

    def __str__(self):

        return self.url

    @staticmethod
    def main():
        while 1:
            menu = input('0.Exit \n1.input URL \n2.Print URL \n3.Update \n4.Delete')

            if menu == '0':
                break
            elif menu == '1':
                wi = Wikipedia(input('URL INPUT'))
            elif menu == '2':
                print(f'입력된 URL : {wi}')
            elif menu == '3':
                pass
            elif menu == '4':
                pass
            else:
                print('잘못 입력하셨습니다.')
                continue

Wikipedia.main()