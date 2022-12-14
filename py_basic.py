import sys
import decimal

# 숫자형
a = 10

# 최대 숫자?
a = sys.maxsize # Reference임, 진짜 maxsize는?
b = sys.maxsize + 100 # 100 더한 값 출력 가능

print(f'{a}, {b}')

d = 0.1 + 0.1 + 0.1 - 0.3

print(f'{d}')

e = decimal.Decimal('0.1') * 3 - decimal.Decimal('0.3')
print(e)
print(f'{e}')

# 문자형
str1 = 'Hello Python'
print(str1)
print(f'{str1[0]}, {str1[0:5]}, {str1[::-1]}') # indexing, slicing(start<=index<end), [start:end:step]

# 산술 연산자
a, b, c = 3, 25, 2
print(f'{a+b}, {a/b}, {a//b}, {b%a}') # 덧셈, 나눗셈, 몫, 나머지

# 문자열 연산자
print('*'+'*', '*'*5)

# 비교 연산자 (논리값 반환)
print(f'{a==b}')

# 논리 연산자 (논리값 반환)
print(f'{True and True}')

# if 문
a = 3
if a%2 == 0:
    print('짝수')
else:
    print('홀수')

c = '짝수' if a%2 == 0 else '홀수' #3항 연산자
print(c)

# for
for i in range(1,11):
    print(f'{"*"*i}')

# 자료구조
# list 가변형
a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)
print(a*3)

c = [n*3 for n in a] # 리스트 컴프리핸션 (요소별 처리)
print(c)

a =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#b = range(1,11)

print(f'{a[0]}, {a[0:5]}, {a[::-1]}')

a[0] = 20       # list는 데이터 변경 가능

#print(f'{b[0]}, {b[0:5]}, {b[::-1]}')
#print(f'{type(a)},{type(b)}')

## tuple 불변형, 원본 데이터 보호!
a = (1, 2, 3)
print(f'{a[0]}, {a[::-1]}')
#a[0] = 20 # 오류 출력, 변경 불가

b, c, d = a     # unpacking
print(f'{b}, {c}, {d}')

e = (b,c)       # packing
print(f'{e}')

# dictionary; 예전에는 key value를 써서 어떻게든 연산 시간 줄이려고했는데, 이제는 CPU 충분히 빨라서 안 헷갈리는게 더 낫다
a = {'name': 'TV', 'price':10000}

print(a['name'])
a['price'] = 100000

# set; 매우 빠름, 중복 허용 X, 집합
a = {1, 2, 3, 4, 5}
#print(a[0])    # 오류 발생, indexing으로 접근 불가
b = list(a)     # tuple, dict, set << 생성자
print(b[0])

b = {5, 6, 7}

print(a | b)                # 합집합
print(a & b)                # 교집합
print((a | b) - (a & b))    # 여집합
# 유사도 = 교집합/합집합
print(a >= {2,3})           # 부분집합

# 함수
print(10+20) # pool에 이미 있는 것을 stack에서 가르키는 것

# Hello world!! 10번 출력
def hello_world(n):     # n 지역변수 초기화
    for i in range(n):
        print(f'{i}. "Hello world!!"')

hello_world(1)
hello_world(10)

class Calc():           # Class는 인간이 분류하는 것을 그대로 구현하기 좋은 형태
    def __init__(self): # class 불러올시 자동 실행되는 것
        self.a = 0      # 인스턴스 변수; 클래스 내에서만 접근 가능한 변수
        self.b = 0

    def add(self):      # 클래스 안에 있는 함수 >> method
        return self.a + self.b

    def multi(self):
        return self.a * self.b

calc = Calc()           # 클래스 안에 있는 함수는 python.exe가 자동으로 올리지 못함, 직접 메모리에 올려야 함
calc.a = 1
calc.b = 2
print(f'{calc.add()}, {calc.multi()}')

calc1 = Calc()
calc1.a = 10
calc1.b = 20
print(f'{calc1.add()}, {calc1.multi()}')

# lambda 표기법
def fn_calc(a, b, opt): # 매개변수와 본체만 쓰는 것, 무명 함수 ex) x = a*x + b
    print(opt(a,b))

def add(a, b):
    return a+b
fn_calc(1,2,add)

fn_calc(1, 2, lambda x,y:x+y)   # add + fn_calc 결과와 동일한데 한줄로




