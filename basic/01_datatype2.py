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

print('abcd' in ls)

# Tuple CRUD Example
tp = ('abcd', 786, 2.23, 'john', 70.2)
tinytp = (123, 'john')
# Create: tp 에 '100'을 추가 Create
# list(tp).append('100')

# tp[int(len(tp)) - 1].append(input('Add value'))
# Read: tp 의 목록을 출력
for i, j in enumerate(tp):
    print(f'tp의 {i}번째 : {j}')
# Update: tp와 tinytp 의 결합
tpmerge = tp+tinytp
# Delete: tp 에서 786을 제거
list(tp).remove(786)
for i, j in enumerate(tp):
    print(f'tp의 {i}번째 : {j}')

# dictionary CRUD Example
dt = {'abcd' : 786, 'john': 70.2}
tinydt = {'홍':'30세'}
# Create: dt 에 키값으로 'tom', 밸류로 '100'을 추가 Create
dt['tom'] = '100'
# Read: dt 의 목록을 출력
for key in dt:
    print(f'dt의 {key} : {dt[key]}')
# Update: dt와 tinydt 의 결합
dt.update(tinydt)
# Delete: dt 에서 'abcd' 제거
del dt['abcd']