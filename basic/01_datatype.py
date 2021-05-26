# *****************
# --- Data Type ---
# *****************
'''
Python has Five standard types
scalar
    Numbers : int, float, complex
    String : str
vector : List, Tuple, Dictionary, Set
hello = 'hello'
print(hello)
print(hello[0])
print(hello[2:5])
print(hello[2:])
'''
# List CRUD Example
ls = ['abcd', 786, 2.23, 'john', 70.2]
tinyls = [123, 'john']
# Create: ls 에 '100'을 추가 Create
ls.append('100')
# Read: ls 의 목록을 출력
for i, j in enumerate(ls):
    print(f'ls의 {i}번째 : {j}')
# Update: ls와 tinyls 의 결합
ls.extend(tinyls)
# Delete: ls 에서 786을 제거
ls.remove(786)

# Tuple CRUD Example
tp = ('abcd', 786, 2.23, 'john', 70.2)
tinytp = (123, 'john')
# Create: tp 에 '100'을 추가 Create
# Read: tp 의 목록을 출력
# Update: tp와 tinytp 의 결합
tpmerge = tp+tinytp
# Delete: tp 에서 786을 제거 리스트로 형변환해서 제거

# dictionary CRUD Example
dt = {'abcd' : 786, 'john': 70.2}
tinydt = {'홍': '30세'}

# Create: dt 에 '100'을 추가 Create
dt['100'] = '100'

# Read: dt 의 목록을 출력
for key in dt:
    print(f'dt의 {key} 값 : {dt[key]}')
# Update: dt와 tinydt 의 결합
dt.update(tinydt)
# Delete: dt 에서 'abcd' 제거
del dt['abcd']
