import pandas as pd


class Conversion(object):

    # 1. 1부터 10까지 요소를 가진 튜플을 생성하시오 (return)

    @staticmethod
    def tuple_create() -> ():
        return (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    # 2. 1번 튜플을 리스트로 전환하시오 (return)
    @staticmethod
    def tp_to_list(tp) -> []:
        return list(tp)

    # 3. 2번 리스트를 실수(float) 리스트 바꾸시오  (return)
    @staticmethod
    def ls_to_float(ls) -> []:

        # return self.t
        return [float(i) for i in ls]

    # 4. 3번 실수(float) 리스트을, 정수 리스트로 바꾸시오  (return)
    @staticmethod
    def f_to_list(ls) -> []:

        return [int(i) for i in ls]

    # 5. 4번 리스트를 딕셔너리로 전환하시오. 단 키는 리스트의 인덱스인데 str 로 전환하시오 (return)
    @staticmethod
    def ls_to_dict(ls) -> {}:

        # for i, j in enumerate(ls):
        # return dict(zip(ls, ls))
        return dict(zip([str(i) for i in ls], ls))
    # 6.'hello' 를 튜플로 전환하시오
    @staticmethod
    def str_to_tp() -> ():
        str = 'hello'
        ls = []
        [ ls.append(i) for i in list(str)]
        return tuple(ls)

    # 7. 6번 튜플을 리스트로 전환하시오
    @staticmethod
    def str_tp_to_list(tp) -> []:
        return list(tp)

    # 8. 5번 딕셔너리를 데이터프레임으로 전환
    @staticmethod
    def dict_to_df(d) -> object:
        #return pd.DataFrame(data=(d.values(), d.keys()))
        return pd.DataFrame.from_dict(d, orient='index')

    @staticmethod
    def main():
        i = 0
        f = 0.0
        s = ''
        ls = []
        t = ()
        d = {}
        df = pd.DataFrame()
        c = Conversion()
        while 1:
            m = input('0-exit 1-create tuple\n'
                      '2-convert list\n'
                      '3-convert float-list\n'
                      '4-convert int-list\n'
                      '5-list convert dictionary\n'
                      '6-str convert tuple\n'
                      '7-str tuple convert list\n'
                      '8-dict_to_df')
            if m == '0':
                break
            # 1.1부터 10까지 요소를 가진 튜플을 생성하시오 (return)
            elif m == '1':
                tp = c.tuple_create()
                print(c.tuple_create())
            # 2.1번 튜플을 리스트로 전환하시오 (return)
            elif m == '2':
                ls = c.tp_to_list(tp)
                print(c.tp_to_list(tp))
            # 3.2번 리스트를 실수(float) 리스트 바꾸시오  (return)
            elif m == '3':
                ls = c.tp_to_list(ls)
                print(c.ls_to_float(ls))
            # 4.3번 실수(float) 리스트을, 정수 리스트로 바꾸시오  (return)
            elif m == '4':
                ls = c.tp_to_list(ls)
                print(c.f_to_list(ls))
            # 5.4번 리스트를 딕셔너리로 전환하시오. 단 키는 리스트의 인덱스인데 str 로 전환하시오 (return)
            elif m == '5':
                d = c.ls_to_dict(ls)
                print(c.ls_to_dict(ls))
            # 6.'hello' 를 튜플로 전환하시오
            elif m == '6':
                tp = c.str_to_tp()
                print(c.str_to_tp())
            # 7.6번 튜플을 리스트로 전환하시오
            elif m == '7':
                ls = (c.str_tp_to_list(tp))
                print(c.str_tp_to_list(tp))
            # 5번 딕셔너리를 데이터프레임으로 전환
            elif m == '8':
                tp = c.tuple_create()
                ls = c.tp_to_list(tp)
                d = c.ls_to_dict(ls)
                print(c.dict_to_df(d))
            else:
                continue
Conversion.main()